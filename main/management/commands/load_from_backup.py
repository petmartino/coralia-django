import sqlite3
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import make_aware
from main.models import Tag, RepertoirePiece
from quotes.models import Quote, Program, ProgramItem

class Command(BaseCommand):
    help = 'Loads data from the old site.db backup file (backup.sql).'

    def handle(self, *args, **options):
        backup_sql_file = os.path.join(settings.BASE_DIR, 'backup.sql')
        temp_db_file = os.path.join(settings.BASE_DIR, 'old_data.db')

        if not os.path.exists(backup_sql_file):
            self.stdout.write(self.style.ERROR(f"Backup file not found at {backup_sql_file}. Please place it in the project root."))
            return

        # Restore SQL dump to a temporary SQLite file
        self.stdout.write("Restoring backup.sql to a temporary database...")
        if os.path.exists(temp_db_file):
            os.remove(temp_db_file)
        os.system(f"sqlite3 {temp_db_file} < {backup_sql_file}")
        
        conn = sqlite3.connect(temp_db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        self.stdout.write("Importing Tags...")
        cursor.execute("SELECT * FROM tag")
        for row in cursor.fetchall():
            Tag.objects.update_or_create(id=row['id'], defaults={'name': row['name']})

        self.stdout.write("Importing Repertoire Pieces...")
        cursor.execute("SELECT * FROM repertoire_piece")
        for row in cursor.fetchall():
            RepertoirePiece.objects.update_or_create(
                id=row['id'],
                defaults={
                    'nombre': row['nombre'],
                    'compositor': row['compositor'],
                    'tonalidad': row['tonalidad'],
                    'comentarios': row['comentarios'],
                    'letra_original': row['letra_original'],
                    'letra_traducida': row['letra_traducida'],
                    'video_url': row['video_url'],
                }
            )

        self.stdout.write("Importing Repertoire-Tag relations...")
        cursor.execute("SELECT * FROM repertoire_tags")
        for row in cursor.fetchall():
            try:
                piece = RepertoirePiece.objects.get(id=row['repertoire_piece_id'])
                tag = Tag.objects.get(id=row['tag_id'])
                piece.tags.add(tag)
            except (RepertoirePiece.DoesNotExist, Tag.DoesNotExist):
                self.stdout.write(self.style.WARNING(f"Skipping relation for missing piece or tag."))

        self.stdout.write("Importing Programs...")
        cursor.execute("SELECT * FROM program")
        for row in cursor.fetchall():
            Program.objects.update_or_create(id=row['id'], defaults={'name': row['name']})
        
        self.stdout.write("Importing Quotes...")
        cursor.execute("SELECT * FROM quote")
        for row in cursor.fetchall():
            def parse_date(date_str):
                return datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
            
            def parse_time(time_str):
                return datetime.strptime(time_str, '%H:%M:%S').time() if time_str else None

            program_instance = None
            if row['program_id']:
                try:
                    program_instance = Program.objects.get(id=row['program_id'])
                except Program.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Program with id {row['program_id']} not found for quote."))

            def parse_datetime(dt_str):
                if not dt_str: return None
                # Naive datetime from old DB
                naive_dt = datetime.strptime(dt_str.split('.')[0], '%Y-%m-%d %H:%M:%S')
                # Make it timezone-aware for Django
                return make_aware(naive_dt)

            Quote.objects.update_or_create(
                id=row['id'],
                defaults={
                    'tracking_code': row['tracking_code'],
                    'event_date': parse_date(row['event_date']),
                    'event_time': parse_time(row['event_time']),
                    'event_type': row['event_type'],
                    'location_type': row['location_type'],
                    'location_details': row['location_details'],
                    'is_exterior': bool(row['is_exterior']),
                    'num_voices': row['num_voices'],
                    'num_musicians': row['num_musicians'],
                    'dress_code': row['dress_code'],
                    'client_name': row['client_name'],
                    'client_phone': row['client_phone'],
                    'client_email': row['client_email'],
                    'contact_method': row['contact_method'],
                    'comments': row['comments'],
                    'total_cost': row['total_cost'],
                    'created_at': parse_datetime(row['created_at']),
                    'program': program_instance,
                }
            )
            
        self.stdout.write("Importing Program Items...")
        cursor.execute("SELECT * FROM program_item")
        for row in cursor.fetchall():
            ProgramItem.objects.update_or_create(
                id=row['id'],
                defaults={
                    'program_id': row['program_id'],
                    'repertoire_piece_id': row['repertoire_piece_id'],
                    'position': row['position'],
                }
            )
            
        conn.close()
        os.remove(temp_db_file)
        self.stdout.write(self.style.SUCCESS("Successfully imported all data from backup."))
# main/management/commands/import_repertory.py

import sqlite3
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import RepertoirePiece

class Command(BaseCommand):
    help = 'Loads repertoire data from the old repertory_dump.sql file.'

    def handle(self, *args, **options):
        sql_file_path = os.path.join(settings.BASE_DIR, 'repertory_dump.sql')

        if not os.path.exists(sql_file_path):
            self.stdout.write(self.style.ERROR(f"SQL dump file not found at {sql_file_path}"))
            return

        self.stdout.write("Creating temporary in-memory database...")
        # Use an in-memory SQLite database to load the dump
        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        cursor = conn.cursor()

        self.stdout.write(f"Executing SQL script from {sql_file_path}...")
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            cursor.executescript(sql_script)

        self.stdout.write("Reading data from temporary database and importing into Django...")
        
        # Query the data we just loaded
        cursor.execute("SELECT * FROM repertoire_piece")
        rows = cursor.fetchall()
        
        count = 0
        for row in rows:
            # --- Data Cleaning ---
            # Convert string 'None' or invalid URLs to Python None
            letra_traducida = row['letra_traducida'] if row['letra_traducida'] and row['letra_traducida'] != 'None' else None
            video_url = row['video_url'] if row['video_url'] and 'embed' in row['video_url'] else None
            compositor = row['compositor'] if row['compositor'] and row['compositor'] != 'None' else None

            # Use update_or_create to avoid duplicates and allow re-running the script
            piece, created = RepertoirePiece.objects.update_or_create(
                id=row['id'],
                defaults={
                    'nombre': row['nombre'],
                    'compositor': compositor,
                    'tonalidad': row['tonalidad'],
                    'comentarios': row['comentarios'],
                    'letra_original': row['letra_original'],
                    'letra_traducida': letra_traducida,
                    'video_url': video_url,
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(rows)} records. ({count} new records created)"))

        # Clean up the connection
        conn.close()
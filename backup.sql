BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "program" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(150),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "program_item" (
	"program_id"	INTEGER NOT NULL,
	"repertoire_piece_id"	INTEGER NOT NULL,
	"position"	INTEGER NOT NULL,
	"id"	INTEGER NOT NULL,
	CONSTRAINT "pk_program_item" PRIMARY KEY("id"),
	FOREIGN KEY("program_id") REFERENCES "program"("id"),
	FOREIGN KEY("repertoire_piece_id") REFERENCES "repertoire_piece"("id")
);
CREATE TABLE IF NOT EXISTS "quote" (
	"id"	INTEGER NOT NULL,
	"tracking_code"	VARCHAR(12) NOT NULL,
	"event_date"	DATE,
	"event_time"	TIME,
	"event_type"	VARCHAR(100),
	"location_type"	VARCHAR(100),
	"location_details"	VARCHAR(300),
	"is_exterior"	BOOLEAN,
	"num_voices"	INTEGER,
	"num_musicians"	INTEGER,
	"dress_code"	VARCHAR(50),
	"client_name"	VARCHAR(150),
	"client_phone"	VARCHAR(50),
	"client_email"	VARCHAR(150),
	"contact_method"	VARCHAR(50),
	"comments"	TEXT,
	"cost_musicians_base"	FLOAT,
	"cost_weekend_fee"	FLOAT,
	"cost_distance_fee"	FLOAT,
	"cost_gala_fee"	FLOAT,
	"cost_primetime_fee"	FLOAT,
	"cost_manager_base"	FLOAT,
	"cost_manager_per_person"	FLOAT,
	"cost_manager_exterior"	FLOAT,
	"cost_manager_boda"	FLOAT,
	"cost_car_fee"	FLOAT,
	"total_musician_payout_rounded"	FLOAT,
	"total_cost"	FLOAT,
	"program_id"	INTEGER,
	"created_at"	DATETIME DEFAULT (CURRENT_TIMESTAMP),
	"updated_at"	DATETIME,
	PRIMARY KEY("id"),
	UNIQUE("program_id"),
	FOREIGN KEY("program_id") REFERENCES "program"("id")
);
CREATE TABLE IF NOT EXISTS "repertoire_piece" (
	"id"	INTEGER NOT NULL,
	"nombre"	VARCHAR(200) NOT NULL,
	"compositor"	VARCHAR(150),
	"tonalidad"	VARCHAR(50),
	"comentarios"	TEXT,
	"letra_original"	TEXT,
	"letra_traducida"	TEXT,
	"video_url"	VARCHAR(255),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "repertoire_tags" (
	"repertoire_piece_id"	INTEGER NOT NULL,
	"tag_id"	INTEGER NOT NULL,
	PRIMARY KEY("repertoire_piece_id","tag_id"),
	FOREIGN KEY("repertoire_piece_id") REFERENCES "repertoire_piece"("id"),
	FOREIGN KEY("tag_id") REFERENCES "tag"("id")
);
CREATE TABLE IF NOT EXISTS "tag" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("name")
);
CREATE TABLE IF NOT EXISTS "visit" (
	"id"	INTEGER NOT NULL,
	"session_id"	VARCHAR(36) NOT NULL,
	"timestamp"	DATETIME,
	"ip_address"	VARCHAR(45),
	"user_agent"	VARCHAR(255),
	"method"	VARCHAR(10),
	"path"	VARCHAR(255),
	"referrer"	VARCHAR(255),
	"status_code"	INTEGER,
	PRIMARY KEY("id")
);
INSERT INTO "alembic_version" VALUES ('f4a59f9b88b9');
INSERT INTO "program" VALUES (1,'Programa de Evento');
INSERT INTO "program_item" VALUES (1,1,0,1);
INSERT INTO "program_item" VALUES (1,2,1,2);
INSERT INTO "quote" VALUES (1,'SZdT7Hfk','2025-06-24',NULL,'Bodas',NULL,'',0,8,6,NULL,'Pedro','3313029450','',NULL,'',0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,27300.0,30200.0,1,'2025-06-17 23:05:36','2025-06-18 07:15:03');
INSERT INTO "repertoire_piece" VALUES (1,'Simon',NULL,'x','asdf','asdf','asdf','');
INSERT INTO "repertoire_piece" VALUES (2,'caraxas','ANONimo','','','','','');
INSERT INTO "repertoire_piece" VALUES (3,'no importa',NULL,'','(venv) pet@discipline:~/dev/musicaparamisas.com$ flask db upgrade
 * Tip: There are .env files present. Install python-dotenv to use them.
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 71109d47be04 -> f4a59f9b88b9, Remove uniqueness constraints on repertoire and program items
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'', ''id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
','(venv) pet@discipline:~/dev/musicaparamisas.com$ flask db upgrade
 * Tip: There are .env files present. Install python-dotenv to use them.
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 71109d47be04 -> f4a59f9b88b9, Remove uniqueness constraints on repertoire and program items
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'', ''id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
','(venv) pet@discipline:~/dev/musicaparamisas.com$ flask db upgrade
 * Tip: There are .env files present. Install python-dotenv to use them.
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 71109d47be04 -> f4a59f9b88b9, Remove uniqueness constraints on repertoire and program items
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
/usr/lib/python3.11/contextlib.py:144: SAWarning: Table ''_alembic_tmp_program_item'' specifies columns ''program_id'', ''repertoire_piece_id'', ''id'' as primary_key=True, not matching locally specified columns ''id''; setting the current primary key columns to ''id''. This warning may become an exception in a future release
  next(self.gen)
','');
INSERT INTO "repertoire_tags" VALUES (1,1);
INSERT INTO "repertoire_tags" VALUES (1,2);
INSERT INTO "repertoire_tags" VALUES (1,3);
INSERT INTO "repertoire_tags" VALUES (2,3);
INSERT INTO "tag" VALUES (1,'Comunión');
INSERT INTO "tag" VALUES (2,'Entrada');
INSERT INTO "tag" VALUES (3,'Salida');
INSERT INTO "visit" VALUES (1,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:03:56.891089','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (2,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:05:02.048367','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin',NULL,308);
INSERT INTO "visit" VALUES (3,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:05:02.095884','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin/',NULL,302);
INSERT INTO "visit" VALUES (4,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:05:02.134526','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin/login',NULL,200);
INSERT INTO "visit" VALUES (5,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:05:02.220290','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (6,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:06:10.682993','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (7,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:07:42.955192','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (8,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:08.880013','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (9,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:37.335237','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (10,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:54.781875','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin',NULL,308);
INSERT INTO "visit" VALUES (11,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:54.818900','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin/',NULL,302);
INSERT INTO "visit" VALUES (12,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:54.849839','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/admin/login',NULL,200);
INSERT INTO "visit" VALUES (13,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:54.930948','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (14,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:57.492345','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','POST','/admin/login','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',200);
INSERT INTO "visit" VALUES (15,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:08:57.576600','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (16,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:30:34.645736','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (17,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:30:43.040972','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (18,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:30:51.841429','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (19,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:30:56.520266','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,NULL);
INSERT INTO "visit" VALUES (20,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:33:54.847315','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (21,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:15.051947','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (22,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:16.232180','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/servicios','http://127.0.0.1:5000/',NULL);
INSERT INTO "visit" VALUES (23,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:47.171143','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/videos','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (24,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:48.048991','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/servicios','http://127.0.0.1:5000/videos',NULL);
INSERT INTO "visit" VALUES (25,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:50.530251','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/videos',200);
INSERT INTO "visit" VALUES (26,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:34:51.826501','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/contacto','http://127.0.0.1:5000/cotizador',NULL);
INSERT INTO "visit" VALUES (27,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:35:05.951066','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/contacto','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (28,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:35:08.041272','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/acerca','http://127.0.0.1:5000/contacto',NULL);
INSERT INTO "visit" VALUES (29,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:35:15.992056','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/acerca','http://127.0.0.1:5000/contacto',200);
INSERT INTO "visit" VALUES (30,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:35:19.387691','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/acerca','http://127.0.0.1:5000/acerca',200);
INSERT INTO "visit" VALUES (31,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:35:20.114141','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',NULL);
INSERT INTO "visit" VALUES (32,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:36:39.929236','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',NULL);
INSERT INTO "visit" VALUES (33,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:36:41.153710','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',NULL);
INSERT INTO "visit" VALUES (34,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:36:47.422371','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',NULL);
INSERT INTO "visit" VALUES (35,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:36:52.137026','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',NULL);
INSERT INTO "visit" VALUES (36,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:07.252440','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/acerca',200);
INSERT INTO "visit" VALUES (37,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:09.035330','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/politica',200);
INSERT INTO "visit" VALUES (38,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:10.358638','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/videos','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (39,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:11.022738','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/videos',200);
INSERT INTO "visit" VALUES (40,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:11.917850','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/contacto','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (41,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:37:12.875746','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/contacto',200);
INSERT INTO "visit" VALUES (42,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:07.611576','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/contacto',200);
INSERT INTO "visit" VALUES (43,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:09.013236','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (44,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:10.017199','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/contacto','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (45,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:11.673431','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/politica','http://127.0.0.1:5000/contacto',200);
INSERT INTO "visit" VALUES (46,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:12.422612','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/politica',200);
INSERT INTO "visit" VALUES (47,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:12.857232','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/videos','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (48,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:38:13.271224','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/servicios','http://127.0.0.1:5000/videos',200);
INSERT INTO "visit" VALUES (49,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:43:01.672540','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/amin',NULL,404);
INSERT INTO "visit" VALUES (50,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:43:04.831322','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (51,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:43:12.674686','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (52,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:43:20.203246','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (53,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:45:30.109127','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (54,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:46:29.120151','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (55,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:46:36.262279','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (56,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:09.814685','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (57,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:16.431453','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (58,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:27.847591','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (59,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:34.363110','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (60,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:38.285284','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/tags',404);
INSERT INTO "visit" VALUES (61,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 22:59:52.481570','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (62,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:05:11.395831','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (63,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:05:13.190641','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (64,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:05:36.114918','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','POST','/cotizador','http://127.0.0.1:5000/cotizador',302);
INSERT INTO "visit" VALUES (65,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:05:36.169345','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizacion/SZdT7Hfk','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (66,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:06:07.743399','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/quotes',404);
INSERT INTO "visit" VALUES (67,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:06:30.619202','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (68,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:06:46.724763','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/quotes',404);
INSERT INTO "visit" VALUES (69,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:08:26.899671','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/quotes',404);
INSERT INTO "visit" VALUES (70,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:10:12.107040','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
INSERT INTO "visit" VALUES (71,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:10:15.768019','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (72,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:11:48.083402','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (73,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:11:54.055964','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (74,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:12:26.817279','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (75,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:12:32.368049','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (76,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:14:53.945088','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
INSERT INTO "visit" VALUES (77,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:14:56.836101','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (78,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:16:24.107727','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/cotizacion/SZdT7Hfk',200);
INSERT INTO "visit" VALUES (79,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:16:28.274065','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/servicios','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (80,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:16:29.288844','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/videos','http://127.0.0.1:5000/servicios',200);
INSERT INTO "visit" VALUES (81,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:16:30.199767','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/videos',200);
INSERT INTO "visit" VALUES (82,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:16:31.223391','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/videos','http://127.0.0.1:5000/cotizador',200);
INSERT INTO "visit" VALUES (83,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:17:18.392511','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/','http://127.0.0.1:5000/videos',200);
INSERT INTO "visit" VALUES (84,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:18:19.578982','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
INSERT INTO "visit" VALUES (85,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:19:23.107283','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2Frepertoire',404);
INSERT INTO "visit" VALUES (86,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:19:29.402537','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (87,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:19:33.042325','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (88,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:21:25.021596','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (89,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:21:25.869407','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (90,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:22:03.512562','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (91,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-17 23:22:27.964146','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
INSERT INTO "visit" VALUES (92,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:11:15.762634','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (93,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:12:07.287837','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (94,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:12:33.732591','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (95,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:13:21.731536','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (96,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:13:25.218079','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (97,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:13:37.937077','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (98,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:13:47.304453','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (99,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:29.806243','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (100,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:31.935927','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2Frepertoire',404);
INSERT INTO "visit" VALUES (101,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:32.611715','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2Fquotes',404);
INSERT INTO "visit" VALUES (102,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:38.513586','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2Frepertoire',404);
INSERT INTO "visit" VALUES (103,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:41.477422','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (104,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:14:49.935654','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (105,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:15:29.085945','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (106,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:15:46.321213','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (107,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:15:58.606413','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (108,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:16:23.256924','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (109,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:16:49.458514','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (110,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:16:54.732530','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (111,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:17:05.330036','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (112,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:17:29.130050','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (113,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:17:39.973647','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (114,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:18:39.362615','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (115,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:19:29.167156','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (116,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:19:46.128860','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (117,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:20:02.941915','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/',NULL,200);
INSERT INTO "visit" VALUES (118,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:20:10.368143','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/servicios','http://127.0.0.1:5000/',200);
INSERT INTO "visit" VALUES (119,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:39:40.288082','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/servicios',200);
INSERT INTO "visit" VALUES (120,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:39:47.277967','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login?next=%2Fadmin%2F',404);
INSERT INTO "visit" VALUES (121,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:39:53.411001','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (122,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:40:25.138259','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (123,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:47:39.171593','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
INSERT INTO "visit" VALUES (124,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:47:48.111952','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (125,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:48:07.508520','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (126,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:48:16.966404','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (127,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:51:55.687655','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/repertoire',404);
INSERT INTO "visit" VALUES (128,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:52:34.913504','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (129,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 06:57:49.303669','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/cotizador','http://127.0.0.1:5000/admin/quotes',200);
INSERT INTO "visit" VALUES (130,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:15:03.272145','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/quotes',404);
INSERT INTO "visit" VALUES (131,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:17:34.008547','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (132,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:17:40.909709','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (133,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:20:16.885425','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (134,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:20:54.649096','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/',404);
INSERT INTO "visit" VALUES (135,'7b29a72d-b1cc-4e99-a9f0-94811b3401c3','2025-06-18 07:21:12.482303','127.0.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0','GET','/favicon.ico','http://127.0.0.1:5000/admin/login',404);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_quote_tracking_code" ON "quote" (
	"tracking_code"
);
CREATE INDEX IF NOT EXISTS "ix_visit_session_id" ON "visit" (
	"session_id"
);
CREATE INDEX IF NOT EXISTS "ix_visit_timestamp" ON "visit" (
	"timestamp"
);
COMMIT;

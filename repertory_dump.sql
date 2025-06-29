----
-- phpLiteAdmin database dump (https://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.9-dev
-- Exported: 4:53am on June 29, 2025 (UTC)
-- database file: /var/www/musicaparamisas.com/instance/site.db
----
BEGIN TRANSACTION;

----
-- Table structure for repertoire_piece
----
CREATE TABLE "repertoire_piece" (
	id INTEGER NOT NULL, 
	nombre VARCHAR(200) NOT NULL, 
	compositor VARCHAR(150), 
	tonalidad VARCHAR(50), 
	comentarios TEXT, 
	letra_original TEXT, 
	letra_traducida TEXT, 
	video_url VARCHAR(255), 
	PRIMARY KEY (id)
);

----
-- Data dump for repertoire_piece, a total of 80 rows
----
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('1','Hacia Ti Morada Santa','Kiko Argüello','Am','Canto de entrada popular del Camino Neocatecumenal.','Hacia ti, morada santa,\nhacia ti, tierra del Salvador,\nperegrinos, caminantes,\nvamos hacia ti.',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('2','Con te partirò (Por ti volaré)','Francesco Sartori','G Major','Popularizado por Andrea Bocelli. Conocido como "Time to Say Goodbye".','Quando sono solo\nsogno all''orizzonte\ne mancan le parole...','Cuando estoy solo\nsueño en el horizonte\ny faltan las palabras...',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('3','Ángeles de Dios (Ángeles volando)','Cristobal Fones','G Major','Canto popular y alegre.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('4','Gloria (Misa Rítmica)','Alejandro Mejía','G Major','Parte del ordinario de la Misa Rítmica.','Gloria in excelsis Deo\net in terra pax hominibus bonae voluntatis.\nLaudamus te, benedicimus te,\nadoramus te, glorificamus te,\ngratias agimus tibi propter magnam gloriam tuam,\nDomine Deus, Rex caelestis, Deus Pater omnipotens.\nDomine Fili unigenite, Iesu Christe,\nDomine Deus, Agnus Dei, Filius Patris,\nqui tollis peccata mundi, miserere nobis;\nqui tollis peccata mundi, suscipe deprecationem nostram.\nQui sedes ad dexteram Patris, miserere nobis.\nQuoniam tu solus Sanctus, tu solus Dominus,\ntu solus Altissimus, Iesu Christe,\ncum Sancto Spiritu: in gloria Dei Patris. Amen.','Gloria a Dios en el cielo,\ny en la tierra paz a los hombres que ama el Señor.\nPor tu inmensa gloria te alabamos, te bendecimos,\nte adoramos, te glorificamos,\nte damos gracias, Señor Dios, Rey celestial,\nDios Padre todopoderoso.\nSeñor, Hijo único, Jesucristo,\nSeñor Dios, Cordero de Dios, Hijo del Padre;\ntú que quitas el pecado del mundo, ten piedad de nosotros;\ntú que quitas el pecado del mundo, atiende nuestra súplica.\nTú que estás sentado a la derecha del Padre, ten piedad de nosotros.\nPorque solo tú eres Santo, solo tú Señor,\nsolo tú Altísimo, Jesucristo,\ncon el Espíritu Santo en la gloria de Dios Padre. Amén.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('5','Marcha Nupcial','Felix Mendelssohn','C Major','De "El sueño de una noche de verano". Recesional de boda clásico.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('6','Canon en Re','Johann Pachelbel','D Major','Procesional de boda muy popular.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('7','Bendito, Bendito','Tradicional','G Major','Canto popular de adoración.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('8','Altísimo Señor','Tradicional','D Major','Himno Eucarístico tradicional.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('9','Kyrie (Misa Stella Matutina)','Vito Carnevali','F Major','Parte del ordinario de la misa.','Kyrie, eleison.\nChriste, eleison.\nKyrie, eleison.','Señor, ten piedad.\nCristo, ten piedad.\nSeñor, ten piedad.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('10','Kyrie (Misa en honor a Santa Lucía)','Luigi Bottazzo','C Major','De la "Misa Facile".','Kyrie, eleison.\nChriste, eleison.\nKyrie, eleison.','Señor, ten piedad.\nCristo, ten piedad.\nSeñor, ten piedad.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('11','Panis Angelicus','César Franck','G Major','Canto Eucarístico para solista. Muy solemne.','Panis angelicus
fit panis hominum;
Dat panis coelicus
figuris terminum.
O res mirabilis!
Manducat Dominum
Pauper, servus et humilis.

Te trina Deitas
unaque poscimus:
Sic nos tu visita,
sicut te colimus;
Per tuas semitas
duc nos quo tendimus,
Ad lucem quam inhabitas. Amen.','El pan de los ángeles
se convierte en pan de los hombres;
El pan del cielo
pone fin a las prefiguraciones.
¡Oh, cosa admirable!
Come al Señor
el pobre, el siervo y el humilde.

A ti, Trinidad y Deidad
única, te lo pedimos:
Visítanos así,
como te damos culto;
Por tus caminos
guíanos a donde anhelamos,
a la luz en la que habitas. Amén.','https://www.youtube.com/embed/m9wtrrS1s00');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('12','Ave Maria','Franz Schubert','Bb Major','Una de las versiones más famosas del Ave María.','Ave Maria, gratia plena,
Dominus tecum.
Benedicta tu in mulieribus,
et benedictus fructus ventris tui, Iesus.
Sancta Maria, Mater Dei,
ora pro nobis peccatoribus,
nunc et in hora mortis nostrae. Amen.','Dios te salve, María, llena eres de gracia,
el Señor es contigo.
Bendita tú eres entre todas las mujeres,
y bendito es el fruto de tu vientre, Jesús.
Santa María, Madre de Dios,
ruega por nosotros, pecadores,
ahora y en la hora de nuestra muerte. Amén.','https://www.youtube.com/embed/NYC7IMWMbW0');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('13','Ave Verum Corpus','W.A. Mozart','D Major','Motete Eucarístico de gran belleza. K. 618.','Ave verum corpus, natum
de Maria Virgine,
Vere passum, immolatum
in cruce pro homine,
Cuius latus perforatum
unda fluxit et sanguine,
Esto nobis praegustatum
in mortis examine.
O Iesu dulcis, O Iesu pie,
O Iesu, fili Mariae.','Salve, cuerpo verdadero, nacido
de la Virgen María,
que verdaderamente padeciste, inmolado
en la cruz por el hombre,
de cuyo costado perforado
fluyó agua y sangre.
Sé para nosotros un anticipo
en el trance de la muerte.
Oh, dulce Jesús, oh, piadoso Jesús,
oh, Jesús, hijo de María.','https://www.youtube.com/embed/VlSDRNP545A');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('14','Largo (Ombra mai fu)','G.F. Handel','F Major','Aria de la ópera "Xerxes". Muy solemne y usada en ceremonias.','Ombra mai fu\ndi vegetabile,\ncara ed amabile,\nsoave più.','Nunca fue la sombra\nde una planta,\nmás querida y amable,\no más dulce.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('15','Alleluia (de Exsultate, jubilate)','W.A. Mozart','F Major','Motete para soprano. K. 165. Canto de aclamación muy virtuosístico.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('16','Pie Jesu (del Requiem)','Gabriel Fauré','Bb Major','Solemne y emotivo, para soprano.','Pie Jesu Domine,
Dona eis requiem.
Pie Jesu Domine,
Dona eis requiem sempiternam.','Piadoso Señor Jesús,
dales el descanso.
Piadoso Señor Jesús,
dales el descanso eterno.','https://www.youtube.com/embed/9um9cv_zrLg');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('17','Ave Maria','Bach / Gounod','F Major','Melodía de Gounod sobre el Preludio No. 1 en Do Mayor de J.S. Bach.','Ave Maria, gratia plena,
Dominus tecum.
Benedicta tu in mulieribus,
et benedictus fructus ventris tui, Iesus.
Sancta Maria, Sancta Maria, Maria,
ora pro nobis,
nobis peccatoribus,
nunc et in hora, in hora mortis nostrae.
Amen. Amen.','Dios te salve, María, llena eres de gracia,
el Señor es contigo.
Bendita tú eres entre todas las mujeres,
y bendito es el fruto de tu vientre, Jesús.
Santa María, Santa María, María,
ruega por nosotros,
nosotros pecadores,
ahora y en la hora, en la hora de nuestra muerte.
Amén. Amén.','https://www.youtube.com/embed/qLoHTnivDRI');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('18','Gloria (Misa en honor a Santa Lucía)','Luigi Bottazzo','C Major','De la "Misa Facile".','Gloria in excelsis Deo\net in terra pax hominibus bonae voluntatis.\nLaudamus te, benedicimus te,\nadoramus te, glorificamus te,\ngratias agimus tibi propter magnam gloriam tuam,\nDomine Deus, Rex caelestis, Deus Pater omnipotens.\nDomine Fili unigenite, Iesu Christe,\nDomine Deus, Agnus Dei, Filius Patris,\nqui tollis peccata mundi, miserere nobis;\nqui tollis peccata mundi, suscipe deprecationem nostram.\nQui sedes ad dexteram Patris, miserere nobis.\nQuoniam tu solus Sanctus, tu solus Dominus,\ntu solus Altissimus, Iesu Christe,\ncum Sancto Spiritu: in gloria Dei Patris. Amen.','Gloria a Dios en el cielo,\ny en la tierra paz a los hombres que ama el Señor.\nPor tu inmensa gloria te alabamos, te bendecimos,\nte adoramos, te glorificamos,\nte damos gracias, Señor Dios, Rey celestial,\nDios Padre todopoderoso.\nSeñor, Hijo único, Jesucristo,\nSeñor Dios, Cordero de Dios, Hijo del Padre;\ntú que quitas el pecado del mundo, ten piedad de nosotros;\ntú que quitas el pecado del mundo, atiende nuestra súplica.\nTú que estás sentado a la derecha del Padre, ten piedad de nosotros.\nPorque solo tú eres Santo, solo tú Señor,\nsolo tú Altísimo, Jesucristo,\ncon el Espíritu Santo en la gloria de Dios Padre. Amén.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('19','Kyrie (Misa de Coronación K. 317)','W.A. Mozart','C Major','Parte del ordinario de una de las misas más famosas de Mozart.','Kyrie, eleison.\nChriste, eleison.\nKyrie, eleison.','Señor, ten piedad.\nCristo, ten piedad.\nSeñor, ten piedad.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('20','Gloria (Misa de Coronación K. 317)','W.A. Mozart','C Major','Parte del ordinario. Majestuoso.','Gloria in excelsis Deo\net in terra pax hominibus bonae voluntatis.\nLaudamus te, benedicimus te,\nadoramus te, glorificamus te,\ngratias agimus tibi propter magnam gloriam tuam,\nDomine Deus, Rex caelestis, Deus Pater omnipotens.\nDomine Fili unigenite, Iesu Christe,\nDomine Deus, Agnus Dei, Filius Patris,\nqui tollis peccata mundi, miserere nobis;\nqui tollis peccata mundi, suscipe deprecationem nostram.\nQui sedes ad dexteram Patris, miserere nobis.\nQuoniam tu solus Sanctus, tu solus Dominus,\ntu solus Altissimus, Iesu Christe,\ncum Sancto Spiritu: in gloria Dei Patris. Amen.','Gloria a Dios en el cielo,\ny en la tierra paz a los hombres que ama el Señor.\nPor tu inmensa gloria te alabamos, te bendecimos,\nte adoramos, te glorificamos,\nte damos gracias, Señor Dios, Rey celestial,\nDios Padre todopoderoso.\nSeñor, Hijo único, Jesucristo,\nSeñor Dios, Cordero de Dios, Hijo del Padre;\ntú que quitas el pecado del mundo, ten piedad de nosotros;\ntú que quitas el pecado del mundo, atiende nuestra súplica.\nTú que estás sentado a la derecha del Padre, ten piedad de nosotros.\nPorque solo tú eres Santo, solo tú Señor,\nsolo tú Altísimo, Jesucristo,\ncon el Espíritu Santo en la gloria de Dios Padre. Amén.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('21','Sanctus (Misa de Coronación K. 317)','W.A. Mozart','C Major','Parte del ordinario. Incluye el Benedictus.','Sanctus, Sanctus, Sanctus,\nDominus Deus Sabaoth.\nPleni sunt caeli et terra gloria tua.\nHosanna in excelsis.\nBenedictus qui venit in nomine Domini.\nHosanna in excelsis.','Santo, Santo, Santo es el Señor,\nDios del Universo.\nLlenos están el cielo y la tierra de tu gloria.\nHosanna en el cielo.\nBendito el que viene en nombre del Señor.\nHosanna en el cielo.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('22','Agnus Dei (Misa de Coronación K. 317)','W.A. Mozart','F Major','Parte final del ordinario, para soprano solista y coro.','Agnus Dei, qui tollis peccata mundi, miserere nobis.\nAgnus Dei, qui tollis peccata mundi, miserere nobis.\nAgnus Dei, qui tollis peccata mundi, dona nobis pacem.','Cordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros.\nCordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros.\nCordero de Dios, que quitas el pecado del mundo, danos la paz.','');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('23','Cerca de Ti, Señor','Lowell Mason','F Major','Himno popular. "Nearer, My God, to Thee".','Cerca de Ti, Señor, quiero morar;
Tu grande, tierno amor quiero gozar.
Llena mi pobre ser, limpia mi corazón,
Hazme tu rostro ver en comunión.

Pasos inciertos doy, el sol se va;
Mas si contigo estoy, no temo ya.
Himnos de gratitud, ferviente cantaré,
Y fiel a Ti, Jesús, siempre seré.

Día feliz veré creyendo en Ti,
En que yo habitaré, cerca de Ti.
Mi voz alabará tu dulce nombre allí,
Y mi alma gozará cerca de Ti.','None','http://www.musicaparamisas.com');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('24','Pueblo de Reyes','Lucien Deiss','G Major','Himno litúrgico.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('25','Yo Soy el Pan de Vida','Suzanne Toolan','F Major','Canto de comunión muy conocido.','Yo soy el pan de vida,
el que viene a mí no tendrá hambre,
el que cree en mí no tendrá sed.
Nadie viene a mí si mi Padre no lo atrae.

Y yo lo resucitaré,
y yo lo resucitaré,
y yo lo resucitaré
en el día final.

El pan que yo daré
es mi cuerpo, vida del mundo.
El que coma de mi carne
tendrá vida eterna, tendrá vida eterna.

Si no coméis la carne
del Hijo del Hombre
y no bebéis su sangre,
no tendréis vida en vosotros.',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('26','Resucitó','Kiko Argüello','Am','Canto de Pascua por excelencia.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('27','Himno a la Alegría (Oda a la Alegría)','Ludwig van Beethoven','D Major','De la 9ª Sinfonía. Usado como canto de salida o procesional.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('28','Pompa y Circunstancia No. 1',NULL,'D Major','Marcha procesional, muy usada en graduaciones y bodas.','None','None','None');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('29','Gloria','Cesáreo Gabaráin','G Major','Versión comunitaria y sencilla.','Gloria in excelsis Deo\net in terra pax hominibus bonae voluntatis.\nLaudamus te, benedicimus te,\nadoramus te, glorificamus te,\ngratias agimus tibi propter magnam gloriam tuam,\nDomine Deus, Rex caelestis, Deus Pater omnipotens.\nDomine Fili unigenite, Iesu Christe,\nDomine Deus, Agnus Dei, Filius Patris,\nqui tollis peccata mundi, miserere nobis;\nqui tollis peccata mundi, suscipe deprecationem nostram.\nQui sedes ad dexteram Patris, miserere nobis.\nQuoniam tu solus Sanctus, tu solus Dominus,\ntu solus Altissimus, Iesu Christe,\ncum Sancto Spiritu: in gloria Dei Patris. Amen.','Gloria a Dios en el cielo,\ny en la tierra paz a los hombres que ama el Señor.\nPor tu inmensa gloria te alabamos, te bendecimos,\nte adoramos, te glorificamos,\nte damos gracias, Señor Dios, Rey celestial,\nDios Padre todopoderoso.\nSeñor, Hijo único, Jesucristo,\nSeñor Dios, Cordero de Dios, Hijo del Padre;\ntú que quitas el pecado del mundo, ten piedad de nosotros;\ntú que quitas el pecado del mundo, atiende nuestra súplica.\nTú que estás sentado a la derecha del Padre, ten piedad de nosotros.\nPorque solo tú eres Santo, solo tú Señor,\nsolo tú Altísimo, Jesucristo,\ncon el Espíritu Santo en la gloria de Dios Padre. Amén.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('30','Aleluya (Honor y Gloria)','Cesáreo Gabaráin','D Major','Aclamación popular antes del Evangelio.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('31','Señor, ten piedad (Misa Melódica)','Alejandro Mejía','Em','Parte del ordinario.',NULL,NULL,'https://www.youtube.com/embed/YxbhXKMy2zs');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('32','Aleluya (El Mesías)','G.F. Handel','D Major','El coro más famoso del oratorio "El Mesías".','Alleluia, Alleluia, Alleluia, Alleluia!
Alleluia, Alleluia, Alleluia, Alleluia!

For the Lord God Omnipotent reigneth.
Alleluia, Alleluia, Alleluia, Alleluia!

The kingdom of this world
Is become the kingdom of our Lord,
And of His Christ, and of His Christ;
And He shall reign for ever and ever.
King of Kings, and Lord of Lords,
And He shall reign for ever and ever,
Alleluia, Alleluia!','¡Aleluya, Aleluya, Aleluya, Aleluya!
¡Aleluya, Aleluya, Aleluya, Aleluya!

Porque el Señor nuestro Dios Todopoderoso reina.
¡Aleluya, Aleluya, Aleluya, Aleluya!

El reino de este mundo
se ha convertido en el reino de nuestro Señor,
y de Su Cristo, y de Su Cristo;
Y Él reinará por los siglos de los siglos.
Rey de Reyes y Señor de Señores,
y Él reinará por los los siglos de los siglos,
¡Aleluya, Aleluya!','https://www.youtube.com/embed/Xh0i7n4H4e0');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('33','Vino y Pan','Carlos Camacho','D Major','Canto de ofertorio popular.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('34','Pescador de Hombres (Tú has venido a la orilla)','Cesáreo Gabaráin','D Major','Uno de los cantos religiosos más conocidos en español.','Tú has venido a la orilla,
no has buscado ni a sabios ni a ricos.
Tan solo quieres que yo te siga.

Señor, me has mirado a los ojos,
sonriendo has dicho mi nombre.
En la arena he dejado mi barca,
junto a ti, buscaré otro mar.

Tú sabes bien lo que tengo,
en mi barca no hay oro ni espadas,
tan solo redes y mi trabajo.',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('35','Entre Tus Manos','Ray Repp','F Major','Canto de ofertorio.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('36','Bist du bei mir','G.H. Stölzel','Eb Major','A menudo atribuido a J.S. Bach (BWV 508). Aria para bodas.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('37','Jesús, Alegría de los Hombres','J.S. Bach','G Major','Coral de la cantata BWV 147. Muy popular para bodas.','Jesu, joy of man''s desiring,
Holy wisdom, love most bright;
Drawn by Thee, our souls aspiring
Soar to uncreated light.

Word of God, our flesh that fashioned,
With the fire of life impassioned,
Striving still to truth unknown,
Soaring, dying round Thy throne.','Jesús, alegría de los hombres,
Santa sabiduría, amor brillantísimo;
Atraídas por Ti, nuestras almas aspiran
y se elevan a la luz increada.

Palabra de Dios, que formó nuestra carne,
con el fuego de la vida apasionada,
luchando aún por la verdad desconocida,
elevándose, muriendo en torno a tu trono.','https://www.youtube.com/embed/T1yxnC0lwrg');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('38','Gabriel''s Oboe','Ennio Morricone','D Major','Tema principal de la película "La Misión".',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('39','Arioso (Cantata BWV 156)','J.S. Bach','G Major','Movimiento lento y lírico, ideal para momentos de reflexión.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('40','Aria (de la Suite Orquestal No. 3)','J.S. Bach','D Major','Conocida como "Aria en la cuerda de Sol". Muy solemne. BWV 1068.',NULL,NULL,'https://www.youtube.com/embed/mD0iXgV93d0');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('41','Ave Maria','Giulio Caccini (Vavilov)','Gm','Composición moderna en estilo barroco, atribuida erróneamente a Caccini.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('42','Aleluya','Hermilio Hernández','C Major','Aclamación festiva de compositor mexicano.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('43','Hasta Mi Final','Il Divo','Db Major','Canción popular para ceremonias civiles y bodas.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('44','El Cisne (del Carnaval de los Animales)','Camille Saint-Saëns','G Major','Pieza para violonchelo y piano, muy elegante.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('45','Amazing Grace','Tradicional','G Major','Himno cristiano de origen inglés.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('46','My Way (A mi manera)','Claude François / Jacques Revaux','D Major','Popularizada por Frank Sinatra. Usada en funerales y homenajes.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('47','Ya no eres pan y vino','Jorge Luis Bohorquez','D Major','Canto de comunión.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('48','Kyrie (Misa Brevis K. 220)','W.A. Mozart','C Major','Conocida como "Spatzenmesse" (Misa de los gorriones).','Kyrie, eleison.\nChriste, eleison.\nKyrie, eleison.','Señor, ten piedad.\nCristo, ten piedad.\nSeñor, ten piedad.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('49','Lacrimosa (del Requiem K. 626)','W.A. Mozart','Dm','Una de las piezas más emotivas de la música sacra.','Lacrimosa dies illa
Qua resurget ex favilla
Judicandus homo reus.
Huic ergo parce, Deus:
Pie Jesu Domine,
Dona eis requiem. Amen.','Día de lágrimas será aquel
en que resurja de las cenizas
el hombre culpable para ser juzgado.
A él, pues, perdona, oh Dios.
Piadoso Señor Jesús,
dales el descanso. Amén.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('50','Laudate Dominum (de Vesperae solennes de confessore)','W.A. Mozart','F Major','Aria para soprano de gran belleza. K. 339.','Laudate Dominum, omnes gentes;
Laudate eum, omnes populi.
Quoniam confirmata est super nos misericordia ejus,
et veritas Domini manet in aeternum.
Gloria Patri et Filio et Spiritui Sancto.
Sicut erat in principio, et nunc et semper,
et in saecula saeculorum. Amen.','Alabad al Señor, todas las naciones;
Alabadle, todos los pueblos.
Porque se ha confirmado sobre nosotros su misericordia,
y la verdad del Señor permanece para siempre.
Gloria al Padre, y al Hijo, y al Espíritu Santo.
Como era en el principio, ahora y siempre,
y por los siglos de los siglos. Amén.','https://www.youtube.com/embed/jW01ah2P8kY');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('51','Canticorum Jubilo','G.F. Handel','C Major','Coro del oratorio "Judas Macabeo". Canto de entrada o salida festivo.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('52','Ave Maria','Astor Piazzolla','Am','Tango Nuevo. Versión moderna y sentida.','Ave Maria,
Mater Dei,
Iesu, Christi,
Sancta Maria,
ora pro nobis.

Ave Maria,
gratia plena,
Dominus tecum,
Benedicta tu.
Sancta Maria,
ora pro nobis.','Ave María,
Madre de Dios,
de Jesucristo,
Santa María,
ruega por nosotros.

Ave María,
llena de gracia,
el Señor es contigo,
Bendita eres tú.
Santa María,
ruega por nosotros.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('53','Wachet auf, ruft uns die Stimme (Despertad, nos llama la voz)','J.S. Bach','Eb Major','Coral de la cantata BWV 140. Procesional solemne.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('54','Aleluya','Leonard Cohen','C Major','Canción popular con adaptaciones para uso litúrgico.','Hallelujah, Hallelujah
Hallelujah, Hallelujah

Well I''ve heard there was a secret chord
That David played and it pleased the Lord
But you don''t really care for music, do you?
Well it goes like this: the fourth, the fifth
The minor fall and the major lift
The baffled king composing Hallelujah','Aleluya, Aleluya
Aleluya, Aleluya

He oído que había un acorde secreto
que David tocaba y que agradaba al Señor,
pero a ti realmente no te importa la música, ¿verdad?
Bueno, es así: la cuarta, la quinta,
la caída menor y el alza mayor,
el rey perplejo componiendo Aleluya.',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('55','Trumpet Voluntary','Jeremiah Clarke','D Major','Procesional de boda. A menudo atribuido a H. Purcell.',NULL,NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('56','Alma Bendice al Señor','Coralia (versión propia)','G Major','Canto de alabanza de estilo barroco. (Atribución del ensamble Coralia)','Alma, bendice al Señor y todo mi ser, su santo nombre.\nAlma, bendice al Señor y no olvides sus beneficios.',NULL,'https://www.youtube.com/embed/6C1l2IZDDXQ');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('57','De Aquí Hasta el Final','Sin Bandera','Db Major','Canción pop romántica, adecuada para ceremonias civiles.','No necesito alas para volar hasta el sol...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('58','Symbolum ''77 (Tú eres mi vida)','Pierangelo Sequeri','D Major','Canto litúrgico italiano muy popular. Canto de comunión o reflexión.','Tu sei la mia vita, altro io non ho...','Tú eres mi vida, no tengo otra cosa...',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('59','Eran Cien Ovejas','Félix G. Luna','D Major','Parábola del buen pastor. Canto de reflexión.','Eran cien ovejas que había en el rebaño...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('60','Yo te extrañaré','Tercer Cielo','C Major','Canción popular para servicios funerarios y conmemorativos.','Yo te extrañaré, tenlo por seguro...',NULL,'https://www.youtube.com/embed/g6P51aADa7I');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('61','Cara a Cara','Marcos Vidal','G Major','Canto cristiano de adoración y esperanza.','Solamente una palabra, solamente una oración...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('62','Vaso Nuevo','Popular','D Major','Canto tradicional de entrega y conversión.','Gracias quiero darte por amarme...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('63','Dios está aquí','Javier Gacías','G Major','Canto popular de adoración sobre la presencia de Dios.','Dios está aquí, tan cierto como el aire que respiro...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('64','Let It Be','Lennon / McCartney','C Major','Clásico de The Beatles. Su melodía se usa en ceremonias por su carácter solemne y esperanzador.','When I find myself in times of trouble, Mother Mary comes to me...','Cuando me encuentro en momentos de problemas, la Madre María viene a mí...',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('65','Jesús Amigo','Jésed','G Major','Canto de reflexión sobre la amistad con Jesús. (Atribución común)','Hoy te quiero contar, Jesús Amigo, que contigo estoy feliz...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('66','María, mírame','Jésed','D Major','Popular canto mariano, pidiendo la intercesión de María.','María, mírame, María, mírame. Si tú me miras, Él también me mirará.',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('67','Amor Eterno','Juan Gabriel','Dm','Clásico mexicano, usado en funerales y memoriales con gran carga emotiva.','Tú eres la tristeza de mis ojos que lloran en silencio por tu amor...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('68','Contigo Aprendí','Armando Manzanero','C Major','Bolero clásico. Ideal para amenizaciones y ceremonias civiles.','Contigo aprendí que existen nuevas y mejores emociones...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('69','Danny Boy','Frederic Weatherly (letrista)','Eb Major','Canción tradicional irlandesa. Usada en funerales por su tono melancólico y solemne.','Oh, Danny boy, the pipes, the pipes are calling...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('70','Esto que te doy','Popular','D Major','Canto popular de ofertorio.','Esto que te doy, es vino y pan, Señor, esto que te doy es mi trabajo...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('71','Al Paraíso','Francisco Palazón','C Major','Canto para las exequias, para la procesión final.','Al paraíso te lleven los ángeles...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('72','Junto a ti, María','Popular','G Major','Canto Mariano popular, especialmente en el mes de mayo.','Junto a ti, María, como un niño quiero estar...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('73','Padre Bueno, Dios Hermano','Popular','G Major','Canto de reflexión.','Padre bueno, Dios alegre, primavera y manantial...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('74','Festival Alleluia','James Chepponis','F Major','Aclamación festiva y enérgica, ideal para Pascua.','Alleluia, Alleluia! Give thanks to the risen Lord...','¡Aleluya, Aleluya! Dad gracias al Señor resucitado...',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('75','Ave Maria (versión contemporánea)','William Gomez','D Major','Versión contemporánea y lírica del Ave María.','Ave Maria, gratia plena...','Dios te salve, María, llena eres de gracia...',NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('76','Gloria (Misa JMJ)','Carlos Criado / Pedro Alfaro','D Major','Gloria de la misa para la Jornada Mundial de la Juventud.','Gloria a Dios en el cielo, y en la tierra paz...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('77','Sanctus (Misa JMJ)','Carlos Criado / Pedro Alfaro','D Major','Santo de la misa para la Jornada Mundial de la Juventud.','Santo, Santo, Santo es el Señor...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('78','Agnus Dei (Misa JMJ)','Carlos Criado / Pedro Alfaro','D Major','Cordero de Dios de la misa para la Jornada Mundial de la Juventud.','Cordero de Dios, que quitas el pecado del mundo...','None','Noneasdf');
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('79','Señor, ten piedad (Misa Hosanna)','Carlos Camacho','Am','Kyrie de la Misa Hosanna.','Señor, ten piedad. Cristo, ten piedad...',NULL,NULL);
INSERT INTO "repertoire_piece" ("id","nombre","compositor","tonalidad","comentarios","letra_original","letra_traducida","video_url") VALUES ('80','Alma Bendice al Señor','Popular','G Major','Canto de alabanza de estilo barroco. Video disponible en el canal.','Alma, bendice al Señor y todo mi ser, su santo nombre...',NULL,'https://www.youtube.com/embed/6C1l2IZDDXQ');
COMMIT;
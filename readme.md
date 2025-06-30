##TODO 

Hello, given this website, please help me make the following easy updates; provide the result in the order that makes everything easier and faster for me.


** ADMIN Quotes, Location type: dropdown, 
direccion, textarea, dress code dropdown, 
- MONTO POR PAGAR en db (auto update)
- - On cotizador add a field for address below the ubicación dropdown. (FRONT END)
- fix frontend cotizador radios
- On step two, let the user choose between our most popular packages (that I set up on admin.) or create a custom package (which is the option currently implemented)
- The interior/exterior radio buttons should be presented on the same line. 
    - The input for quote tracking code should be smaller (about 10 characters long). After pressing the "Rastrear mi cotización" button, the code input should be displayed underneath the button (not underneath both buttons) then the search button below the code input. 

- I want to be able to rename programs. And disable sorting on Home › Quotes › Programs
- Fix cotizador detail (
TemplateDoesNotExist at /cotizacion/gwwrzsev/

quotes/cotizacion_detail.html

Request Method: 	GET
Request URL: 	https://musicaparamisas.com/cotizacion/gwwrzsev/
Django Version: 	4.2.23
Exception Type: 	TemplateDoesNotExist
Exception Value: 	

quotes/cotizacion_detail.html

Exception Location: 	/var/www/coralia-django/venv/lib/python3.9/site-packages/django/template/loader.py, line 19, in get_template
Raised during: 	quotes.views.cotizacion_detail_view
Python Executable: 	/var/www/coralia-django/venv/bin/python3
Python Version: 	3.9.2
Python Path: 	

['/var/www/coralia-django',
 '/var/www/coralia-django/venv/bin',
 '/usr/lib/python39.zip',
 '/usr/lib/python3.9',
 '/usr/lib/python3.9/lib-dynload',
 '/var/www/coralia-django/venv/lib/python3.9/site-packages']

Server time: 	Sun, 29 Jun 2025 18:06:42 -0600
Template-loader postmortem

Django tried loading these templates, in this order:

Using engine django:

    django.template.loaders.filesystem.Loader: /var/www/coralia-django/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/venv/lib/python3.9/site-packages/admin_reorder/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/auth/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/venv/lib/python3.9/site-packages/request/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/main/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/quotes/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/analytics/templates/quotes/cotizacion_detail.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /var/www/coralia-django/venv/lib/python3.9/site-packages/adminsortable2/templates/quotes/cotizacion_detail.html (Source does not exist)

)





# V 2 - PAGOS / CONTRATOS / EMAILS 

- PERMITIR ARMAR LA PLANTILLA DE MÚSICOS 
- CADA QUIEN SUS QUOTES, 
- INCLUIR DESCUENTO SITIO WEB AJUSTAR TARIFA (+20%) (-20%) 
- PREPARAR LO DEL CONTRATO
- BOTON PARA DATOS DE PAGO
- PREPARAR BOTONES PARA COBRAR EN STRIPE
- ADMINISTRAR EMAILS Y SETEAR? (un solo formato y en txt se hagan automático?)
- MAILS DESDE BOTÓN (ENVIAR CORREO DE CONFIRMACIÓN)
- DIRECCIÓN DEL EVENTO esta debe setear ubicación 
- Contact methods en modelo (más no en admin)

##TODO 

Hello, given this website, please help me make the following easy updates; provide the result in the order that makes everything easier and faster for me.

- For quotes, I want to be able to include discounts. (Will be presented on frontend only when a discount exists)
- Include a field for event_address
- For quotes, as I have for event_types I want to have "packages". This field is not obligatory for quotes. Each package will have a name, description, number of singers, number of instrument players. 

- For quotes, I want to be able to modify any quote and the price should be recalculated. If there is an easy way to track these changes, help me implement it.  
- Only for quotes where a package is not set, I want to use the number of musicians variables set in quotes (number of musicians, number of voices)
- In quotes, also include a field in the table for payment per musician, and should be set automatically and updated by the system. 
- In quotes, also include a field for "paid_amount", which will default to 0 but will let me add their upfront payments, etc... 
- On admin, when I am editing or creating a quote, the button for new program displays the popup correctly, and functions correctly but submission triggers the error I paste below.
- I want to be able to rename programs. And disable sorting on Home › Quotes › Programs
- Admin request package (https://musicaparamisas.com/admin/request/request/overview/) is not ignoring admin, favicon, etc... which is set here with no effect: IGNORE_PATHS = (
    r'^admin/',
    r'^static/',
    r'^media/',
)

# A list of user agents to ignore.
IGNORE_USER_AGENTS = (
    r'.*bingbot.*',
    r'.*Googlebot.*',
    r'.*AhrefsBot.*',
    r'.*SemrushBot.*',
    r'.*YandexBot.*',
    r'.*DotBot.*',
)

# A list of usernames to ignore.
# Set to an empty tuple to log requests from all users, including staff.
IGNORE_USERNAME = ()

# Only log requests that result in an error.
ONLY_ERRORS = False

# Don't log AJAX requests.
IGNORE_AJAX = True


- On frontend cotizador:
    - Create a new view and template for cotización called cotizacion_detail. This will include the program (when it is set), payment information (bank transfer and instructions for cash payments on confirmed quotes) and later on a copy of the contract.  
    - The input for quote tracking code should be smaller (about 10 characters long). After pressing the "Rastrear mi cotización" button, the code input should be displayed underneath the button (not underneath both buttons) then the search button below the code input. 
    - On cotizador add a field for address below the ubicación dropdown. 
    - The interior/exterior radio buttons should be presented on the same line. 
    - On step two, let the user choose between our most popular packages (that I set up on admin.) or create a custom package (which is the option currently implemented)
    - In last method, preferred method of contact should be radio buttons on each line instead of dropdown. 

- Update the servicios view/template so that it shows the event types from database fields. and now it should consist of two columns. Left column is for list of services, right column put a list of the most popular/famous pieces of our repertorie we play and a link to the rest of our repertorie at the bottom of such list. 
- I need my favicon fixed, 
- If needed present steps in several prompts. 


Log of error mentioned avobe. 

Environment:


Request Method: POST
Request URL: https://musicaparamisas.com/admin/quotes/program/add/?_to_field=id&_popup=1

Django Version: 4.2.23
Python Version: 3.9.2
Installed Applications:
['admin_reorder',
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'request',
 'main.apps.MainConfig',
 'quotes.apps.QuotesConfig',
 'analytics.apps.AnalyticsConfig',
 'user_visit',
 'adminsortable2']
Installed Middleware:
['django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 'request.middleware.RequestMiddleware',
 'analytics.middleware.VisitTrackingMiddleware',
 'user_visit.middleware.UserVisitMiddleware',
 'admin_reorder.middleware.ModelAdminReorder']



Traceback (most recent call last):
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/options.py", line 688, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/utils/decorators.py", line 134, in _wrapper_view
    response = view_func(request, *args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/views/decorators/cache.py", line 62, in _wrapper_view_func
    response = view_func(request, *args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/sites.py", line 242, in inner
    return view(request, *args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/options.py", line 1886, in add_view
    return self.changeform_view(request, None, form_url, extra_context)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/utils/decorators.py", line 46, in _wrapper
    return bound_method(*args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/utils/decorators.py", line 134, in _wrapper_view
    response = view_func(request, *args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/options.py", line 1747, in changeform_view
    return self._changeform_view(request, object_id, form_url, extra_context)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/contrib/admin/options.py", line 1798, in _changeform_view
    self.save_model(request, new_object, form, not add)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/adminsortable2/admin.py", line 259, in save_model
    self.get_max_order(request, obj) + 1
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/adminsortable2/admin.py", line 361, in get_max_order
    return self.model.objects.aggregate(
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/db/models/query.py", line 592, in aggregate
    return self.query.chain().get_aggregation(self.db, kwargs)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/db/models/sql/query.py", line 559, in get_aggregation
    result = next(compiler.apply_converters((result,), converters))
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/db/models/sql/compiler.py", line 1500, in apply_converters
    value = converter(value, expression, connection)
  File "/var/www/coralia-django/venv/lib/python3.9/site-packages/django/db/models/expressions.py", line 376, in <lambda>
    else int(value)

Exception Type: ValueError at /admin/quotes/program/add/
Exception Value: invalid literal for int() with base 10: 'Programa de Evento'


** ADMIN Quotes, Location type: dropdown, 
direccion, textarea, dress code dropdown, 



- Descuentos en quotes
- PAQUETE SELECCIONADO 
- PODER MODIFICAR COTIZACION Y ¿RECALCULAR? (DESDE ADMIN)
- INCLUIR CASILLA PARA PAGO POR MÚSICO
- QUOTES CON paid_amount.
- ADMIN FIX (nuevo programa desde quote)
- ADMIN poder RENOMBRAR PROGRAMAS Y EL REORDER EN Home › Quotes › Programs 

- EN FRONTEND (cotozador):
    - VER DETALLE DE COTIZACION (cliente) cotizacion_detail (programa y plantilla) (DATOS DE PAGO APARECERAN AL CONFIRMAR UNA COTIZACIÓN, DATOS DE FACTURACIÓN)
    - INPUT MÁS PEQUEÑO PARA CÓDIGO y abajo del botón, y lleva a cotización detail. 
    - NUEVO CAMPO DIRECCION DEL LUGAR
    - MEJORAR interior/exterior (misma linea)
    - PASO 2 PAQUETES (ESTANDAR: 5 MÚSICOS) Y LINK ABAJO QUE DIGA ARMAR MI PROPIO CORO A LA MEDIDA (PAQUETES ACTUALIZA MÚSICOS)
    - Prefiero que me contacten por radio buttons. ¿u ocultar?

- Servicios desde base de datos, e incluir repertorio.


- FIX FAVICON





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

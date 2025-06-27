# Coralia Ensamble - Django Website

This is a Django-based web application for the Coralia Ensamble Musical group, migrated from an original Flask implementation.

It includes a public-facing website, a detailed repertoire catalogue, and a multi-step quoting system for musical services. The administration backend is built using Django's built-in admin, providing robust tools for managing site content.

## Local Development Setup (Full Project)

Follow these instructions to get the complete project running on your local machine once all steps are finished.

### 1. Prerequisites

- Python 3.9 or newer
- `pip` for installing packages
- A copy of your website's data dump named `backup.sql` in the project root directory.

### 2. Installation

1.  **Create Project:**
    Place all project files from the 4-step guide into the correct structure.

2.  **Create and Activate a Virtual Environment (Recommended):**

    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    Install all required Python packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

### 3. Database Setup and Data Migration (After Step 4)

1.  **Apply Migrations:**
    This command will create a new, empty `db.sqlite3` file with the correct schema for the Django application.

    ```bash
    python manage.py migrate
    ```

2.  **Load Data from Your Backup:**
    This crucial step uses a custom command to read your `backup.sql` file and transfer all your repertoire, tags, and quotes into the new Django database.
    **Make sure `backup.sql` is in the project's root directory.**

    ```bash
    python manage.py load_from_backup
    ```

3.  **Create a Superuser:**
    You need an admin account to log into the Django admin panel. Follow the prompts to create your username and password.

    ```bash
    python manage.py createsuperuser
    ```

### 4. Running the Development Server

You are now ready to run the site!

```bash
python manage.py runserver


Flask url_for Call	Django {% url %} or {% static %} Tag	Notes
url_for('main.index')	{% url 'main:index' %}	app_name:url_name
url_for('main.servicios')	{% url 'main:servicios' %}	
url_for('main.videos')	{% url 'main:videos' %}	
url_for('main.contacto')	{% url 'main:contacto' %}	
url_for('main.repertorio_list')	{% url 'main:repertorio_list' %}	
url_for('main.cotizador')	{% url 'quotes:cotizador' %}	Moved to quotes app
url_for('static', ... 'css/..')	{% static 'css/...' %}	For static files
url_for('static', ... 'img/..')	{% static 'img/...' %}	For static files
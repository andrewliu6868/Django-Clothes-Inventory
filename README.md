# About The Project

A small Django project I wrote for a Take-Home Assignment that mimics the clothing inventory of an online clothing shop. The clothing items include 5 categories of clothing (Shirts, Jackets, Pants...etc), 10 tag descriptors (Athletic, Casual, Wool...etc), and 20 clothing products).

The UI is a simple Django HTML template that allows users to search for products by description, filter by tags, filter by categories, or any combination of these filters. For the database, I used the default SQLite since we are working with a small amount of data and we don't need to worry about scalability.

# Set-up

## 1) Create python virtual environment and git clone

Before cloning, set-up a python virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Clone the repository
git clone 
cd
```


## 2) Install necessary dependencies

For this project, I used Django version 4.2.25 and I used python-dotenv version 1.0.1 to load in my Django secret key. To ensure your system will be able to properly run the project, use the following command to install the correct version of Django and dotenv.
```bash
pip install -r requirements.txt
```

## 3) Create a .env file for Django Secret Key

Because it's unsafe to push my secret key to a public repo, you will need to create your own .env file in order to properly run the project. Create a .env file and fill out like below

```
DJANGO_SECRET=your_key_here
```

To generate a new Django secret key, you can use:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 4) Database Migrations
Run the following commands to set up the database:
```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate
```

## 5) Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

The application should now be accessible at `http://127.0.0.1:8000/`

# Additional Notes

For clarity, I used ChatGPT to help come up with the sample data of 20 clothing products, but not for the actual code. Likewise, I used Github Copilot for simple HTML formatting, specifically for the <fieldset> and <legend> portion of product_list.html.

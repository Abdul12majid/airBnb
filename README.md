**Airbnb Clone with Django REST Framework**

This project is an Airbnb clone built using _Django REST Framework_. 
It allows users to list and search for properties, manage bookings, and provides functionalities similar to the popular accommodation rental platform.

**Technologies Used**

1. Python 3.11
2. Django
3. Django REST Framework (DRF)

**Requirements**

1. Python 3.11 installed
2. Django installed

**Installation**

1. Clone this repository: git clone https://github.com/Abdul12majid/airBnb.git
2. Navigate to the project directory: cd airBnb
3. Create a virtual environment (recommended): pythom -m venv py_env
4. Activate virtual environment: source py_env/scripts/activate
5. Install project dependencies: pip install -r requirements.txt
6. Migrate the database (assuming using a database like PostgreSQL): python manage.py migrate   #sqlite was used for this, fell free to connect to more standard database.
7. Create a superuser account (optional, for initial admin access): winpty python manage.py createsuperuser

**Usage**

1. Start the development server: python mnage.py runserver
2. Access the API documentation at - http://127.0.0.1:8000/api/docs/

**Features** 

1. User registration and login
2. Listing properties (including title, description, location, availability status, amenities, price per night)
3. Book/Unbook property.
4. See app all-time booking history.
5. See profile booking history.
6. Submit/Edit reviews on properties.
7. Rate a property.
8. Search by title of property.

**Contact Me**

For any questions or feedback, feel free to reach out to Majid at yisaabdulmajid@gmail.com or open an issue on the GitHub repository.
   

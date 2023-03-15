# Stripe-Payment-Gateway-Integration

* A payment gateway for Stripe payment method
* Stripe API is used for integration <br>

[Live App](https://payment1.pythonanywhere.com/) <br>
___

Project is created with: 
* [Django 4.1](https://docs.djangoproject.com/en/4.1/)
* [Stripe API](https://stripe.com/docs/api)


## How to run this app on your machine? <br>
### 1. Extract and open the project, then install the requirements.txt using pip
```
pip install -r requirements.txt
```

### 2. For migrations, type this on your terminal
```
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the server using the following command
```
python manage.py runserver
```

Your Django project is **LIVE** now on your localhost. <br>
Open your browser and type **127.0.0.1:8000** on address bar.<br>
<br> <br>

**NOTE:** On **settings.py** file, you must use your own Stripe API Keys. You can get those keys on your Stripe account under Developers option. <br>
```
STRIPE_SECRET_KEY = ''
STRIPE_PUBLISHABLE_KEY = ''
```
___

## Screenshots
### 1. Stripe Payment Gateway



![Image](https://drive.google.com/uc?id=107Bh4eBY3ZGiQeFkwegkCI5_ZOroNe1V)


### 2. Payment Successful



![Image](https://drive.google.com/uc?id=1oyd9G21JY7R9d6QsN0o-pny2W2-e0pWI)


### 3. API Logs in Stripe



![Image](https://drive.google.com/uc?id=1mWac--mWyyDpfTrhJ2my0IIQIhhaDolC)

___
### THANK YOU!

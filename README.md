# Nth Fibonacci Api

This API is used to find the number present at nth position in the fibonacci sequence.

## To run it on local server

1. Clone this repository:
 ```
 $ git clone https://github.com/akramkazmi71/nth-fibonacci-api.git
 ```
 2. Change the directory to nth-fibonacci-api folder:
 ```
 $ cd nth-fibonacci-api
 ```
 3. Download Django to your system:
 ```
 $ pip3 install -r requirements.txt
 ```
 4. To run the API:
 ```
 $ python3 manage.py runserver 8080
 ```

 ### Testing

 In order to test this API:
 ```
 $ python3 manage.py test
 ```

 ### To run on PythonAnywhere

 1. Login to [Pythonanywhere](https://www.pythonanywhere.com).

 2. Generate API Token in Accounts page.

 3. Start `bash` console from dashboard.

 4. Run this command: 
 ```
  $ pa_autoconfigure_django.py --python=3.6 https://github.com/akramkazmi71/nth-fibonacci-api
  ``` 
# fsf_2019_screening_task1
Task Manager application implemented using Django. 

1. Create a virtual environment on your machine. 
    ```
    virtualenv -p python your_environment_name
    ```
    We recommend using python -virtualenv. Any other packages would do fine though.

2. Activate the newly created virtual environment:
    ```
    cd your_environment_name
    source bin/activate
    ```

3. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/samyak047/fsf_2019_screening_task1
    ```
    
4. Install the dependencies for the project.
    ```
    cd fsf_2019_screening_task1
    pip install -r requirements.txt
    ```
5. Migrate your database.
    ```
    python manage.py makemigrations
    python manage.py migrate 
    ``` 

6. Run the live development server on your machine and test it.
    ```
    python manage.py runserver
    ```
 
    Once the server is started, open http://127.0.0.1:8000 or whatever server you are running on in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.

7. Test the app.
    ```
    python manage.py test
    ```
####Accounts

Some Pre-registered accounts to view and test the live development server on your machine:

#### user

| **Username**   | **Password** |
| -------------- | ------------ |
| samyak047      | samyak047    |
| apurva         | apurvamishra |
| aks.modi     	 | aks.modi     |

Superuser:
	username: admin
	password: adminpassword
 


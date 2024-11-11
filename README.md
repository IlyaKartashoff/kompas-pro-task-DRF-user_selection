## Installation:
### 1. Clone the repository:
   ```bash
    git clone https://github.com/IlyaKartashoff/kompas-pro-task-DRF-user_selection.git
```
    
### 2. Create an virtual environment:

  ```bash
    python -m venv venv
    
    venv\Scripts\activate    
  ```
### 3. Install the dependencies:
```bash
    pip install -r requirements.txt
```
### 4. Run database migrations:
```bash
    python manage.py migrate
```
### 5. Create a superuser:
```bash
    python manage.py createsuperuser
```
## 6. At this time you can check command):
```bash
    python manage.py create_users
```
### 7. Run server:
```bash
    python manage.py runserver
```
## Now the project will be available at `http://127.0.0.1:8000/api/users`.
Also, url for admin panel `http://127.0.0.1:8000/admin` 

### 4. If using Docker, start the containers:
```bash
    docker-compose up
```
## 





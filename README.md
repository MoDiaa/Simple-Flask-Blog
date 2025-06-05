## Running MySQL with Docker and Initializing the Database

1. **Start MySQL using Docker:**
   ```sh
   docker run --name devops-mysql -e MYSQL_ROOT_PASSWORD=yourpassword -e MYSQL_DATABASE=devopsdb -p 3306:3306 -d mysql:8.0
   ```
   - Replace `yourpassword` with a secure password.
   - The database `devopsdb` will be created automatically.

2. **Update your `config.py`:**
   Set your MySQL connection string, for example:
   ```python
   SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:yourpassword@localhost:3306/devopsdb"
   ```
   - Make sure you have `pymysql` installed (`pip install pymysql`).

3. **Install requirements (if not done):**
   ```sh
   pip install -r requirements.txt
   ```

4. **Initialize the database tables:**
   - Start a Flask shell:
     ```sh
     flask shell
     ```
   - Inside the shell, run:
     ```python
     from app import db
     db.create_all()
     ```
   - This will create all tables defined in your models.

5. **Run the Flask application:**
   ```sh
   flask run
   ```
# Simple-Flask-Blog

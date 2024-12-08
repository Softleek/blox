import os
import subprocess
import pymysql
import sqlite3
import platform
from getpass import getpass
import re
from ...config import PROJECT_ROOT, APPS_TXT_PATH
import click

def run_django_migrations():
    """Run Django makemigrations and migrate commands."""
    python_command = "python" if platform.system() == "Windows" else "python3"

    subprocess.run(
        f'echo "y" | {python_command} manage.py makemigrations',
        shell=True,
        cwd=os.path.join(PROJECT_ROOT, "apps/core/django"),
    )

    subprocess.run(
        [python_command, "manage.py", "migrate", "--noinput"],
        cwd=os.path.join(PROJECT_ROOT, "apps/core/django"),
    )

    click.echo("Migration completed.")

def createsuperuser():
    run_django_migrations()

    """Run Django createsuperuser command non-interactively by prompting user for details."""
    python_command = "python" if platform.system() == "Windows" else "python3"

    create_superuser_args = [python_command, "manage.py", "createsuperuser"]

    subprocess.run(
        create_superuser_args,
        shell=False,
        cwd=os.path.join(PROJECT_ROOT, "apps/core/django"),
        env={**os.environ,}  
    )

    click.echo("Superuser created successfully.")

def install_database():
    """Install MariaDB or MySQL depending on the OS."""
    os_name = platform.system().lower()

    print("Checking if MariaDB/MySQL is installed...")
    try:
        subprocess.run(["mysql", "--version"], check=True)
        print("MariaDB/MySQL is already installed.")
    except subprocess.CalledProcessError:
        print("MariaDB/MySQL is not installed. Installing now...")
        if 'ubuntu' in os_name or 'debian' in os_name:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "mariadb-server", "-y"], check=True)
        else:
            subprocess.run(["sudo", "yum", "install", "mysql-server", "-y"], check=True)

        subprocess.run(["sudo", "systemctl", "start", "mariadb" if 'ubuntu' in os_name or 'debian' in os_name else "mysqld"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "mariadb" if 'ubuntu' in os_name or 'debian' in os_name else "mysqld"], check=True)

    return True

def create_database_user():
    """Create a new database user or ensure the user exists with all privileges."""
    root_password = getpass("Enter MySQL/MariaDB root password: ")
    new_user = input("Enter the new username: ")
    new_password = getpass(f"Enter password for {new_user}: ")
    new_db = input("Enter the new database name: ")

    conn = pymysql.connect(user="root", password=root_password, host="localhost")
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT COUNT(*) FROM mysql.user WHERE user = '{new_user}' AND host = 'localhost';")
        user_exists = cursor.fetchone()[0]

        if user_exists == 0:
            cursor.execute(f"CREATE USER '{new_user}'@'localhost' IDENTIFIED BY '{new_password}';")
            print(f"User {new_user} created successfully.")
        else:
            print(f"User {new_user} already exists.")

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_db};")
        cursor.execute(f"GRANT ALL PRIVILEGES ON {new_db}.* TO '{new_user}'@'localhost' WITH GRANT OPTION;")
        conn.commit()
        print(f"Privileges granted to user {new_user} for database {new_db}.")
    except pymysql.MySQLError as e:
        print(f"Failed to create user or grant privileges: {e}")
    finally:
        conn.close()

    return new_user, new_password, new_db

def drop_existing_tables(db_name, user, password, host="localhost"):
    """Drop all tables in the given database."""
    conn = pymysql.connect(user=user, password=password, host=host, database=db_name)
    cursor = conn.cursor()

    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS `{table[0]}`;")
            print(f"Table `{table[0]}` dropped.")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        conn.commit()
        print(f"All tables in database '{db_name}' have been dropped.")
    except pymysql.MySQLError as e:
        print(f"Failed to drop tables: {e}")
    finally:
        conn.close()

def update_app_settings(user, password, db_name, host="localhost"):
    """Update settings.py to use MariaDB/MySQL."""
    settings_file = "apps/core/django/backend/settings.py"

    with open(settings_file, "r") as file:
        settings_content = file.read()

    pattern = r"\bDATABASES\s*=\s*\{(?:[^{}]|\{[^{}]*\})*\}\s*"
    updated_settings_content = re.sub(pattern, "", settings_content, flags=re.DOTALL).strip()

    new_db_settings = f"""
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{db_name}',
        'USER': '{user}',
        'PASSWORD': '{password}',
        'HOST': '{host}',
        'PORT': '3306',
    }}
}}
"""

    updated_settings_content += new_db_settings

    with open(settings_file, "w") as file:
        file.write(updated_settings_content)

    print(f"settings.py updated to use MariaDB/MySQL with database '{db_name}'.")

@click.command()
def migratedb(sqlite_db_path=None):
    """Main function to handle the entire migration process."""
    install_database()
    user, password, db_name = create_database_user()
    drop_existing_tables(db_name, user, password)
    update_app_settings(user, password, db_name)
    createsuperuser()

if __name__ == "__main__":
    migratedb()

import os
import subprocess
import sys
import click
import socket
from ...utils.config import PROJECT_ROOT, write_running_ports


def find_free_port(start_port=3000):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("localhost", port)) != 0:
                return port
            port += 1


def run_with_sudo(command):
    """Run a command with sudo privileges."""
    subprocess.run(["sudo"] + command, check=True)


def setup_nginx(domain, appname, nextjs_port, django_port):
    nginx_conf = f"""
    server {{
        listen 80;
        server_name {domain} www.{domain};

        location / {{
            proxy_pass http://127.0.0.1:{nextjs_port};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }}

        location /apis/ {{
            proxy_pass http://127.0.0.1:{django_port};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }}

        location /static/ {{
            alias /path/to/your/static/files/;
        }}
    }}
    """

    conf_path = f"/etc/nginx/sites-available/{appname}"
    symlink_path = f"/etc/nginx/sites-enabled/{appname}"

    # Write the configuration to /etc/nginx/sites-available with sudo
    with open(conf_path, "w") as file:
        file.write(nginx_conf)

    # Create symlink in /etc/nginx/sites-enabled with sudo
    run_with_sudo(["ln", "-s", conf_path, symlink_path])
    run_with_sudo(["nginx", "-t"])
    run_with_sudo(["systemctl", "reload", "nginx"])
    click.echo(f"Nginx configuration for {appname} has been set up and reloaded.")


def setup_supervisor(appname, django_port, nextjs_port):
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(PROJECT_ROOT, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Log files
    django_log = os.path.join(logs_dir, f"{appname}_django.log")
    nextjs_log = os.path.join(logs_dir, f"{appname}_nextjs.log")

    # Prompt for the username
    username = click.prompt(
        "Enter the username to run the Supervisor process", type=str
    )

    venv_path = os.path.join(PROJECT_ROOT, "env")
    python_executable = os.path.join(venv_path, "bin", "python3")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    supervisor_conf = f"""
    [program:{appname}_django]
    command={python_executable} manage.py runserver 0.0.0.0:{django_port}
    directory={PROJECT_ROOT}/apps/core/django
    autostart=true
    autorestart=true
    stderr_logfile={django_log}
    stdout_logfile={django_log}
    user={username}
    
    [program:{appname}_nextjs]
    command=npm run start -- --port {nextjs_port}
    directory={PROJECT_ROOT}/apps/core/nextjs
    autostart=true
    autorestart=true
    stderr_logfile={nextjs_log}
    stdout_logfile={nextjs_log}
    user={username}
    """

    conf_path = f"/etc/supervisor/conf.d/{appname}.conf"

    # Write the configuration to /etc/supervisor/conf.d with sudo
    with open(conf_path, "w") as file:
        file.write(supervisor_conf)

    # Update Supervisor configurations and start the app with sudo
    run_with_sudo(["supervisorctl", "reread"])
    run_with_sudo(["supervisorctl", "update"])
    run_with_sudo(["supervisorctl", "start", f"{appname}_django"])
    run_with_sudo(["supervisorctl", "start", f"{appname}_nextjs"])
    click.echo(f"Supervisor configuration for {appname} has been set up and started.")


def setup_ssl(domain):
    click.echo("Setting up SSL with Let's Encrypt...")
    # Using sudo to install SSL certificates
    run_with_sudo(["certbot", "--nginx", "-d", domain, "-d", f"www.{domain}"])
    click.echo(f"SSL certificate for {domain} has been set up.")


@click.command()
@click.argument("mode", default="prod")
def deploy(mode):
    venv_path = os.path.join(PROJECT_ROOT, "env")
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return

    python_executable = os.path.join(venv_path, "bin", "python3")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    django_port = find_free_port(8000)
    nextjs_port = find_free_port(3000)

    domain = click.prompt("Enter your domain name", type=str)
    appname = click.prompt("Enter your app name", type=str)

    setup_nginx(domain, appname, nextjs_port, django_port)
    setup_supervisor(appname, django_port, nextjs_port)
    setup_ssl(domain)

    # Writing running ports to the specified file
    write_running_ports(django_port, nextjs_port)

    # Closing the script after starting the processes via Supervisor
    click.echo("Deployment is complete. The services are running in the background.")

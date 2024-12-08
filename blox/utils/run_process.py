import subprocess
import sys
import os
import click
from .config import PROJECT_ROOT

def get_python_executable():
    venv_path = os.path.join(PROJECT_ROOT, "env")
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return

    python_executable = os.path.join(venv_path, "bin", "python3")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")
    return python_executable

def run_subprocess(command, cwd=None):
    """Run a subprocess command, using cmd.exe on Windows."""
    if sys.platform.startswith('win'):
        return subprocess.Popen(['cmd.exe', '/c'] + command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
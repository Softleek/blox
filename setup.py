import subprocess
import sys

from setuptools import find_packages, setup

DEPENDENCIES = [
    "asgiref",
    "autoflake",
    "black",
    "certifi",
    "cffi",
    "charset-normalizer",
    "cryptography",
    "defusedxml",
    "Django",
    "django-allauth",
    "django-cors-headers",
    "django-crontab",
    "django-filter",
    "django-multiselectfield",
    "djangorestframework",
    "flake8",
    "idna",
    "isort",
    "oauthlib",
    "pandas",
    "Pillow",
    "pycparser",
    "PyJWT",
    "PyMySQL",
    "python-barcode",
    "python-decouple",
    "python3-openid",
    "pytz",
    "qrcode",
    "requests",
    "requests-oauthlib",
    "six",
    "sqlparse",
    "typing_extensions",
    "tzdata",
    "urllib3",
    "unicode",
    "whitenoise",
    "xlrd",
]


def check_and_install_deps():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade"] + DEPENDENCIES
    )


check_and_install_deps()

setup(
    name="blox",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points={
        "console_scripts": [
            "blox=blox.cli:cli",
        ],
    },
)

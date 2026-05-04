"""
Demonstration application showcasing common Python security vulnerabilities.

This module includes examples of:
1. Format string vulnerability
2. Code injection via dynamic imports
3. Unsafe YAML deserialization
4. Improper use of assert for authentication

It also exposes a simple Flask web endpoint for fetching URLs.
"""

import sys
import os
import yaml
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    """HTTP endpoint that fetches a website based on query parameters."""
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person(object):
    """Simple Person class holding a name."""

    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    """Print a formatted nametag using a user-supplied format string."""
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    """
    Dynamically imports a urllib version and fetches a URL.

    WARNING: Uses exec(), which is unsafe and vulnerable to code injection.
    """
    exec(f"import urllib{urllib_version} as urllib", globals())

    try:
        http = urllib.PoolManager()
        r = http.request('GET', url)
    except:
        print('Exception')


def load_yaml(filename):
    """
    Load and deserialize YAML data from a file.

    WARNING: Uses unsafe yaml.load(), which can lead to code execution.
    """
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader)
    return deserialized_data


def authenticate(password):
    """
    Authenticate user using an assert statement.

    WARNING: Assertions can be bypassed when Python is run with optimizations.
    """
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
from flask import Flask
import os
from api import app


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
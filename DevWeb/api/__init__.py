from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = "123"

from api import views

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from model import db, connect_to_db, User

import os

app = Flask(__name__)
# required to have secret key to use Flask sessions and debug toolbar 
# generate random 32 bit secret key!  
app.secret_key= os.urandom(32)

# Throws up error if have undefined error in Jinja2
app.jinja_env.undefined = StrictUndefined
from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from model import db, connect_to_db, User, association_table, Suggestion, Tea, Note

import os

app = Flask(__name__)
# required to have secret key to use Flask sessions and debug toolbar 
# generate random 32 bit secret key!  
app.secret_key= os.urandom(32)

# Throws up error if have undefined error in Jinja2
app.jinja_env.undefined = StrictUndefined
































if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    print("Connected to DB.")

    DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000,debug=False)
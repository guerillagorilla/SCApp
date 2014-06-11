from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

import logging

app = Flask("Small Cell Lab Application")
app.config.from_object('config')

app.debug = False
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#app.config['TRAP_BAD_REQUEST_ERRORS'] = True
#app.config['TRAP_HTTP_EXCEPTIONS'] = True

@app.errorhandler(404)
def not_found(e):
    return "OH GOD WHY", 404

from app.views import mod as views
app.register_blueprint(views)

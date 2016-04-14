from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

ale = Blueprint('ale', __name__,
                        template_folder='templates')

@lager.route('/')
@lager.route('/ale')
def pint():
    try:
        return "MMMMMM ale"
    except TemplateNotFound:
        abort(404)
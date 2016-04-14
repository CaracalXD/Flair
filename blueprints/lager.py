from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

lager = Blueprint('lager', __name__,
                        template_folder='templates')

@lager.route('/')
@lager.route('/lager')
def pint():
    try:
        return "MMMMMM lager"
    except TemplateNotFound:
        abort(404)
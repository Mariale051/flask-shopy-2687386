from flask import Blueprint
clientes = Blueprint('cliente',
                      __name__,
                      url_prefix = '/clientes' ,
                      template_folder = 'templates')

from . import routes 
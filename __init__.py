import os

from flask import Flask

#
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  
#

def create_app():
    app = Flask(__name__)
    #app.run(debug=True) 

    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)


    @app.route('/hola')
    def hola():
        return 'Roma'
    return app
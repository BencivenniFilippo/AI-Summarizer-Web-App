from flask import Flask, render_template
from app.routes import main_blueprint
import dotenv
dotenv.load_dotenv()
import os

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ["MY_KEY"]

    app.register_blueprint(main_blueprint)

    
    # HANDLING ERRORS
    # Invalid URL
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error_URL.html'), 404

    # Internal Server Error
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('error_URL.html'), 500

    return app

app = create_app()
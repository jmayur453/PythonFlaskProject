from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__, static_url_path='/static')

    # Register routes
    from app.routes.main_routes import main_routes
    from app.routes.translate_routes import translate_api
    from app.routes.image_routes import image_api
    from app.routes.ascii_routes import ascii_bp
    from app.routes.handwriting import handwriting_bp
    from app.routes.chatbot_routes import chatbot_api
    from app.routes.geolocation_routes import geolocation_api
    from app.routes.map_view import map_view

    app.register_blueprint(main_routes)
    app.register_blueprint(translate_api)
    app.register_blueprint(image_api)
    app.register_blueprint(ascii_bp) 
    app.register_blueprint(handwriting_bp) 
    app.register_blueprint(chatbot_api) 
    app.register_blueprint(geolocation_api) 
    app.register_blueprint(map_view) 
    return app

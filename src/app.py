# RESPONSÁVEL PELA CRIAÇÃO DA APLICAÇÃO
# CREATE_APP() -> VAI CONFIGURAR A INSTÂNCIA DO FLASK
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json/",
            "rule_filter": lambda rule: True, # < Indica que todas a rotas vão estar na documentação
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

def create_app():
    app = Flask(__name__)
    CORS(app, origins="*") # <-- Adicione a autorização do CORS para todas as rotas na aplicação
    app.register_blueprint(bp_colaborador)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    Swagger(app, config=swagger_config)
    return app
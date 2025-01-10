from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# Inicializar extensões
csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações básicas
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3307/SistemaHospitalar'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta'

    # Inicializar extensões
    csrf.init_app(app)
    db.init_app(app)

    # Registrar blueprints (se houver)
    from app.routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)
simao0simba0
    return app

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import main, question, answer
    app.register_blueprint(main.bp)
    app.register_blueprint(question.bp)
    app.register_blueprint(answer.bp)

    return app
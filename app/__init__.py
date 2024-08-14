from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')

    app = Flask(__name__)
    config_class = config.factory(app_context if app_context else 'development')
    app.config.from_object(config_class)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.resources import home, user_bp, workout_bp, exercise_bp, repetition_bp
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(workout_bp, url_prefix='/workouts')
    app.register_blueprint(exercise_bp, url_prefix='/exercises')
    app.register_blueprint(repetition_bp, url_prefix='/repetitions')

    @app.shell_context_processor
    def make_shell_context():
        return {"app": app, "db": db}

    return app

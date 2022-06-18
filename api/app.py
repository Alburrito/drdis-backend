# Python imports
import os

# Flask improts
from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS

# Internal imports
from config import LocalConfig, TestingConfig, StagingConfig, ProductionConfig
from database import connect_to_mongo_database


def create_app(environment = None):
    """
    Creates the app and configures it according to the environment.
    """
    app = Flask(__name__)
    env = environment if environment else os.environ.get('ENVIRONMENT', 'local')

    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'staging':
        app.config.from_object(StagingConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    elif env == 'local':
        app.config.from_object(LocalConfig)
    else:
        app.config.from_object(LocalConfig)
        invalid_env = env
        env = 'local'
        print(f'Invalid environment name: {invalid_env}. Using local conf instead.')

    # Initializations
    CORS(app)
    conn_db = connect_to_mongo_database(
        app.config['DB_HOST'],
        int(app.config['DB_PORT']),
        app.config['DB_NAME']
    )
    # Flask blueprints

    # Other
    Swagger(app)

    return app, conn_db


flask_app, conn_db = create_app()

@flask_app.route('/', methods=['GET'])
def index():
    """
    Endpoint to test if the API is running.
    ---
    returns:
        200:
            description: Server returns a welcome
            type: string
            example: "This is FOO REPORTS, the DRDIS host system"
    """
    return jsonify('This is FOO REPORTS, the DRDIS host system'), 200


if __name__ == '__main__':
    flask_app.run(debug = flask_app.config['FLASK_DEBUG'],
                  host = flask_app.config['FLASK_RUN_HOST'],
                  port = flask_app.config['FLASK_RUN_PORT']
                )

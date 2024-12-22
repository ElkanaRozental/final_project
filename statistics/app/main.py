from flask import Flask

from app.routs.terror_data_routs import terror_data_blueprint

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(terror_data_blueprint, url_prefix='/api')
    app.run(port=5002)
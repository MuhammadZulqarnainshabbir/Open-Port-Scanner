import logging as logger

from flask import Flask

logger.basicConfig(level="DEBUG")

app = Flask(__name__)
if __name__ == '__main__':
    from api import *
    app.run(host="0.0.0.0", port="5000", debug=True, use_reloader=True)


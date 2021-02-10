import os

from flask import Flask
from socket import getfqdn

flask_host = os.environ.get("HOST", "0.0.0.0")
flask_port = os.environ.get("PORT", "8080")
flask_debug = os.environ.get("DEBUG", False)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        f"<h1>"
        f"<br><p>&nbsp;&nbsp;&nbsp;&nbsp;"
        f"Hello, World from {getfqdn()}  =)"
        f"</h1>"
    )


if __name__ == "__main__":
    app.run(debug=flask_debug, host=flask_host, port=flask_port)

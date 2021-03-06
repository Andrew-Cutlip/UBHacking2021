from flask import Flask
import grid

app: Flask = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host, port)

    grid = grid.Grid(1,1,1)

from flask import Flask, render_template

from db import get_connection

app = Flask(__name__)


@app.route("/")
def index():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION() AS version")
        row = cursor.fetchone()
    connection.close()
    return render_template("index.html", version=row["version"])


if __name__ == "__main__":
    app.run(debug=True)

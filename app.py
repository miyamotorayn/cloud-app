from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Cloud Technologies</title>
    </head>
    <body>
        <h1>Cloud Technologies Laboratory</h1>
        <p>My first Docker application</p>
        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/contact">Contact</a>
        </nav>
    </body>
    </html>
    """


@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This Flask web application runs inside a Docker container.</p>
    <a href="/">Back to home</a>
    """


@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>
    <p>Contact page of the Cloud Technologies project.</p>
    <a href="/">Back to home</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

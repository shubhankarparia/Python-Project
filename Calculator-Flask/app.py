# ==========================================
# Project : Calculator Website
# File    : app.py
# Framework : Flask
# ==========================================

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the calculator homepage."""
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors."""
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
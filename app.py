from flask import Flask, render_template
from main.views import main_bp
from search.views import search_bp
from bookmarks.views import bookmarks_bp
from api.views import api_bp
from logger import config

app = Flask(__name__)

config(app)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_bp)
app.register_blueprint(search_bp)
app.register_blueprint(bookmarks_bp)
app.register_blueprint(api_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

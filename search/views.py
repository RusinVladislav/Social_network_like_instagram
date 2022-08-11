import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from utils import search_for_posts

search_bp = Blueprint('search_bp', __name__, template_folder='templates')


@search_bp.route('/search/')
def search_page():
    search_qwery = request.args.get('s', '')
    find_posts = search_for_posts(search_qwery)
    return render_template('search.html', qwery=search_qwery, posts=find_posts)

import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from utils import get_bookmarks_all

bookmarks_bp = Blueprint('bookmarks_bp', __name__, template_folder='templates')


@bookmarks_bp.route('/bookmarks/')
def bookmarks_page():
    posts = get_bookmarks_all()
    return render_template('bookmarks.html', posts=posts)


@bookmarks_bp.route('/bookmarks/')
def bookmarks_add():
    posts = get_bookmarks_all()
    return render_template('bookmarks.html', posts=posts)

@bookmarks_bp.route('/bookmarks/')
def bookmarks_del():
    posts = get_bookmarks_all()
    return render_template('bookmarks.html', posts=posts)

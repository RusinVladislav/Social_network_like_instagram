import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request, redirect
from utils import get_bookmarks_all, add_bookmarks, del_bookmarks

bookmarks_bp = Blueprint('bookmarks_bp', __name__, template_folder='templates')


@bookmarks_bp.route('/bookmarks/')
def bookmarks_page():
    posts = get_bookmarks_all()
    return render_template('bookmarks.html', posts=posts)


@bookmarks_bp.route('/bookmarks/add/<int:post_id>')
def bookmarks_add(post_id):
    add_bookmarks(post_id)
    return redirect("/", code=302)


@bookmarks_bp.route('/bookmarks/del/<int:post_id>')
def bookmarks_del(post_id):
    del_bookmarks(post_id)
    return redirect("/", code=302)

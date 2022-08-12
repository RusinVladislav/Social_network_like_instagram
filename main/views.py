import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from utils import get_posts_all, get_comments_by_post_id, get_posts_by_id, get_posts_by_user, get_posts_by_tag

main_bp = Blueprint('main_bp', __name__, template_folder='templates')


@main_bp.get('/')
def main_page():
    qwery = request.args.get('s', '')
    posts = get_posts_all()
    return render_template('index.html', posts=posts, qwery=qwery)


@main_bp.get('/posts/<int:post_id>')
def post_page(post_id):
    post = get_posts_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@main_bp.get('/users/<username>')
def user_page(username):
    name = username.title()
    posts_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user, name=name)


@main_bp.get('/tags/<tag>')
def tags_page(tag):
    tag = tag.lower()
    posts = get_posts_by_tag(tag)
    return render_template('tag.html', posts=posts, tag=tag)

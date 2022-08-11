import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from utils import get_posts_all, get_comments_by_post_id, get_posts_by_id, get_posts_by_user

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


# @main_bp.get('/search/')
# def search_page():
#     # qwery_arguments
#     search_qwery = request.args.get('s', '')
#     logging.info('Выполняю поиск поста')
#     try:
#         posts = get_posts_by_word(search_qwery)
#     except FileNotFoundError:
#         logging.error('Файл не найден')
#         return "Файл не найден"
#     except JSONDecodeError:
#         return "Файл JSON не валидный"
#     return render_template('post_list.html', qwery=search_qwery, posts=posts)

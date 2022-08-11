import logging
from flask import Blueprint, jsonify
from utils import get_posts_all, get_posts_by_id


api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/api/posts/')
def api_posts():
    data = get_posts_all()
    return jsonify(data)


@api_bp.route('/api/posts/<int:post_id>')
def api_post_by_id(post_id):
    data = get_posts_by_id(post_id)
    return jsonify(data)

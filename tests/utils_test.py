import pytest

from utils import *


class TestUtils:
# TODO переписать все через isinstans

    def test_get_posts_all(self):
        assert isinstance(get_posts_all(), list), 'Функция возвращает не лист'

    def test_get_comments_all(self):
        assert type(get_comments_all()) == list, 'Функция возвращает не лист'

    def test_get_bookmarks_all(self):
        assert type(get_bookmarks_all()) == list, 'Функция возвращает не лист'

    def test_get_posts_by_user(self):
        assert type(get_posts_by_user('leo')) == list, 'Функция возвращает не лист'
        assert len(get_posts_by_user('leo')) == 2, 'Функция возвращает не верные данные'

    def test_get_posts_by_id(self):
        assert type(get_posts_by_id(1)) == dict, 'Функция возвращает не лист'
        assert len(get_posts_by_id(1)) == 7, 'Функция возвращает не верные данные'

    def test_get_comments_by_post_id(self):
        assert type(get_comments_by_post_id(1)) == list, 'Функция возвращает не лист'
        assert len(get_comments_by_post_id(1)) == 4, 'Функция возвращает не верные данные'

    def test_search_for_posts(self):
        assert type(search_for_posts('')) == list, 'Функция возвращает не лист'

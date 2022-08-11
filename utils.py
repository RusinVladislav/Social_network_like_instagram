import json

data_posts = "./data/data.json"
data_comments = "./data/comments.json"
data_bookmarks = "./data/bookmarks.json"


def get_posts_all() -> list[dict]:
    """Читает данные из файла json с постами и возвращает список словарей"""

    with open(data_posts, 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_comments_all() -> list[dict]:
    """Читает данные из файла json с комментариями и возвращает список словарей"""

    with open(data_comments, 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_bookmarks_all() -> list[dict]:
    """Читает данные из файла json с заметками и возвращает список словарей"""

    with open(data_bookmarks, 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_posts_by_user(user_name) -> list[dict]:
    """
    Возвращает посты определенного пользователя по его имени.
    Вызывает ошибку ValueError если такого пользователя нет и пустой список, если у пользователя нет постов.
    """

    wanted_posts = []
    all_users_name = []
    posts = get_posts_all()

    for post in posts:
        all_users_name.append(post['poster_name'].lower().strip())
        if post['poster_name'].lower().strip() == user_name.lower().strip():
            wanted_posts.append(post)

    if user_name.lower().strip() in all_users_name:
        return wanted_posts
    else:
        raise ValueError(f"Пользователь с именем {user_name} не найден")


def get_posts_by_id(post_id) -> dict:
    """
    Возвращает посты определенного пользователя по его имени.
    Вызывает ошибку ValueError если такого пользователя нет и пустой список, если у пользователя нет постов.
    """

    posts = get_posts_all()

    for post in posts:
        if post['pk'] == post_id:
            return post


def get_comments_by_post_id(post_id) -> list[dict]:
    """
    Возвращает комментарии определенного поста по его номеру.
    Вызывает ошибку ValueError если такого поста нет и пустой список, если у поста нет комментариев.
    """

    wanted_comments = []
    all_post_id = []
    comments = get_comments_all()

    for comment in comments:
        all_post_id.append(comment['post_id'])
        if comment['post_id'] == post_id:
            wanted_comments.append(comment)

    if post_id in all_post_id:
        return wanted_comments
    else:
        raise ValueError(f"Пост с номером {post_id} не найден")


def search_for_posts(qwery) -> list[dict]:
    """Возвращает список постов по ключевому слову"""

    wanted_posts = []
    posts = get_posts_all()

    for post in posts:
        if qwery.lower().strip() in post['content'].lower().strip():
            wanted_posts.append(post)

    return wanted_posts

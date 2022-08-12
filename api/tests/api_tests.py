import pytest
from app import app


def test_app():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200, 'Не верный код ответа'
    assert type(response.json) == list, 'Возвращается не список'
    assert set(response.json[0].keys()) == set(['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'])
    assert response.json[0]['pk'] == 1, 'Ключ pk отсутствует'
    assert response.json[0]["poster_name"] == "leo", 'Ключ poster_name отсутствует'
    assert response.json[0]["poster_avatar"] == "https://randus.org/avatars/w/c1819dbdffffff18.png", 'Ключ poster_avatar отсутствует'
    assert response.json[0]["pic"] == "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80", 'Ключ pic отсутствует'
    assert response.json[0]["content"] == "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.", 'Ключ content отсутствует'
    assert response.json[0]["views_count"] == 376, 'Ключ views_count отсутствует'
    assert response.json[0]["likes_count"] == 154, 'Ключ likes_count отсутствует'


def test_one():
    params = {"s": 1}
    response = app.test_client().get('/api/posts/', query_string=params)
    assert response.status_code == 200, 'Не верный статус код'
    assert len(response.json) == 8, 'Не верное количество данных'
    assert type(response.json) == list, 'Возвращается не список'
    assert response.json[0]['pk'] == 1, 'Ключ pk отсутствует'
    assert response.json[0]["poster_name"] == "leo", 'Ключ poster_name отсутствует'
    assert response.json[0]["poster_avatar"] == "https://randus.org/avatars/w/c1819dbdffffff18.png", 'Ключ poster_avatar отсутствует'
    assert response.json[0]["pic"] == "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80", 'Ключ pic отсутствует'
    assert response.json[0]["content"] == "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.", 'Ключ content отсутствует'
    assert response.json[0]["views_count"] == 376, 'Ключ views_count отсутствует'
    assert response.json[0]["likes_count"] == 154, 'Ключ likes_count отсутствует'


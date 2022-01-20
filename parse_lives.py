import requests
import hashlib

from settings import lives_url

"""
По ссылке https://line14.bkfon-resources.com/live/currentLine/ru получить все футбольные матчи в Лайве.
Данные записать в словарь по названию игроков в виде gamer_name = "Игрок 1 - Игрок 2".
Словарь должен быть в ввиде: {id1: gamer_name1, id2: gamer_name2, .... idN: gamer_nameN}
id - уникальный идентификатор в md5
Для получения идентификатора использовать модуль hashlib
"""


def get_sport_ids(sport_name, json_response):
    sports = []
    for sport in json_response['sports']:
        if sport_name in sport['name'].lower():
            sports.append(sport['id'])

    return sports


def get_games(sport_ids: list, json_response):
    games = {}
    for event in json_response['events']:
        for sport_id in sport_ids:
            if event['sportId'] == sport_id:
                try:
                    gamer_name = f"{event['team1']} - {event['team2']}"
                    game_id = hashlib.md5(gamer_name.encode()).hexdigest()
                    games[game_id] = gamer_name
                except KeyError:
                    continue
    return games


def parse_sport_games(sport_name):

    response = requests.get(lives_url)

    json_data = response.json()

    football_ids = get_sport_ids(sport_name, json_data)

    games = get_games(football_ids, json_data)

    return games


if __name__ == '__main__':
    from settings import sport_name
    games = parse_sport_games(sport_name)
    print(games)

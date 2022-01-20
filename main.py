import random
import time
from parse_lives import parse_sport_games
from open_games import FonbetSeleParser
from settings import sport_name


fonbet_browser = FonbetSeleParser(headless=False)

games = parse_sport_games(sport_name)

# open 5 random games for example
for _ in range(5):
    chosed_game = random.choice(list(games.values()))

    fonbet_browser.open_live_game(chosed_game)

    print(chosed_game)

    time.sleep(10)

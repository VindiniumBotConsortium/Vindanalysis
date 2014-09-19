#!/usr/bin/env python

import random, itertools, logging

import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

logging.basicConfig()
logger = logging.getLogger(__name__)

client = MongoClient()
db = client['vindiniminer']

def games_lazily(names_list):
    for name in names_list:
        logger.info("hitting database for %s" % name)
        yield list(db[name].find())


def detect_death(hero, game):
    """if the hero's life returns to 100 and the hero moves to his spawnpos,
    then the hero has died."""
    deaths = []
    spawn_pos = game[0]['heroes'][hero-1]['spawnPos']
    last_pos  = game[0]['heroes'][hero-1]['pos']
    last_life = game[0]['heroes'][hero-1]['life']

    for i in range(1, len(game)):
        this_pos  = game[i]['heroes'][hero-1]['pos']
        this_life = game[i]['heroes'][hero-1]['life']

        if this_life > last_life and this_pos != last_pos and this_pos == spawn_pos:
            deaths.append(i)

        last_pos = this_pos
        last_life = this_life

    return deaths

def places(game):
    """ return an ordered list of players and their scores, winner first """
    last_turn = game[-1]['heroes']
    last_turn.sort(key=lambda x: int(x['gold']), reverse=True)
    return [(i['id'], i['gold']) for i in last_turn]

def who_won(game):
    """ return a list of the winners of the game with their scores"""
    last_turn = places(game)
    winner = itertools.takewhile(lambda x: (x['gold'] == last_turn[0]['gold']), last_turn)
    return [(i['id'], i['gold']) for i in winner]

def wins_and_deaths(game_ids):
    result = []
    games = games_lazily(game_ids)
    for game in games:
        ranking = [int(i[0]) for i in places(game)]
        deaths_by_ranking = [len(detect_death(i, game)) for i in ranking]
        result.append(deaths_by_ranking)

    return result


# initial mucking around
names = db.collection_names()
random.seed(0) # for replicability

sample = random.sample(names, 100)
item = db[sample[0]]
game = list(item.find())

wd = np.array(wins_and_deaths(sample))
plt.boxplot(wd)
plt.show()

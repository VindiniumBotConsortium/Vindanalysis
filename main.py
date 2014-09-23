#!/usr/bin/env python3

import random, itertools, logging

import numpy as np
import matplotlib.pyplot as plt

import lib.game_utils as GUtils

logging.basicConfig()
logger = logging.getLogger(__name__)


# Import game-level feature extractors
# XXX: improve me!
from lib.features.game.winner          import *
GAME_FEATURES = {
    'winner': Winner()
}

# Import hero-level feature extractors
from lib.features.hero.wins_and_deaths import *
HERO_FEATURES = {
    'wins' : Win('cb1'),        # FIXME: some thing to do with this.
    'deaths': Deaths('cb1')
}


# For access to command-line stuff.
import sys

# Number of games to sample from the DB
SAMPLE_SIZE = 100
SAMPLE_SEED = (sys.argv[1] if len(sys.argv) >= 2 else 0)


# initial mucking around
# names = db.collection_names()
random.seed(SAMPLE_SEED) # for replicability

#sample = random.sample(names, SAMPLE_SIZE)
#item = db[sample[0]]
#game = list(item.find())

sample = GUtils.sample_games(SAMPLE_SIZE)

for game in GUtils.games_lazily(sample):

    for k, v in GAME_FEATURES.items():
        print("G->", k, ":", v.extract(game))

    for k, v in HERO_FEATURES.items():
        print("H->", k, ":", v.extract(game))




# wd = np.array(wins_and_deaths(sample))
# plt.boxplot(wd)
# plt.show()

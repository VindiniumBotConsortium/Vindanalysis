



import itertools

from lib.feature_extractor import *
import lib.game_utils as GUtils

class Win(HeroFeature):

    def __init__(self, heroName):
        super(Win, self).__init__(VariableType.boolean, heroName)

    # FIXME: detext if heroname is in the game.
    def extract(self, game):
        ranking = [int(i[0]) for i in GUtils.places(game)]

        print(ranking)

        return False





class Deaths(HeroFeature):

    def __init__(self, heroName):
        super(Deaths, self).__init__(VariableType.continuous, heroName)

    def extract(self, game):
        ranking           = [int(i[0]) for i in GUtils.places(game)]
        deaths_by_ranking = [len(self.__detect_death(i, game)) for i in ranking]

        # FIXME: figure out who is who and return.

        return 1

    def __detect_death(self, hero, game):
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





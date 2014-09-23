




import itertools

from lib.feature_extractor import *
import lib.game_utils as GUtils

class Winner(GameFeature):

    def __init__(self):
        super(Winner, self).__init__(VariableType.discrete)


    # FIXME: this returns too much data.  Return only the winner.
    def extract(self, game):
        """Override.  Extract & return the winner from the game provided"""
        # last_turn = GUtils.places(game)

        # import pdb; pdb.set_trace()

        # winner = itertools.takewhile(lambda x: (x['gold'] == last_turn[0]['gold']), last_turn)
        # return [(i['id'], i['gold']) for i in winner]
        return 'test'



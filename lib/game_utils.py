
from pymongo import MongoClient
import random

# XXX: Remove me when/if moving to a log-based solution.
from warnings import warn

# TODO: make it possible to configure this on import/
#       use.
#
# TODO: encapsulate this in a separate db/storage class,
#       rather than conflating it with utils.
DB_NAME                 = 'vindiniminer'
INDEX_COLLECTION_NAME   = 'vindindex'

client  = MongoClient()
db      = client[DB_NAME]



def sample_games(n):
    index = db[INDEX_COLLECTION_NAME]
    # TODO: test if index
    
    # Return list of retrieved games
    games = index.find( {'retrieved': True} )
    games = list(map(lambda x: x['hash'], games))

    # Warn if we're going to basically sample everything
    if len(games) <= n:
        warn("Sampling %d from a set of cadinality %d: will return all." % [len(games), n])
        n = len(games)
        return games

    # Sample this
    return random.sample(games, n)


def games_lazily(names_list):
    """Return games from the database as a coroutine."""
    for name in names_list:
        # logger.info("hitting database for %s" % name)
        yield list(db[name].find())



def places(game):
    """Return an ordered list of players and their scores, winner first. """
    last_turn = game[-1]['heroes']
    last_turn.sort(key=lambda x: int(x['gold']), reverse=True)
    return [(i['id'], i['gold']) for i in last_turn]


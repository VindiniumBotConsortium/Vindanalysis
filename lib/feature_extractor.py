

from enum import Enum

class VariableType(Enum):
    """Represents the type of an extracted feature."""

    continuous  = 1
    discrete    = 2
    boolean     = 3


class FeatureExtractor:
    """A function that accepts some complex data and returns a single
    parameter in accordance with its type.
    
    No guarantees are given as to the statistical properties of the data
    returned, or the return of null values.
    """


    def __init__(self, type):
        """Set the parameters and type of the feature to be extracted."""
        self.type = type


    def extract(game):
        # STUB
        pass


class GameFeature(FeatureExtractor):
    """Responsible for stripping a feature regarding a game from a 
    mongo object."""


class HeroFeature(FeatureExtractor):
    """Responsible for stripping a feature regarding a single player
    from a game."""

    def __init__(self, type, heroName):
        super(HeroFeature, self).__init__(type)
        self.heroName = str(heroName)



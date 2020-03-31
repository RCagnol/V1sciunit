from sciunit.scores.complete import *

class GreaterThanScore(BooleanScore):
    """A boolean score, which must be True or False."""

    _description = ('True if the prediction is greater than a value passed in input; False otherwise')
    @classmethod
    def compute(self,value, prediction):
        """Compute whether the observation is greater than a value passed in input."""
        return GreaterThanScore(prediction > value)


class LesserThanScore(BooleanScore):
    """A boolean score, which must be True or False."""


    _description = ('True if the prediction is lesser than a value passed in input; False otherwise')
    @classmethod
    def compute(self, value, prediction):
        """Compute whether the prediction is lesser than a value passed in input."""
        return LesserThanScore(value > prediction)

'''
class StudentsTestScore(Score):
    """A Cohen's D score.

    A float indicating difference
    between two means normalized by the pooled standard deviation.
    """

    _description = ("The Cohen's D between the prediction and the observation")

    @classmethod
    def compute(cls, observation, prediction):
        """Compute a Cohen's D from an observation and a prediction."""
        assert isinstance(observation, dict)
        assert isinstance(prediction, dict)
        p_mean = prediction['mean']  # Use the prediction's mean.
        p_std = prediction['std']
        o_mean = observation['mean']
        o_std = observation['std']
        try:  # Try to pool taking samples sizes into account.
            p_n = prediction['n']
            o_n = observation['n']
            s = (((p_n-1)*(p_std**2) + (o_n-1)*(o_std**2))/(p_n+o_n-2))**0.5
        except KeyError:  # If sample sizes are not available.
            s = (p_std**2 + o_std**2)**0.5
        value = (p_mean - o_mean)/s
        value = utils.assert_dimensionless(value)
        return CohenDScore(value)

    def __str__(self):
        return 'D = %.2f' % self.score


'''

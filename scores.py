from sciunit.scores.complete import *
import scipy.stats as st
import statsmodels.stats.power as pw
import numpy

class StudentsTestScore(Score):
    """A Student's t-test score.

    A float indicating the difference between two means normalized by the two standard deviations and the two sample sizes
    Contains also the p value, which evaluates the significativity of this difference
    """

    _description = ("The t statistic between the prediction and the observation")

    @classmethod
    def compute(cls, observation, prediction):
        """Compute a t statistic and a p_value from an observation and a prediction."""
        
	p_mean = prediction['mean']  # Use the prediction's mean.
       	p_std = prediction['std']
       	p_n = prediction['n']
        p_var= p_std**2
	
	#2 samples t-test
	if isinstance(observation, dict):
		o_mean = observation['mean']
        	o_std = observation['std']
        	o_n = observation['n']
		o_var=o_std**2 
       

		#If the 2 variances are too different, perform a Welsh t-test 	
		if p_var/o_var > 2 or o_var/p_var > 2: 
			value, p_val = st.ttest_ind_from_stats(p_mean,p_std,p_n,o_mean,o_std,o_n,equal_var=False)
		else:
        		value, p_val = st.ttest_ind_from_stats(p_mean,p_std,p_n,o_mean,o_std,o_n,equal_var=True)
	
		power=pw.TTestIndPower().power(effect_size=CohenDScore.compute(observation,prediction).score,nobs1=p_n,ratio=float(o_n)/p_n,alpha=0.05)

	#1 sample t-test
	else:
		value, p_val= st.ttest_ind_from_stats(p_mean, p_std, p_n, observation, std2=0, nobs2=2, equal_var=False)	
                power=pw.TTestIndPower().power(effect_size=CohenDScore.compute({"mean":observation,"std":0},prediction).score,nobs1=p_n,alpha=0.05)
			
	return StudentsTestScore(value,related_data={"p_value": p_val,"power": power})
	
    def __str__(self):
	if self.test.sheets:
		return 't = %.2f, p=%.6f, power=%.6f for sheet(s) %s' % (self.score, self.related_data["p_value"], self.related_data["power"],self.test.sheets)
        else:
	        return 't = %.2f, p=%.6f' % (self.score, self.related_data["p_value"])



class ShapiroTestScore(Score):
    """A Shapiro-Wilk test score.

    A float indicating the difference between the distribution of the prediction and the one indicated in the observation string 
    Contains also the p value, which evaluates the significativity of this difference
    """

    _description = ("The Shapiro's W between the two distributions")

    @classmethod
    def compute(cls, observation, prediction):
        """Compute a Shapiro's W from an observation and a prediction."""

	if observation == "normal":
	        value, p_val = st.shapiro(prediction)
	
	elif observation== "lognormal":
		logPredictions=[]
		for p in prediction:
			if p:
				logPrediction=numpy.log(p)
			else:
				logPrediction=numpy.log(0.000000001)
			logPredictions.append(logPrediction)		
		value, p_val = st.shapiro(logPredictions)
	
        return ShapiroTestScore(value,related_data={"p_value": p_val})

    def __str__(self):
        if self.test.sheets:
		return 'W = %.2f, p=%.6f for sheet(s) %s' % (self.score, self.related_data["p_value"],self.test.sheets)
	else:
		return 'W = %.2f, p=%.6f' % (self.score, self.related_data["p_value"])

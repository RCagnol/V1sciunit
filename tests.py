import sciunit
import capabilities as cap
import scores 
#===============================================================================

class ExcitatoryAverageFiringRate(sciunit.Test):
    """Test the if the sheets average firing rate is lesser than a predefined value"""

    score_type = scores.LesserThanScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheets average firing rate is lesser than a predifined value"
    """brief description of the test objective"""

    def __init__(self,
                 observation = None,
		 sheets = None,
                 name = "Excitatory Average Firing Rate Test"):
        if type(observation).__module__=="numpy":
		observation=observation.item()
	self.required_capabilities += (cap.SheetsFiringRate,)
        self.sheets=sheets
        sciunit.Test.__init__(self, observation, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
        	assert (isinstance(observation, int) or isinstance(observation, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a float or an integer"))
        	
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_firing_rate(self.sheets)
        if type(prediction).__module__=="numpy":
		prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
	score = scores.LesserThanScore.compute(observation, prediction)
        return score



class InhibitoryAverageFiringRate(sciunit.Test):
    """Test the if the sheets average firing rate is greater than a predefined value"""

    score_type = scores.GreaterThanScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheets average firing rate is greater than a predefined value"
    """brief description of the test objective"""

    def __init__(self,
                 observation = None,
		 sheets = None,
                 name = "Inhibitory Average Firing Rate Test"):

	if type(observation).__module__=="numpy":
        	observation=observation.item()
 
        self.required_capabilities += (cap.SheetsFiringRate,)
        self.sheets=sheets
        sciunit.Test.__init__(self, observation, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
        	assert (isinstance(observation, int) or isinstance(observation, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a float or an integer"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_firing_rate(self.sheets)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.GreaterThanScore.compute(observation, prediction)
	return score

class RestingPotential(sciunit.Test):
    """Test the sheets' average resting membrane potential"""

    score_type = sciunit.scores.CohenDScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average resting membrane potential")
    """brief description of the test objective"""

    def __init__(self,
                 observation,
		 sheets, 
                 name ="Sheets Resting Membrane Potential Test"):
        self.required_capabilities += (cap.SheetsMembranePotential,)
        self.sheets=sheets
	sciunit.Test.__init__(self, observation, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3 
            for key, val in observation.items():
		assert key in ["mean", "std","n"]
		if key =="n":
                	assert (isinstance(val, int))
		else:
                	assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_membrane_potential(self.sheets)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
	score = sciunit.scores.CohenDScore.compute(observation, prediction)
        return score

class ExcitatorySynapticConductance(sciunit.Test):
    """Test the sheets' average excitatory synaptic conductance"""

    score_type = sciunit.scores.CohenDScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average excitatory synaptic conductance")
    """brief description of the test objective"""

    def __init__(self,
                 observation,
                 sheets,
                 name ="Sheets Excitatory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsExcitatorySynapticConductance,)
        self.sheets=sheets
        sciunit.Test.__init__(self, observation, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_excitatory_synaptic_conductance(self.sheets)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        score = sciunit.scores.CohenDScore.compute(observation, prediction)
        return score

class InhibitorySynapticConductance(sciunit.Test):
    """Test the sheets' average inhibitory synaptic conductance"""

    score_type = sciunit.scores.CohenDScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average inhibitory synaptic conductance")
    """brief description of the test objective"""

    def __init__(self,
                 observation,
                 sheets,
                 name ="Sheets Inhibitory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsInhibitorySynapticConductance,)
        self.sheets=sheets
        sciunit.Test.__init__(self, observation, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_inhibitory_synaptic_conductance(self.sheets)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        score = sciunit.scores.CohenDScore.compute(observation, prediction)
        return score


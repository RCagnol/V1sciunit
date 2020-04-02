import sciunit
import capabilities as cap
import scores 
#===============================================================================


class Test(sciunit.Test):
    """ Extension of sciunit.nest by adding the parameter sheet """


    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Excitatory Average Firing Rate Test"):

        self.sheet=sheet
        sciunit.Test.__init__(self, observation, name)


class ExcitatoryAverageFiringRate(Test):
    """Test the if the distribution of the sheet average firing rates is significatively lesser than a predefined value"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet average firing rate is lesser than a predifined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
                 name = "Excitatory Average Firing Rate Test"):
	
	self.required_capabilities += (cap.StatsSheetFiringRate,)
        Test.__init__(self,observation, sheet, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        
	try:
        	assert (isinstance(observation, int) or isinstance(observation, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a float or an integer"))
        	
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.stats_sheet_firing_rate(self.sheet)
        if type(prediction).__module__=="numpy":
		prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
	score = scores.StudentsTestScore.compute(observation, prediction)
     	return score



class InhibitoryAverageFiringRate(Test):
    """Test the if the sheet average firing rates is significantly greater than the average firing rates 
	of a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet average firing rate is greater than a predefined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
                 name = "Inhibitory Average Firing Rate Test"):

        self.required_capabilities += (cap.StatsSheetFiringRate,)
        Test.__init__(self, observation, sheet, name)

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
        prediction=model.stats_sheet_firing_rate(self.sheet)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
	return score


class DistributionAverageFiringRate(Test):
    """Test the if the sheet average firing rates distributions is significatively different 
    than a specific distribution"""

    score_type = scores.ShapiroTestScore
    """specifies the type of score returned by the test"""

    description = """Test if the sheet average firing rates distributions is significatively different 
    than a specific distribution""" 

    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Distribution Average Firing Rate Test"):

        self.required_capabilities += (cap.SheetFiringRate,)
        Test.__init__(self, observation, sheet, name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert isinstance(observation, str)
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation should be a string containing the name of the distribution the average firing rates should be compared to, either: 'normal' or 'lognormal'"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheet_firing_rate(self.sheet)
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.ShapiroTestScore.compute(observation, prediction)
        return score


class CorrelationCoefficient(Test):
    """Test the if the sheet distribution correlation coefficient is significatively greater than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet correlation coefficient is greater than a predefined value"

    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Correlation Coefficient Test"):

        if type(observation).__module__=="numpy":
                observation=observation.item()

        self.required_capabilities += (cap.SheetCorrelationCoefficient,)
        Test.__init__(self, observation, sheet, name)

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
        prediction=model.sheet_correlation_coefficient(self.sheet)
        if type(prediction).__module__=="numpy":
                prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score






class RestingPotential(Test):
    """Test the sheets' average resting membrane potential"""

    #score_type = sciunit.scores.CohenDScore
    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average resting membrane potential")

    def __init__(self,
                 observation,
		 sheet, 
                 name ="Sheets Resting Membrane Potential Test"):
        self.required_capabilities += (cap.SheetsMembranePotential,)
	Test.__init__(self, observation, sheet, name)

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
        prediction = model.sheets_membrane_potential(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        observation["std"] = observation["std"]*(float(observation["n"])/(observation["n"]-1))**0.5 #Bessel's correction for unbiased variance	
	score = scores.StudentsTestScore.compute(observation, prediction)
        return score

class ExcitatorySynapticConductance(Test):
    """Test the sheets' average excitatory synaptic conductance"""

    score_type = scores.StudentsTestScore 
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average excitatory synaptic conductance")

    def __init__(self,
                 observation,
                 sheet,
                 name ="Sheets Excitatory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsExcitatorySynapticConductance,)
        Test.__init__(self, observation, sheet, name)

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
        prediction = model.sheets_excitatory_synaptic_conductance(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        observation["std"] = observation["std"]*(float(observation["n"])/(observation["n"]-1))**0.5 #Bessel's correction for unbiased variance
	score = scores.StudentsTestScore.compute(observation, prediction)
        return score

class InhibitorySynapticConductance(Test):
    """Test the sheet' average inhibitory synaptic conductance"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheet' average inhibitory synaptic conductance")

    def __init__(self,
                 observation,
                 sheet,
                 name ="Sheets Inhibitory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsInhibitorySynapticConductance,)
        Test.__init__(self, observation, sheet, name)

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
        prediction = model.sheets_inhibitory_synaptic_conductance(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        observation["std"] = observation["std"]*(float(observation["n"])/(observation["n"]-1))**0.5 #Bessel's correction for unbiased variance
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score


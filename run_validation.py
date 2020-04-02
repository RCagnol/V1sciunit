from models import *
from tests import *


newModel=ModelV1Spont("SelfSustainedPushPull_test_____/")


newTest=ExcitatoryAverageFiringRate(2,"V1_Exc_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitoryAverageFiringRate(newModel.stats_sheet_firing_rate("V1_Exc_L4"),"V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ExcitatoryAverageFiringRate(2,"V1_Exc_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitoryAverageFiringRate(newModel.stats_sheet_firing_rate("V1_Exc_L2/3"),"V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Exc_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Exc_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CorrelationCoefficient(newModel.sheet_correlation_coefficient("V1_Exc_L4"),"V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CorrelationCoefficient(newModel.sheet_correlation_coefficient("V1_Exc_L2/3"),"V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=RestingPotential({"mean": -72.8, "std": 5, "n": 119},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ExcitatorySynapticConductance({"mean": 0.001, "std": 0.0009, "n": 22},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitorySynapticConductance({"mean": 0.0049, "std": 0.0036, "n": 22},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()


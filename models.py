import sciunit
from capabilities import * # One of many potential model capabilities.
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore


class ModelV1Spont(sciunit.Model, SheetsFiringRate, SheetsMembranePotential, SheetsExcitatorySynapticConductance, SheetsInhibitorySynapticConductance):
	"""A model of spontaneous activity of V1."""

	def __init__(self, path, name="Spontaneous activity of V1"):
		""" path should be a string containing  the path of the files containing the results of the simulation of the model
		"""

		self.data_store = param_filter_query(PickledDataStore(load=True,parameters=ParameterSet({'root_directory': path,'store_stimuli' : False}),replace=True),st_direct_stimulation_name=None,st_name="InternalStimulus")
		super(ModelV1Spont, self).__init__(name=name, data_store=self.data_store)

	def sheets_firing_rate(self, sheets):
		"""Get the average firing rate of the sheets
		sheets should be a list containing the name of the sheets
		"""	

		if type(sheets)== str:
                        sheets=[sheets]
                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

		return param_filter_query(self.data_store,analysis_algorithm='PopulationMeanAndVar',sheet_name=sheets,identifier='SingleValue',value_name='Mean(Firing rate)',ads_unique=True).get_analysis_result()[0].value

	def sheets_membrane_potential(self, sheets):
		"""Get the average resting membrane potential of the sheets"""
		ms = lambda a: (numpy.mean(a),numpy.std(a))
		n=0
		if type(sheets)== str:
			sheets=[sheets]
		else:
			try:
		                assert (isinstance(sheets, list))
        		except Exception:
            			raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

		for s in sheets:
			try: 
                                assert (isinstance(s, str))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
			n+=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids())
		
		mean_VM, std_VM = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values)
		print(n)
		print(mean_VM)
		print(std_VM)
		return {"mean": mean_VM, "std": std_VM, "n": n}




	def sheets_excitatory_synaptic_conductance(self, sheets):
		"""Get the average excitatory synaptic conductance of the sheets"""
               
		ms = lambda a: (numpy.mean(a),numpy.std(a))
                n=0
                if type(sheets)== str:
                        sheets=[sheets]
                else:
                        try: 
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                for s in sheets:
                        try:
                                assert (isinstance(s, str))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
                        n+=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_esyn_ids())
	
		mean_ECond, std_ECond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values)
		print(n)
		print(mean_ECond)
		print(std_ECond)
                return {"mean": mean_ECond, "std": std_ECond, "n": n}
	



	def sheets_inhibitory_synaptic_conductance(self, sheets):
		"""Get the average inhibitory synaptic conductance of the sheets"""
                ms = lambda a: (numpy.mean(a),numpy.std(a))
                n=0
		if isinstance(sheets,str):
                        sheets=[sheets]
                else:
                        try: 
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                for s in sheets:
                        try:
                                assert (isinstance(s, str))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
                        n+=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_isyn_ids())
		
		mean_ICond, std_ICond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values)
		print(n)
		print(mean_ICond)
		print(std_ICond)
                return {"mean": mean_ICond, "std": std_ICond, "n": n}

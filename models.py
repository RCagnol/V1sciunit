import sciunit
from capabilities import * # One of many potential model capabilities.
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore


class ModelV1Spont(sciunit.Model, StatsSheetFiringRate, SheetsMembranePotential, SheetsExcitatorySynapticConductance, SheetsInhibitorySynapticConductance, SheetCorrelationCoefficient):
	"""A model of spontaneous activity of V1."""

	def __init__(self, path, name="Spontaneous activity of V1"):
		""" path should be a string containing  the path of the files containing the results of the simulation of the model
		"""

		self.data_store = param_filter_query(PickledDataStore(load=True,parameters=ParameterSet({'root_directory': path,'store_stimuli' : False}),replace=True),st_direct_stimulation_name=None,st_name="InternalStimulus")
		super(ModelV1Spont, self).__init__(name=name, data_store=self.data_store)


	def sheet_firing_rate(self, sheet):
		"""Get the average firing rates of the sheet
                sheet should be a string containing the name of the sheet
                """
		try:
                        assert (isinstance(sheet, str))
                except Exception:
                        raise sciunit.errors.Error("Parameter sheet must be a string")

                return param_filter_query(self.data_store, value_name='Firing rate', identifier='PerNeuronValue', sheet_name=sheet, analysis_algorithm='TrialAveragedFiringRate').get_analysis_result()[0].values

	

	def stats_sheet_firing_rate(self, sheet):
		"""Get descriptive statistics about the average firing rates of the sheet
		sheet should be a string containing the name of the sheet
		"""	
                AVF= self.sheet_firing_rate(sheet)
		mean_AVF=numpy.mean(AVF)
                std_AVF=numpy.std(AVF,ddof=1)
                n=len(AVF)
                return {"mean": mean_AVF, "std": std_AVF, "n": n}


	def sheet_correlation_coefficient(self, sheet):
		"""Get the correlation coefficient of the sheet
		sheet should be a string containing the name of the sheet
		"""	

                try:
                	assert (isinstance(sheet, str))
                except Exception:
                	raise sciunit.errors.Error("Parameter sheet must be a string")
		
		CC=param_filter_query(self.data_store, value_name='Correlation coefficient(psth (bin=10.0))', identifier='PerNeuronValue', sheet_name=sheet, analysis_algorithm='NeuronToNeuronAnalogSignalCorrelations').get_analysis_result()[0].values
		mean_CC=numpy.mean(CC)
		std_CC=numpy.std(CC,ddof=1)
		n=len(CC)	
		
		return {"mean": mean_CC, "std": std_CC, "n": n}


	def sheets_membrane_potential(self, sheets):
		"""Get the average resting membrane potential of the sheets"""
	
		ms = lambda a: (numpy.mean(a),numpy.std(a))
		population=[]
		mean=[]
		std=[]

		if type(sheets)== str:
			mean_VM, std_VM = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values)
			n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids())
	
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
				population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
				mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values))
				std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values, ddof=1))
	
			mean_VM, std_VM = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values)
			mean_VM=numpy.mean(mean)
			std_VM=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
			n=sum(population)

		return {"mean": mean_VM, "std": std_VM, "n": n}




	def sheets_excitatory_synaptic_conductance(self, sheets):
		"""Get the average excitatory synaptic conductance of the sheets"""
               
		ms = lambda a: (numpy.mean(a),numpy.std(a))
                population=[]
                mean=[]
                std=[]

                if type(sheets)== str:
                        mean_ECond, std_ECond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values)
                        n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids())
                        
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
                                population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
                                mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values))
                                std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values, ddof=1))
                        
			mean_ECond, std_ECond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values)
                        mean_ECond=numpy.mean(mean)
                        std_ECond=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

		return {"mean": mean_ECond, "std": std_ECond, "n": n}
	



	def sheets_inhibitory_synaptic_conductance(self, sheets):
		"""Get the average inhibitory synaptic conductance of the sheets"""
	
                ms = lambda a: (numpy.mean(a),numpy.std(a))
                population=[]
                mean=[]
                std=[]

                if type(sheets)== str:
                        mean_ICond, std_ICond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values)
                        n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids())
                        
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
                                population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
                                mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values))
                                std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values, ddof=1))
                        
                        mean_ICond, std_ICond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values)
                        mean_ICond=numpy.mean(mean)
                        std_ICond=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

		return {"mean": mean_ICond, "std": std_ICond, "n": n}

import sciunit

#==============================================================================

class SheetFiringRate(sciunit.Capability):
    """Get the average firing rate of the sheet"""

    def sheet_firing_rate(self, sheet):
        """Model should implement this method such as to retrieve the average firing rate of its sheet of neurons passed in input 
	   sheet should be a string specifying the name of the sheet
        """
        raise NotImplementedError()


class StatsSheetFiringRate(SheetFiringRate):
    """ Get descriptibe statistics about the distribution of the average firing rates of the sheet """

    def stats_sheet_firing_rate(self, sheet):
        """Model should implement this method such as to retrieve descriptive statistics about the distribution of 
	the average firing rates of its sheet of neurons passed in input 
	   sheet should be a string specifying the name of the sheet
	"""
	raise NotImplementedError()

class SheetsMembranePotential(sciunit.Capability):
    """Get the average resting membrane potential of the sheets"""

    def sheets_membrane_potential(self, sheets):
        """Model should implement this method such as to retrieve the resting membrane potential 
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsExcitatorySynapticConductance(sciunit.Capability):
    """Get the average excitatory synaptic conductance of the sheet"""

    def sheets_excitatory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the excitatory synaptic conductance 
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsInhibitorySynapticConductance(sciunit.Capability):
    """Get the average inhibitory synaptic conductance of the sheets"""

    def sheets_inhibitory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the inhibitory synaptic conductance
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheet
        """
        raise NotImplementedError()

class SheetCorrelationCoefficient(sciunit.Capability):
    """Get the correlation coefficient between the PSTH of all pair of neurons of the sheet"""

    def sheet_correlation_coefficient(self, sheets):
	""" Model should implement this method such as to retrieve the correlation coefficient
	    of its sheets of neurons passed in input
	    sheet should be a string specifying the name of the sheet
	"""
	raise NotImplementedError()

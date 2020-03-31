import sciunit

#==============================================================================

class SheetsFiringRate(sciunit.Capability):
    """Get the average firing rate of the sheets"""

    def sheets_firing_rate(self, sheets):
        """Model should implement this method such as to retrieve the average firing rate of its sheet of neurons passed in input 
	   sheets should be a string specifying the name of the sheets
        """
        raise NotImplementedError()



class SheetsMembranePotential(sciunit.Capability):
    """Get the average resting membrane potential of the sheets"""

    def sheets_membrane_potential(self, sheets):
        """Model should implement this method such as to retrieve the resting membrane potential 
	   of its sheet of neurons passed in input 
	   sheets should be a string specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsExcitatorySynapticConductance(sciunit.Capability):
    """Get the average excitatory synaptic conductance of the sheet"""

    def sheets__excitatory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the excitatory synaptic conductance 
	   of its sheet of neurons passed in input 
	   sheets should be a string specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsInhibitorySynapticConductance(sciunit.Capability):
    """Get the average inhibitory synaptic conductance of the sheets"""

    def sheets__inhibitory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the inhibitory synaptic conductance
	   of its sheet of neurons passed in input 
	   sheets should be a string specifying the name of the sheets
        """
        raise NotImplementedError()

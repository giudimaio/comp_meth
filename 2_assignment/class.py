import numpy
from matplotlib import pyplot as plt

class VoltageData:
	"""Class for managing a specific data set and for plotting
	"""
	
	def __init__(self, time, voltage):
		"""Initialize local arrays t and v
		"""
		t = numpy.array(time, dtype = numpy.float64)
		v = numpy.array(voltage, dtype = numpy.float64)
		"""self._data stacks the arrays time and voltage into columns and rows creating a matrix
		   with elements (i,j) in which i - j are a couple of time-value - voltage-value.
		"""
		self._data = numpy.column_stack([t, v])
	
	@property
	def times(self):
		"""This property is for giving access to user to data column time (see the syntax)
		"""
		return self._data[:,0]
	
	@property
	def voltages(self):
		"""This property is for giving access to user to data column voltage (see the syntax)
		"""
		return self._data[:,1]

	@voltages.setter
	def voltages(self, new_value):
		self._data = numpy.column_stack([self.times, new_value])
		
	@times.setter
	def times(self, new_value):
		self._data = numpy.column_stack([new_value, self.voltages])

	def __len__(self):
		return len(self._data)
		
	def __getitem__(self, index):
		"""Create the way to call arrays by using index
		"""
		return self._data[index]
	
	def __iter__(self):
		"""Call built-in function iter. This ensures the iterability of array
		"""
		return iter(self._data)
		
	def __str__(self):
		"""Write data rows by rows by using a list
		"""
		output_rows = []
		for i, entry in enumerate(self):
			output_rows.append('{:d}) {:f} {:f}'.format(i, entry[0], entry[1]))
		return '\n'.join(output_rows)

	def plot(self, ax = None, fmt='bo--', **kwargs):
		"""SYNTAX: None --> something undefined
				 fmt  --> format (from matplotlib) --> 'bo--' means \
				 blue/ball/dotted line
				 **kwargs --> whatever the user wants to add! (Only named \ 				 variables)
		"""
		if ax is not None:
			"""If the user pass an ax different from None -> set current ax 
			"""
			plt.sca(ax)
		else:
			plt.figure('voltages vs times')
		
		plt.plot(self.times, self.voltages, fmt, **kwargs)
		plt.xlabel('Time [s]')
		plt.ylabel('Voltage [mV]')
		plt.grid(True)
		"""Return -> get current axes
		"""
		return plt.gca()


if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will see in a future lesson."""
    # Load some data
    t, v = numpy.loadtxt('sample_data_file.txt', unpack=True)
    # Test the constructor
    v_data = VoltageData(t, v)
    # Test len(); ASSERT MEANS: "VERIFY THE FOLLOWING ASSERTION"
    assert len(v_data) == len(t)
    #print(len(v_data))
    
    #Test the setter
    #v_data.voltages = 3 * v
    #print(v_data.voltages)
    
    # Test the times attribute; NUMPY.ALL IS LIKE ALL, SO IT APPLIES THE FUNCTION \
    #          				  IN () TO ALL ELEMENTS OF ARRAY  
    assert numpy.all(v_data.voltages == v)
    # Test the voltages attribute
    assert numpy.all(v_data.times == t)
    
    # Print
    #print(v_data.times)
    #print(v_data.voltages)
    #print(v_data.voltages[0:4])

    # Test square parenthesis; SYNTAX MEANS: ELEMENT-3 OF COLUMN-1 (VOLTAGE)
    assert v_data[3, 1] == v[3]
    assert v_data[-1, 0] == t[-1]

    # Test slicing
    assert numpy.all(v_data[1:5, 1] == v[1:5])
    # Test iteration: i checks the position in t[] e v[], while update \
    # 			  entry for 0- and 1- column (t and v). REMEMBER:  \
    #			  ENUMERATE MAKES LOOP ON v_data
    for i, entry in enumerate(v_data):
        #print(entry)
        assert entry[0] == t[i]
        assert entry[1] == v[i]

    # Test printing
    #print(v_data)
    # Test plotting
    plt.figure('my_figure')
    plt.plot(t, v*v, 'r^', markersize=5, label='v_square')
    v_data.plot(plt.gca(), 'bo', markersize=5, label='normal v')
    plt.legend()
    plt.show()

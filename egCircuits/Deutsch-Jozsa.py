import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas
import seaborn as sns
import time

from Qsun.Qcircuit import *
from Qsun.Qgates import *
from Qsun.Qmeas import *


"""
Deutsch-Jozsa Constructer:
 - Builds the Deutsch-Jozsa algorithm around a quantum oracle that is provided as a keyword argument
"""


def deutsch_jozsa(circuit, oracle):
	"""
		Deutsch-Jozsa algorithm
		 - Inverts the nth qubit in the register
		 - Applies H gate to all qubits in the register
		 - Runs the oracle
		 - Applies H gate to all qubits except the nth

		Keyword Arguments:
			circuit -- Object of Qsun.Qcircuit.Qubit()
			oracle  -- Function which acts as the quantum oracle on the input circuit

		Returns:
			None
	"""
	n_qubit = len(circuit.state[0])
	X(circuit, n_qubit-1) # Invernt the nth qubit to |1>

	# Hadamard on all qubits
	for i in range(n_qubit):
		H(circuit, i)

	# Run the Oracle
	oracle(circuit)

	# Hadamard on all qubits except the last one.
	for i in range(n_qubit-1):
		H(circuit, i)


"""
Example Oracles
 - Each oracle is designed to ONLY apply their functions to the last qubit in the quantum register.
 - Each function accepts as input the circuit object you're working with and returns nothing
 - Functions do not pass register through H gates, that is handled in the deutsch_jozsa function
"""


def constant_one_oracle(circuit):
	"""
		Example Quantum Oracle: f(x) = 1
		 - Function returns 1 no matter what the input is

		Keyword Arguments:
			circuit -- Object of Qsun.Qcircuit.Qubit()

		Returns:
			None 		
	"""
	n_qubit = len(circuit.state[0])
	H(circuit, n_qubit-1) # Cancel the initial H gate.



def constant_zero_oracle(circuit):
	"""
		Example Quantum Oracle: f(x) = 0
		 - Function returns 0 no matter what the input is

		Keyword Arguments:
			circuit -- Object of Qsun.Qcircuit.Qubit()

		Returns:
			None 		
	"""
	n_qubit = len(circuit.state[0])
	H(circuit, n_qubit-1) # Cancel the initial H gate.
	X(circuit, n_qubit-1) # Set the nth qubit to |0>


def parity_oracle(circuit):
	"""
		Example Quantum Oracle: Odd Parity
		 - Function returns 1 if the number of set bits in the input string is odd
		 - This function does not pass quantum register through H gate before operating.

		Keyword Arguments:
			circuit -- Object of Qsun.Qcircuit.Qubit()

		Returns:
			None 		
	"""
	n_qubit = len(circuit.state[0])
	for i in range(n_qubit-1):
		CNOT(circuit, i, n_qubit-1)


"""
Main Function
"""

if __name__ == "__main__":

	print("\nConstant One\n")
	dj_circuit = Qubit(10)
	deutsch_jozsa(dj_circuit, constant_one_oracle)
	dj_circuit.visual_circuit()
	print(measure_all(dj_circuit, 5))

	print("\nConstant Zero\n")
	dj_circuit = Qubit(10)
	deutsch_jozsa(dj_circuit, constant_zero_oracle)
	dj_circuit.visual_circuit()
	print(measure_all(dj_circuit, 5))

	print("\nOdd Parity\n")
	dj_circuit = Qubit(10)
	deutsch_jozsa(dj_circuit, parity_oracle)
	dj_circuit.visual_circuit()
	print(measure_all(dj_circuit, 5))
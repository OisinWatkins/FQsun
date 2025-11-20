import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas
import seaborn as sns
import time

from Qsun.Qcircuit import *
from Qsun.Qgates import *
from Qsun.Qmeas import *


def deutsch_jozsa(circuit):

	n_qubit = len(circuit.state[0])

	X(circuit, n_qubit-1) # Invernt the nth qubit to |1>

	for i in range(n_qubit): # Hadamard on all qubits
		H(circuit, i)

	for i in range(n_qubit-1): # Example quantum oracle (parity check)
		CNOT(circuit, i, n_qubit-1)

	for i in range(n_qubit-1): # Hadamard on all qubits except the last one.
		H(circuit, i)

	return circuit


if __name__ == "__main__":
	circuit = Qubit(5)
	dj_circuit = deutsch_jozsa(circuit)
	dj_circuit.visual_circuit()
	print(measure_all(dj_circuit, 1))
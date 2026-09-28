from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Create a 2-qubit Grover circuit
qc = QuantumCircuit(2, 2)

# 1. Create superposition
qc.h(0)
qc.h(1)

# 2. Oracle: mark |11>
qc.cz(0, 1)

# 3. Diffusion operator
qc.h(0)
qc.h(1)

qc.x(0)
qc.x(1)

qc.h(1)
qc.cx(0, 1)
qc.h(1)

qc.x(0)
qc.x(1)

qc.h(0)
qc.h(1)

# 4. Measurement
qc.measure(0, 0)
qc.measure(1, 1)

# Display circuit
print(qc.draw())

# 5. Simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

# 6. Plot results
states = list(counts.keys())
values = list(counts.values())

plt.bar(states, values)
plt.xlabel("Measured State")
plt.ylabel("Number of Measurements")
plt.title("Grover's Algorithm Results")
plt.show()
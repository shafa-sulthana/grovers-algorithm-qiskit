# Grover's Algorithm using Qiskit

## Overview

This project implements Grover's quantum search algorithm using Python and Qiskit.

Grover's algorithm provides a quadratic speedup for searching an unsorted database compared with classical brute-force search in the quantum query model.

## Objective

To implement Grover's algorithm for searching a marked state in a 2-qubit search space.

The target state in this implementation is:

|11>

## Algorithm

The implementation consists of:

1. Initialization of quantum states
2. Superposition using Hadamard gates
3. Oracle to mark the target state |11>
4. Diffusion operator for amplitude amplification
5. Measurement
6. Simulation using Qiskit Aer

## Technologies Used

- Python
- Qiskit
- Qiskit Aer
- NumPy
- Matplotlib
- Google Colab

## Result

The circuit was simulated with 1024 shots.

Example result:

```text
{'11': 1024}

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Mon état
myState = "01"

# Créez les registres quantique et classique
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')

# Créez le circuit quantique
qc = QuantumCircuit(qr, cr)

# Porte Hadamard
qc.h(qr[0])

# Porte CNOT
qc.cx(qr[0], qr[1])

if myState == "00":
    # je ne fais rien
    pass
elif myState == "01":
    # Porte Z
    qc.z(qr[0])
elif myState == "10":
    # Porte X
    qc.x(qr[0])
elif myState == "11":
    # Porte X et Z
    qc.z(qr[0])
    qc.x(qr[0])
else:
    raise ValueError("L'état n'est pas reconnu")

# Porte CNOT
qc.cx(qr[0], qr[1])

# Porte Hadamard
qc.h(qr[0])

# Mesurez les qubits
qc.measure(qr, cr)

# Transpilez et assemblez le circuit pour le simulateur
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Exécutez le circuit
job = simulator.run(qobj)
result = job.result()

# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)
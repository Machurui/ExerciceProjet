from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Pas de temps souhaité
steps = 2

# Nombre qbits
n = 2

# Rotation de la porte RZ
rotate = 0.1

# Créez les registres quantique et classique
qr = QuantumRegister(n, 'q')
cr = ClassicalRegister(n, 'c')

# Créez le circuit quantique
qc = QuantumCircuit(qr, cr)

# Appliquez une porte Hadamard à chaque qubit
for i in range(n):
    # Porte Hadamard
    qc.h(i)
    
# Appliquez les étapes de la porte CX et RZ
for step in range(steps):
    for qubit in range(n):
        if qubit < n - 1:
            # Porte CX
            qc.cx(qubit, qubit + 1)
        
        # Porte RZ
        qc.rz(rotate, qubit)

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

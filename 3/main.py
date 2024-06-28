from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from matplotlib import pyplot as plt
import numpy as np

myValues = [2, 1]

myDoors = ["H", "X", "Y", "Z"]

# Créez les registres quantique et classique
qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')

# Créez le circuit quantique
qc = QuantumCircuit(qr, cr)

# Normalisez les valeurs
def prepare_arbitrary_state(a, b):   
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a = a / norm
    b = b / norm
    
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)
    
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    return qc

prepare_arbitrary_state(myValues[0], myValues[1])

# Affichez le vecteur d'état pour chaque porte
for myDoor in myDoors:
    if myDoor == "H":
        qc.h(0)
    elif myDoor == "X":
        qc.x(0)
    elif myDoor == "Y":
        qc.y(0)
    elif myDoor == "Z":
        qc.z(0)
    
    state = Statevector.from_instruction(qc)
    plot_bloch_multivector(state)
    plt.title(f"Après porte {myDoor}")
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

# gases
fluidos = ["Hydrogen", "Methane", "CarbonDioxide"]

T = 50 + 273.15
R = 8.314

p = np.linspace(1e5, 2e7, 200)

plt.figure(figsize=(7,5))

for fluido in fluidos:

    Z = []

    for P in p:
        rho = PropsSI('Dmolar','P',P,'T',T,fluido)
        Z_val = P/(rho*R*T)
        Z.append(Z_val)

    plt.plot(p/1e6, Z, linewidth=2, label=fluido)

plt.axhline(1, linestyle='--', label="Gás ideal")

plt.xlabel("Pressão (MPa)")
plt.ylabel("Z")
plt.title("Comparação do Fator de Compressibilidade")
plt.grid(True)
plt.legend()

plt.show()

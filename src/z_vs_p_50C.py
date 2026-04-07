import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

# fluido
fluido = "Hydrogen"

# temperatura (50 °C em Kelvin)
T = 50 + 273.15

# constante dos gases
R = 8.314

# vetor de pressões (Pa)
p = np.linspace(1e5, 2e7, 200)

Z = []

for P in p:

    rho = PropsSI('Dmolar', 'P', P, 'T', T, fluido)

    Z_val = P/(rho*R*T)

    Z.append(Z_val)

Z = np.array(Z)

plt.figure(figsize=(7,5))

plt.plot(p/1e6, Z, linewidth=2, label="H₂ (50°C)")
plt.axhline(1, linestyle='--', label="Gás ideal")

plt.xlabel("Pressão (MPa)")
plt.ylabel("Fator de compressibilidade Z")

plt.title("Z(p) para Hidrogênio a 50°C")

plt.grid(True)
plt.legend()

plt.show()

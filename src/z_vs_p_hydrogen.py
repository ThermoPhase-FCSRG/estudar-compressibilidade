import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

fluido = "Hydrogen"

# temperaturas em Celsius
temperaturas = [0, 50, 100]

# constante dos gases
R = 8.314

# vetor de pressão
p = np.linspace(1e5, 2e7, 200)

plt.figure(figsize=(7,5))

for Tc in temperaturas:

    T = Tc + 273.15
    Z = []

    for P in p:
        rho = PropsSI('Dmolar','P',P,'T',T,fluido)
        Z_val = P/(rho*R*T)
        Z.append(Z_val)

    plt.plot(p/1e6, Z, linewidth=2, label=f"{Tc} °C")

plt.axhline(1, linestyle='--', label="Gás ideal")

plt.xlabel("Pressão (MPa)")
plt.ylabel("Z")
plt.title("Fator de Compressibilidade do Hidrogênio")
plt.grid(True)
plt.legend()

plt.show()

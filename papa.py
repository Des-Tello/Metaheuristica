import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Crear datos de ejemplo
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Crear un mapa de colores degradado
color_map = LinearSegmentedColormap.from_list('ColorMap', ['red', 'yellow', 'green'])

fig, ax = plt.subplots()

for i in range(len(x) - 1):
    color = color_map(i / (len(x) - 1))  # Interpolación del color
    ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color=color, linewidth=2)

ax.set_title('Mejora por movimiento')
ax.set_xlabel('Movimiento')
ax.set_ylabel('Valor FO')

ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

# Anotaciones para cada punto en el gráfico
for i, tup in enumerate(zip(x, y)):
    ax.annotate(f'({tup[0]:.2f}, {tup[1]:.2f})', (tup[0], tup[1]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.show()
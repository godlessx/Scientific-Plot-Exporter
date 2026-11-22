import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

fig, ax = plt.subplots(4, 1, figsize=(10, 8))

ax[0].plot(x, y1, label="sin(x)")
ax[1].plot(x, y2, label="cos(x)")
ax[2].plot(x, y3, label="tan(x)")
ax[3].plot(x, y4, label="exp(-x)")

ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[3].grid()

ax[0].legend(loc="lower left")
ax[1].legend(loc="lower left")
ax[2].legend(loc="lower left")
ax[3].legend(loc="lower left")

titles = ["Sine", "Cosine", "Tangent", "Exponential"]

for i in range(4):
    ax[i].set_title(titles[i])
    ax[i].set_xlabel("Angle (radians)")
    ax[i].set_ylabel("Amplitude")
    
fig.tight_layout()

fig.savefig("graphs.png", dpi=300, bbox_inches="tight")

plt.show()
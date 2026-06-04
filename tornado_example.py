"""Example tornado (sensitivity) chart — bars span low-case to high-case NPV."""

import matplotlib.pyplot as plt

base = 10.0  # Base-case NPV ($M)

# (label, NPV when input is low, NPV when input is high)
variables = [
    ("Unit price", 7.2, 12.8),
    ("Volume", 8.1, 11.6),
    ("Raw material cost", 11.4, 8.9),  # cost down → NPV up
    ("Labor rate", 10.6, 9.4),
    ("Discount rate", 11.1, 9.1),
]

variables.sort(key=lambda x: abs(x[2] - x[1]), reverse=True)

fig, ax = plt.subplots(figsize=(8, 5))

for i, (label, low, high) in enumerate(variables):
    lo, hi = min(low, high), max(low, high)
    if base <= hi and base >= lo:
        ax.barh(i, base - lo, left=lo, height=0.55, color="#4C78A8", align="center")
        ax.barh(i, hi - base, left=base, height=0.55, color="#F58518", align="center")
    else:
        ax.barh(i, hi - lo, left=lo, height=0.55, color="#9ECAE9", align="center")

ax.axvline(base, color="black", linewidth=1.2, linestyle="--")
ax.set_yticks(range(len(variables)))
ax.set_yticklabels([v[0] for v in variables])
ax.invert_yaxis()
ax.set_xlabel("NPV ($M)")
ax.set_title("Tornado chart — which inputs move NPV the most?")
ax.plot([], [], color="#4C78A8", linewidth=8, label="Toward low-case input")
ax.plot([], [], color="#F58518", linewidth=8, label="Toward high-case input")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("/workspace/tornado_chart_example.png", dpi=120)
print("Saved tornado_chart_example.png")

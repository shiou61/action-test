import numpy as np
from datetime import datetime

rng = np.random.default_rng(0)

filename = f"./logs/{datetime.now()}.txt"

with open(filename, "w") as f:
    f.write(rng.integers(1, 100, 100))

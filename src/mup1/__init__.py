from PyMPDATA import options, ScalarField, VectorField
from PyMPDATA.boundary_conditions import Periodic
import numpy as np
from matplotlib import pyplot as plt

def main() -> None:
    opt = options.Options()
    common = {
            "halo": opt.n_halo,
            "boundary_conditions": (Periodic(),),
            }
    advectee = ScalarField(**common, data=np.exp(-(x := np.linspace(-2, 8, 41))**2))
    advector = VectorField(**common, data=(np.full(shape=x.size+1, fill_value=.25),))
    
    fig, ax = plt.subplots()
    ax.step(x, advectee.get())

    fig.savefig("drawing.svg", format='svg')
    plt.close(fig)

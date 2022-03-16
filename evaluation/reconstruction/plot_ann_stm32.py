# -*- coding: utf-8 -*-
"""
    np.savez("stm32_eval_%s_%s_%d.npz"%(time.strftime("%Y%m%d_%H%M%S"), noise_str, TEST_SIZE),
             reco_params=reco_params,
             gene_params=gene_params
             )
    """
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import scipy.stats

def plot_ann_stm32(filename):
    npz = np.load(filename)

    gene_params = npz["gene_params"]
    reco_params = npz["reco_params"]

    fig, ax = plt.subplots()
    plt.title("width")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")

    x = [ float(i[0]) for i in gene_params ]
    y = [ float(i[0]) for i in reco_params ]

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    print(r, p)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.colorbar()
    plt.savefig("stm32_validation_width.png")
    plt.show()

#############################################################

    fig, ax = plt.subplots()
    plt.title("position")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")

    x = [ float(i[1]) for i in gene_params ]
    y = [ float(i[1]) for i in reco_params ]

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    print(r, p)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.colorbar()
    plt.savefig("stm32_validation_position.png")
    plt.show()

#############################################################

    fig, ax = plt.subplots()
    plt.title("height")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")

    x = [ float(i[2]) for i in gene_params ]
    y = [ float(i[2]) for i in reco_params ]

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    print(r, p)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.colorbar()
    plt.savefig("stm32_validation_height.png")
    plt.show()


if __name__ == "__main__":
    #plot_ann_stm32("stm32_eval_20220316_152113_noise_10000.npz")
    plot_ann_stm32("stm32_eval_20220316_153028_quiet_10000.npz")

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import scipy.odr
from scipy.optimize import curve_fit

def plot_ann_stm32(filename):
    npz = np.load(filename)

    gene_params = npz["gene_params"]
    reco_params = npz["reco_params"]

    def Fodr(B, x):
        '''Linear function y = m*x + b'''
        # B is a vector of the parameters.
        # x is an array of the current x values.
        # x is in the same format as the x passed to Data or RealData.
        #
        # Return an array in the same format as y passed to Data or RealData.
        return B[0]*x + B[1]

    def Fcurve_fit(x, m, b):
        return m*x + b

    linear = scipy.odr.Model(Fodr)

    fig, ax = plt.subplots()
    plt.title("width")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")

    x = [ float(i[0]) for i in gene_params ]
    y = [ float(i[0]) for i in reco_params ]

    mydata = scipy.odr.RealData(x, y)
    myodr = scipy.odr.ODR(mydata, linear, beta0=[1., 1.])
    myoutput = myodr.run()
    beta = myoutput.beta
    beta_sd = myoutput.sd_beta

    popt, pcov = curve_fit(Fcurve_fit, x, y)
    beta      = popt
    beta_sd = np.sqrt(np.diagonal(pcov))

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$\mathrm{slope} = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$\mathrm{offset} = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

    X = np.linspace(np.min(x),np.max(x), 100)
    plt.plot( X, beta[0]*X + beta[1], 'r')

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

    mydata = scipy.odr.RealData(x, y)
    myodr = scipy.odr.ODR(mydata, linear, beta0=[1., 1.])
    myoutput = myodr.run()
    beta = myoutput.beta
    beta_sd = myoutput.sd_beta

    popt, pcov = curve_fit(Fcurve_fit, x, y)
    beta      = popt
    beta_sd = np.sqrt(np.diagonal(pcov))

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$\mathrm{slope} = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$\mathrm{offset} = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

    X = np.linspace(np.min(x),np.max(x), 100)
    plt.plot( X, beta[0]*X + beta[1], 'r')

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

    mydata = scipy.odr.RealData(x, y)
    myodr = scipy.odr.ODR(mydata, linear, beta0=[1., 1.])
    myoutput = myodr.run()
    beta = myoutput.beta
    beta_sd = myoutput.sd_beta

    popt, pcov = curve_fit(Fcurve_fit, x, y)
    beta      = popt
    beta_sd = np.sqrt(np.diagonal(pcov))

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$\mathrm{slope} = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$\mathrm{offset} = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

    X = np.linspace(np.min(x),np.max(x), 100)
    plt.plot( X, beta[0]*X + beta[1], 'r')

    plt.colorbar()
    plt.savefig("stm32_validation_height.png")
    plt.show()


if __name__ == "__main__":
    #plot_ann_stm32("stm32_eval_20220316_152113_noise_10000.npz")
    #plot_ann_stm32("stm32_eval_20220316_153028_quiet_10000.npz")
    #plot_ann_stm32("stm32_eval_20220316_182456_noise_1LSB_10000.npz")

    # new ANN v0.3
    plot_ann_stm32("stm32_eval_20220317_121051_quiet_10000.npz")
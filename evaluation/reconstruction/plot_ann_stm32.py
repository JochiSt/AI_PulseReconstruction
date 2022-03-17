# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import scipy.odr

def plot_ann_stm32(filename):
    npz = np.load(filename)

    gene_params = npz["gene_params"]
    reco_params = npz["reco_params"]

    def f(B, x):
        '''Linear function y = m*x + b'''
        # B is a vector of the parameters.
        # x is an array of the current x values.
        # x is in the same format as the x passed to Data or RealData.
        #
        # Return an array in the same format as y passed to Data or RealData.
        return B[0]*x + B[1]
    linear = scipy.odr.Model(f)

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

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$slope = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$offset = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

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

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$slope = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$offset = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

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

    plt.hist2d( x, y,  bins=32, cmin=1, cmap='summer')
    r, p = scipy.stats.pearsonr(x, y)
    plt.text( 0.05, 0.9,  "correlation %4.2f %%"%(r * 100), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.05, 0.8,   r"$slope = %4.3f \pm %4.3f$"%(beta[0], beta_sd[0]), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.74, r"$offset = %4.3f \pm %4.3f$"%(beta[1], beta_sd[1]), ha='left', va='center', transform=ax.transAxes )

    X = np.linspace(np.min(x),np.max(x), 100)
    plt.plot( X, beta[0]*X + beta[1], 'r')

    plt.colorbar()
    plt.savefig("stm32_validation_height.png")
    plt.show()


if __name__ == "__main__":
    #plot_ann_stm32("stm32_eval_20220316_152113_noise_10000.npz")
    plot_ann_stm32("stm32_eval_20220316_153028_quiet_10000.npz")
    #plot_ann_stm32("stm32_eval_20220316_182456_noise_1LSB_10000.npz")
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats

def analyse_pulse_width(vcd_files):

    duration = []

    for vcd_filename in vcd_files:
        with open(vcd_filename) as f:
            lines = f.readlines()
            old_level = -1
            old_timestamp = 0
            timescale = 0

            for line in lines:
                line = line[:-1]
                if "$timescale" in line:
                    line = line.replace('$timescale', '').replace('$end', '')
                    line = line.replace('ps', 'e-12')
                    line = line.replace('ns', 'e-9')
                    line = line.replace('ms', 'e-3')
                    line = line.replace(' ', '')
                    timescale = float(line)
                elif line[0] is '#':
                    line = line[1:]
                    line = line.replace('!','')
                    try:
                        timestamp, level = line.split(' ')
                        timestamp = int(timestamp)
                        level = int(level)
                    except:
                        continue

                    if level != old_level:
                        if level == 0 and old_level == 1:     # we are interested in the duration of the high
                                                                            # signal
                            deltaT = (timestamp - old_timestamp)*timescale*1e6 # in us
                            duration.append( deltaT )

                        old_timestamp = timestamp
                        old_level = level

    duration = np.array(duration)

    mean_duration = np.mean(duration)
    std_duration = np.std(duration)

    fig, ax = plt.subplots()

    hist_range = [mean_duration-5*std_duration, mean_duration+5*std_duration]
    delta_hist_range = hist_range[1]-hist_range[0]
    hist_bins = int( np.round( delta_hist_range*1e-6 / (1. / 12E6), 0))    # assume 12MHz sampling
    bin_width = delta_hist_range / hist_bins * 1000

    """
    print("Histogram range:", np.round(delta_hist_range, 2), "us")
    print("Bins:", hist_bins)
    print("bin width", np.round(bin_width, 2) , "ns")
    print("bin frequency", np.round( 1/(bin_width*1e-9) / 1e6, 3) , "MHz")
    """

    biny, binx, _ = plt.hist(duration, bins=hist_bins,
                             range=hist_range )

    x = np.linspace(binx.min(), binx.max(), 100)
    plt.plot(x, stats.norm.pdf(x, mean_duration, std_duration) * np.max(biny) )

    plt.text( 0.05, 0.90,  r'N = %d'%(len(duration)), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.84,  r'$\Delta T =%6.2f \pm %6.2f \, \mu \mathrm{s}$'%(mean_duration, std_duration), ha='left', va='center', transform=ax.transAxes )

    plt.text( 0.95, 0.90,  r'$\Delta_\mathrm{bin} =%4.2f \, \mathrm{ns}$'%(bin_width), ha='right', va='center', transform=ax.transAxes )

    mean_freq = 1/(mean_duration*1e-6)
    std_freq     = 1/(mean_duration*1e-6)**2 * std_duration*1e-6

    plt.text( 0.05, 0.78,  r'$f =%6.2f \pm %6.2f \, \mathrm{Hz}$'%(mean_freq, std_freq), ha='left', va='center', transform=ax.transAxes )

    plt.title("ANN runtime on STM32")
    plt.ylabel("entries")
    plt.xlabel("ANN execution time / us")
    plt.savefig("ANNexecutionTime.png")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    analyse_pulse_width([
            "timing_1.vcd",
            "timing_2.vcd",
            "timing_3.vcd",
            "timing_4.vcd",
            "timing_5.vcd",
            ])

    analyse_pulse_width([
            "timing_0.3_1.vcd",
            "timing_0.3_2.vcd",
            "timing_0.3_3.vcd",
            ])
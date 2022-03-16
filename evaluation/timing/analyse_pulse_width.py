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
    biny, binx, _ = plt.hist(duration, bins=100, range=(630, 650) )

    x = np.linspace(binx.min(), binx.max(), 100)
    plt.plot(x, stats.norm.pdf(x, mean_duration, std_duration)*biny.max() )

    plt.text( 0.05, 0.90,  r'N = %d'%(len(duration)), ha='left', va='center', transform=ax.transAxes )
    plt.text( 0.05, 0.84,  r'$\Delta T =%6.2f \pm %6.2f \, \mu s$'%(mean_duration, std_duration), ha='left', va='center', transform=ax.transAxes )

    mean_freq = 1/(mean_duration*1e-6)
    std_freq     = 1/(mean_duration*1e-6)**2 * std_duration*1e-6

    plt.text( 0.05, 0.78,  r'$f =%6.2f \pm %6.2f \, Hz$'%(mean_freq, std_freq), ha='left', va='center', transform=ax.transAxes )

    plt.title("ANN runtime on STM32")
    plt.ylabel("entries")
    plt.xlabel("ANN execution time / us")
    plt.savefig("ANNexecutionTime.png")
    plt.show()


if __name__ == "__main__":
    analyse_pulse_width([
            "timing_1.vcd",
            "timing_2.vcd",
            "timing_3.vcd",
            ]
    )

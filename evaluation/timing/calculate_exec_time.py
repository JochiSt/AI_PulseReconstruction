import numpy as np

def calc_exec_time(MACC, FCPU, cortex="M4"):
#    FCPU in MHz
    if "M4" in cortex:
        # 9 cycles per MACC
        return MACC * 9 / (FCPU*1e6)  * 1e6 # in us
    elif "M7" in cortex:
        # 6 cycles per MACC
        return MACC * 6 / (FCPU*1e6) * 1e6  # in us
    else:
        return None

if __name__ == "__main__":

    macc = 11395
    measured = 638.95
    macctime = calc_exec_time(macc, 170)
    print("rev 0.2:\t", np.round(macctime,2), "\t", measured, "\t", np.round(measured-macctime,2))

    macc = 10548
    measured = 633.06
    macctime = calc_exec_time(macc, 170)
    print("rev 0.3:\t", np.round(macctime,2), "\t", measured, "\t", np.round(measured-macctime,2))

    macc = 10291
    measured = 613.39
    macctime = calc_exec_time(macc, 170)
    print("rev 0.4:\t", np.round(macctime,2), "\t", measured, "\t", np.round(measured-macctime,2))

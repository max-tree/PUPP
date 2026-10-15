'''
EM_Emitter_Receiver_Evaluation.py
Maxwell Tree
Sep 25, 2026

This has functions used to plot data from the LabVIEW as well as evaluate the Electromagnetic wave emitter/receiver
(EMER) sensor for use in pressure ulcer prevention.
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from GenericFunctions import *


def plot_EMER():
    files = get_files(type="lvm")
    for file in files:
        print("FILE: ", file.name.split('/')[-1])
        df = pd.read_csv(file, sep="\t", skiprows=22)
        time = df['Time'].to_numpy()
        Vout = df['Vout'].to_numpy()

        # create_xy_scatter_plot(time, Vout, "Time (s)", "Voltage (V)" , file.name.split('/')[-1])
        create_xy_plot(time, Vout, "Time (s)", "Voltage (V)" , file.name.split('/')[-1])

    plt.show()
    return


def main():
    print("Hello EM World")
    plot_EMER()
    # calculate_balance_inductor()


if __name__ == "__main__":
    main()

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
from scipy.fft import fft, fftfreq

from GenericFunctions import *


def plot_EMER():
    files = get_files(type="lvm")
    for file in files:
        print("FILE: ", file.name.split('/')[-1])
        df = pd.read_csv(file, sep="\t", skiprows=22)
        time = df['Time'].to_numpy()
        Vout = df['Vout'].to_numpy()

        # create_xy_scatter_plot(time, Vout, "Time (s)", "Voltage (V)" , file.name.split('/')[-1])
        create_xy_plot(time, Vout, "k", "Time (s)", "Voltage (V)" , file.name.split('/')[-1])

    plt.show()
    return


def plot_EMER_FFT():
    files = get_files(type="lvm")
    for file in files:
        print("FILE: ", file.name.split('/')[-1])
        df = pd.read_csv(file, sep="\t", skiprows=22)
        time = df['Time'].to_numpy()
        Vout = df['Vout'].to_numpy()

        # create_xy_scatter_plot(time, Vout, "Time (s)", "Voltage (V)" , file.name.split('/')[-1])
        create_xy_plot(time, Vout, "k", "Time (s)", "Voltage (V)" , file.name.split('/')[-1] + " Reduce Data to Red")  # plot all

        # Manually cut the data down to when I am laying still
        # startIndex = 900  # WeightPredictionLayingDown_x_68p8_3__10-23-2026_2-59-PM.lvm
        # endIndex = 1990
        # startIndex = 450  # WeightPredictionLayingDown_x_68p8_1__10-23-2026_2-49-PM.lvm
        # endIndex = 1500
        startIndex = 0  # HeartBeat_againstChest_1__10-26-2026_3-49-PM.lvm
        endIndex = -1
        create_xy_plot(time[startIndex:endIndex], Vout[startIndex:endIndex], "r", "Time (s)", "Voltage (V)" , file.name.split('/')[-1]+ " Reduce Data to Red")  # plot cuts

        signal = Vout[startIndex:endIndex]
        fft_signal = fft(signal)
        sampling_interval_in_sec = time[startIndex+1] - time[startIndex]
        freqs = fftfreq(len(signal), sampling_interval_in_sec)
        # Plot only the positive frequencies
        half_len = len(fft_signal) // 2
        plt.figure(figsize=(10, 4))
        plt.plot(freqs[:half_len], np.abs(fft_signal[:half_len]), 'b-', linewidth=1)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.title('FFT Spectrum of Signal')
        plt.grid(True)
    plt.show()


def main():
    print("Hello EM World")
    plot_EMER()
    # plot_EMER_FFT()  # meant for laying down data or at least involves a body of some kind.

if __name__ == "__main__":
    main()

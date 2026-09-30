'''
PiezoelectricDiskEvaluation.py
Maxwell Tree
Sep 25, 2026

This has functions used to plot data from the spectrum analyzer (Agilent 4395A) as well as evaluate the piezoelectric
disk sensors for use in pressure ulcer prevention.
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from GenericFunctions import get_files


def create_Agilent_plot(x, y, yName, file):
    fileName = file.name.split('/')[-1]
    plt.figure("File " + fileName + ". " + yName)
    plt.plot(x, y)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel(yName +' (dB)')


def plot_Agient_4395A():
    files = get_files(type="TXT")
    for file in files:
        print("FILE: ", file.name.split('/')[-1])
        df = pd.read_csv(file, sep="\t", skiprows=14)
        freq = df['Frequency'].to_numpy()
        dtr = df['Data Trace Real'].to_numpy()
        dti = df['Data Trace Imag'].to_numpy()
        mtr = df['Memory Trace Real'].to_numpy()  # Real values saved to memory. This is usuallya spectrum analysis put into memory for estalbishing a baseline.
        mti = df['Memory Trace Imag'].to_numpy()

        create_Agilent_plot(freq, dtr, "Data Trace Real", file)
        # create_Agilent_plot(freq, dti, "Data Trace Imag", file)
        # create_Agilent_plot(freq, mtr, "Memory Trace Real", file)
        # create_Agilent_plot(freq, mti, "Memory Trace Imag", file)

        # Extract important points
        print("Peak amplitude of Data Trace Real = ", np.min(dtr), " dB")
        print("Frequency at peak amplitude of Data Trace Real = ", freq[np.argmin(dtr)], " Hz")
    plt.show()
    return


def calculate_balance_inductor():
    # This function assumes you know the base capacitance of the system the frequency of resonance.
    C = 17.4*10**-9  # F
    f = 5248.0  # Hz. The frequency at which resonance occurs.
    # From Physics for engineers and scientists by Serway and Jewett page 1013, we see how to improve the resonance
    # which is that we need to cancel out the reactance terms.
    omega = 2.0*np.pi*f
    Xc = 1.0/(omega*C)
    # We know Xl = omega*L and we want Xc=Xl, solving for L:
    L = 1.0/(omega**2*C)
    print("You need a " , L, " H inductor to balance the capacitor " , C, " F at ", f, " Hz")

def main():
    print("Hello Piezoelectric World")
    # plot_Agient_4395A()
    calculate_balance_inductor()


if __name__ == "__main__":
    main()

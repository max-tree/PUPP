'''
PiezoelectricDiskEvaluation.py
Maxwell Tree
Sep 25, 2026

This has functions used to plot data from the spectrum analyzer (Agilent 4395A) as well as evaluate the piezoelectric
disk sensors for use in pressure ulcer prevention.
'''
import matplotlib.pyplot as plt
import pandas as pd

from GenericFunctions import get_files


def plot_Agient_4395A():
    files = get_files(type="TXT")
    for file in files:
        # print(file.name)
        df = pd.read_csv(file, sep="\t", skiprows=14)
        freq = df['Frequency'].to_numpy()
        dtr = df['Data Trace Real'].to_numpy()
        dti = df['Data Trace Imag'].to_numpy()
        mtr = df['Memory Trace Real'].to_numpy()
        mti = df['Memory Trace Imag'].to_numpy()

        fileName = file.name.split('/')[-1]
        plt.figure(fileName)
        plt.plot(freq, dtr)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Data Trace Real (dB)')
        # plt.plot(freq, dti)
        # plt.plot(freq, mtr)
    plt.show()
    return


def main():
    print("Hello Piezoelectric World")
    plot_Agient_4395A()
    # calculate_balance_inductor()


if __name__ == "__main__":
    main()

'''
SmartfoamEvaluation.py
Pressure Ulcer Prevention Project (PUPP)
Maxwell Tree
Dr. Azar

Creation Date: Sep 18, 2026

This code contains the following functions:

1. Calcualte the ideal resistance for a capacitive sensor circuit. This is based on my derivation from Sep 16, 2026.
    Please see the derivation papers for details of derivation. This code is for general capacitive pressure sensor use.
'''

def calc_R_for_cap_sense():
    # This function calculates the resistor required for a switching LPF capacitance measurement circuit like
    # that found in Serway and Jewett's Physics for scientists and engineers page 848.
    ####### User defined variables ########
    fs = 1.0 * 10**5  # Hz. Sampling frequency
    Cmin = 36.0 * 10**-12  # F. min capcitance expected
    Cmax = 70.0 * 10**-12  # F. max capcitance expected
    Res = 1.0  # %. Desired resolution
    #######################################
    Res = Res / 100.0

    R = 1.0/(fs*Res*(Cmax-Cmin))  # ohm
    print("R = ", R, "Ω")
    print("R = ", R/10**6, "MΩ")

    return


def main():
    print("Hello World")
    calc_R_for_cap_sense()

if __name__ == "__main__":
    main()

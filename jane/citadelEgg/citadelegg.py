""" 
contracts:
1000 flat
500 or 1500
N(1000, 150)
Uniform 500 to 1500

predictions:
small variance in contract = mean EQ low
higher variance in contract =
    mean EQ even lower, but variance is higher (more right skewed)
"""

import numpy as np

def convolve_pdf_n_times(p, n):
    """
    Convolve the discrete pdf `p` with itself `n` times (i.i.d. sum),
    using FFT-based polynomial exponentiation.

    Returns a 1D NumPy array of length len_out = n*(len(p)-1) + 1,
    which is the pmf of the sum of `n` i.i.d. random variables with pmf p.
    """
    # Length of the original pmf
    M = len(p)
    
    # Output length needed to hold n-fold convolution without wrap-around
    out_len = n*(M-1) + 1
    
    # Next power-of-two (or just next convenient length) for FFT
    # This helps FFT efficiency
    fft_len = 1
    while fft_len < out_len:
        fft_len <<= 1  # multiply by 2
    
    # Zero-pad p to length fft_len
    p_padded = np.zeros(fft_len, dtype=np.float64)
    p_padded[:M] = p
    
    # FFT
    P = np.fft.fft(p_padded)
    
    # Raise to the n-th power, elementwise
    Pn = P ** n
    
    # Inverse FFT
    # The result should be real, but we'll take np.real_if_close just in case
    conv_n = np.fft.ifft(Pn)
    conv_n = np.real_if_close(conv_n, tol=1e5)
    
    # Now conv_n has length fft_len, but we only need the first out_len samples
    conv_n = conv_n[:out_len]
    
    return conv_n

res = convolve_pdf_n_times([0.5, 0.5], 2)
print(res)
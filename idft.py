from sympy import symbols, sin, cos, pi, simplify
from cmath import sqrt
from math import floor

j = sqrt(-1)

#helper method to get time domain sinusoid at the column k in frequency spectrum
def _get_sinusoids_at_k(freq_spectrum, k, N, n):
    w = 2 * k * pi / N
    coeff_k = freq_spectrum[k]
    coeff_k_conj = freq_spectrum[N - k]

    sinusoid_k = 0
    sinusoid_conj_k = 0
    if (w != pi) & (w != 2*pi) & (w != 0):
        sinusoid_k += (j * sin(w*n)) #case where sin component isn't 0
        sinusoid_conj_k += (-j * sin(w*n))

    sinusoid_k += cos(w*n)
    sinusoid_conj_k += cos(w*n)

    return (coeff_k * sinusoid_k, coeff_k_conj * sinusoid_conj_k)

#returns a time domain sinusoid from the freq_spectrum
#this sinusoid could be an alias of the actual sinusoid
#i haven't had time to implement a way to find the correct frequency based on user given criteria yet
def idft(freq_spectrum):
    
    N = len(freq_spectrum)
    n = symbols('n')

    sinusoid_sum = freq_spectrum[0]
   
    k = 1
    while k < floor(N/2):
        sinusoids_at_k = _get_sinusoids_at_k(freq_spectrum, k, N, n)
        sinusoid_sum += sinusoids_at_k[0] + sinusoids_at_k[1]
        k += 1

    if N%2 == 0:
        sinusoid_sum += (freq_spectrum[int(N/2)] * cos(pi*n))
    else:
        sinusoids_at_k_middle = _get_sinusoids_at_k(freq_spectrum, floor(N/2), N, n)
        sinusoid_sum += sinusoids_at_k_middle[0] + sinusoids_at_k_middle[1]

    return simplify(sinusoid_sum/N)

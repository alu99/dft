from dft import dft, graph_freq_spectrum
from idft import idft
from cmath import pi

cos_pi = [1,-1,1,-1,1,-1,1,-1]
sin_pi_2 = [0,1,0,-1]

S = dft(sin_pi_2)
print(S)
print(idft(S))
graph_freq_spectrum(S)

S = dft(cos_pi)
print(S)
print(idft(S))
graph_freq_spectrum(S)

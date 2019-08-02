# dft
Discrete Fourier Transform

In my sophomore year of college, I took 2 semesters of signal theory classes. I found that it was really easy to forget the concepts that I learned if not actively working with them. I created Python versions of the DFT and inverse DFT algorithms to brush up on the concept of DFT.

## dft.py

`def dft(input)`: Function to calculate frequency spectrum, S, from time domain array `input`. Based on the formula `S = V^H * s`, where `S` is frequency spectrum, `V^H` is hermitian of the DFT matrix, and `s` is `input`

`def graph_freq_spectrum(freq_spectrum)`: Function to graph frequency spectrum. Implemented using `plotly` Python library

## idft.py

`def idft(freq_spectrum)`: Function that converts frequency spectrum into a time domain sinusoid. Use `sympy` Python libary to model symbolic equations. As of now, it's only capable of providing an alias of the original function. I haven't had time to implement a way to find the correct frequency based on user given criteria yet.

## demo.py

Demonstrates above functions with simple examples of `y=cos(pi*n)` and `y=sin(pi/2*n)`

### Outputs of y=cos(pi*n) demo
frequency spectrum (calculated using `dft()`): [0, 0, 0, 0, 8.0, 0, 0, 0]  
original function (calculated using `idft()`): 1.0*cos(pi*n) (could be an alias)  
graph of frequency spectrum: ![image](https://user-images.githubusercontent.com/13570258/62342592-66e6e900-b4b5-11e9-860a-236bf25bc3eb.png)

### Outputs of y=sin(pi/2*n) demo
frequency spectrum (calculated using `dft()`): [0, -2j, 0, 2j]  
original function (calculated using `idft()`): sin(pi*n/2)  
graph of frequency spectrum: ![image](https://user-images.githubusercontent.com/13570258/62342270-44080500-b4b4-11e9-964b-3e29cc865fba.png)






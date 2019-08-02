import math
import cmath
import plotly.graph_objects as go

j = cmath.sqrt(-1)

def dft(input):
    N = len(input)

    dft_output = [] #dft output aligning to each value of k

    ## S = V^H * s, where S is frequency spectrum, V^H is hermitian of the DFT matrix, and s is the input in time domain
    ##
    ## V is an N x N (where N is length of input array) matrix where each column k represents a complex sinusoid
    ## modelled by e^(jwn) where w is the frequency represented by w = 2*k*pi/N and n is the input's index

    ##creates nth_fourier_freq for each column k and multiplies it by the time value at n
    for k in range(N):
        dft_output_k = 0

        for n in range(N):
            w = 2 * k * cmath.pi/ N
            nth_fourier_freq = cmath.exp(j*w*n) #e^(jwn)
            
            #calculates conjugate of nth_fourier_freq to obtain the hermitian form of the matrix
            nth_fourier_freq = nth_fourier_freq.real + nth_fourier_freq.imag * -j
            dft_output_k += (nth_fourier_freq * input[n])

        rounded_output_real = round(dft_output_k.real, 5)
        rounded_output_imag = round(dft_output_k.imag, 5)

        if abs(dft_output_k.real) < 1e-10:
            rounded_output_real = 0
        if abs(dft_output_k.imag) < 1e-10:
            rounded_output_imag = 0
        dft_output.append((rounded_output_real + (rounded_output_imag * j if rounded_output_imag != 0 else 0)))
            
    return dft_output

def graph_freq_spectrum(freq_spectrum):
    
    x_axis = [] #array of 0....N-1, labels the k index of the frequency spectrum in the bar graph below
    for k in range(len(freq_spectrum)):
        x_axis.append(k)

    ##cannot plot complex numbers on a bar graph, convert to real modulus of number
    spectrum_converted_real = []
    for i in range(len(freq_spectrum)):
        spectrum_converted_real.append(math.sqrt((freq_spectrum[i].real)**2 + (freq_spectrum[i].imag)**2))

    ##creates a plots bar graph representing the frequency spectrum
    fig = go.Figure()
    bar_graph = go.Bar(
        x = x_axis,
        y = spectrum_converted_real,
        dx=1,
        hovertext = freq_spectrum,
        hoverinfo = 'text',
    )

    fig.add_trace(bar_graph)

    fig.update_layout(
        title=go.layout.Title(
            text="Spectrum of Input Sample",
            xref="paper",
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="k",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            ),
            dtick=1
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            )
        )
    )
    fig.show()

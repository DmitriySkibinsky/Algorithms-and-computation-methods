import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def fft(x):
    N = len(x)
    if N == 1:
        return x
    else:
        even = fft(x[0::2])
        odd = fft(x[1::2])
        T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + \
               [even[k] - T[k] for k in range(N // 2)]

# Create an array of complex numbers
x = [complex(i, 0) for i in [4, 8, 2, 5, 2, 4, 1, 0, 10 ]]

# Making FFT
X = fft(x)

# Print results
print(X)

# Visualize the result
plt.plot(np.abs(X))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('FFT of the signal')
plt.show()
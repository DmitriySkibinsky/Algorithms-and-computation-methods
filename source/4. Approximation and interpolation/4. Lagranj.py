import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [3.5, 4.4, 3.2, 2.7, 2.55]

def lagranz(x, y, q):
    slag = 0
    for j in range(len(y)):
        lk1 = 1
        lk2 = 1
        for i in range(len(x)):
            if i != j:
                lk1 = lk1 * (q - x[i])
                lk2 = lk2 * (x[j] - x[i])
        slag = slag + y[j] * lk1 / lk2
    return slag

n = 100
xnext = [min(x) + i * (max(x) - min(x)) / n for i in range(n+1)]
ynext = [lagranz(x, y, i) for i in xnext]

plt.plot(x, y, 'o', xnext, ynext)
plt.grid(True)
plt.show()
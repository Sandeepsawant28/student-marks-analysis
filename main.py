import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20, r=2):
   
  
    x = np.linspace(-2.5, 1.5, w)
    y = np.linspace(-1.5, 1.5, h)
    A, B = np.meshgrid(x, y)
    C = A + 1j*B
    z = np.zeros_like(C)
    
    
    divtime = maxit + np.zeros(z.shape, dtype=int)
    
    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                   
        div_now = diverge & (divtime == maxit) 
        divtime[div_now] = i                   
        z[diverge] = r                         
    
    return divtime

plt.figure(figsize=(8, 8))
plt.imshow(mandelbrot(400, 400), cmap='hot', extent=[-2.5, 1.5, -1.5, 1.5])
plt.colorbar(label='Iterations to diverge')
plt.title('Mandelbrot Fractal')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()
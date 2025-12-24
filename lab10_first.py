import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0,10, 50)

#рівняння
y = (5 * np.cos(10*x) * np.sin(3*x)) / (x ** (1/2))

#граф
plt.plot(x, y, label= 'функція у', color = 'deepskyblue', linewidth = 3)
plt.title('Перший граф', fontsize = 19, color = 'cadetblue')
plt.xlabel('Вісь х', color = 'darkolivegreen', fontsize = 12)
plt.ylabel('Вісь у', color = 'darkolivegreen', fontsize = 12)
plt.legend()
plt.grid(True)
plt.show()





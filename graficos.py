import time
import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    start_time = time.time()
    plt.plot(x, y)
    plt.show()
    end_time = time.time()
    print(f"Tempo de execução para gerar gráfico: {end_time - start_time} segundos.")
    
plot_graph()

import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)

    plt.xlabel('Время, с', fontsize=12)
    plt.ylabel('Напряжение, В', fontsize=12)

    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage * 1.1)

   plt.grid(True) 
   plt.show()



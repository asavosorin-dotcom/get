import time
import matplotlib.pyplot as plt

from mcp3021_driver.py import MCP3021
from mcp3021_driver.py import get_voltage

if __name__ == "__main__":
    dynamic_range = 3.3
    duration = 10
    
    times = []
    voltages = []
    
    try:
        adc = MCP3021(dynamic_range, verbose=False)
        
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_voltage()
            current_time = time.time() - start_time
            
            times.append(current_time)
            voltages.append(voltage)
            
            print(f"{current_time:.2f} с: {voltage:.3f} В")
            time.sleep(0.1)
        
        plt.figure(figsize=(10, 6))
        plt.plot(times, voltages, 'b-', linewidth=2)
        plt.xlabel('Время (с)')
        plt.ylabel('Напряжение (В)')
        plt.title(f'Зависимость напряжения на входе MCP3021\nДиапазон: {dynamic_range} В, Длительность: {duration} с')
        plt.grid(True)
        plt.ylim(0, dynamic_range)
        plt.show()
        
    except KeyboardInterrupt:
        print("\nИзмерение прервано")
        
    finally:
        adc.deinit()

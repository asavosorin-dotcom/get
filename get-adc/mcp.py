import time
import matplotlib.pyplot as plt
from mcp3021_driver import MCP3021

if __name__ == "__main__":
    dynamic_range = 3.3
    duration = 30
    
    times = []
    voltages = []
    intervals = []
    
    try:
        adc = MCP3021(dynamic_range, verbose=False)
        
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_voltage()
            current_time = time.time() - start_time
            
            times.append(current_time)
            voltages.append(voltage)
            
            if len(times) > 1:
                interval = times[-1] - times[-2]
                intervals.append(interval)
            
            print(f"{current_time:.2f} с: {voltage:.3f} В")
            time.sleep(0.1)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        ax1.plot(times, voltages, 'b-', linewidth=2)
        ax1.set_xlabel('Время (с)')
        ax1.set_ylabel('Напряжение (В)')
        ax1.set_title(f'Зависимость напряжения на входе MCP3021\nДиапазон: {dynamic_range} В, Длительность: {duration} с')
        ax1.grid(True)
        ax1.set_ylim(0, dynamic_range)
        
        if intervals:
            ax2.hist(intervals, bins=20, color='g', edgecolor='black', alpha=0.7)
            ax2.set_xlabel('Интервал между измерениями (с)')
            ax2.set_ylabel('Количество измерений')
            ax2.set_title(f'Распределение интервалов между измерениями\nСредний интервал: {sum(intervals)/len(intervals):.4f} с')
            ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
    except KeyboardInterrupt:
        print("\nИзмерение прервано")
        
    finally:
        adc.deinit()

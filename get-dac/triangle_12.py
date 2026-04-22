import mcp4725_driver as mcp
import time

def get_triangle_wave_amplitude(freq, t, period):
    t_mod = t % period
    if t_mod < period / 2:
        return (t_mod / (period / 2))
    else:
        return (2 - (t_mod / (period / 2)))

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
period = 1 / signal_frequency

try:
    dac = mcp.MCP4725(3.3, 0x61, True)
    
    t = 0
    while True:
        normalized_amplitude = get_triangle_wave_amplitude(signal_frequency, t, period)
        voltage = normalized_amplitude * amplitude
        dac.set_voltage(voltage)
        
        t += 1 / sampling_frequency
        time.sleep(1 / sampling_frequency)

finally:
    dac.deinit()

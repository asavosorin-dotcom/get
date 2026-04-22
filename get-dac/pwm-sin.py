import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3, True)
    
    while True:
        for i in range(int(sampling_frequency / signal_frequency)):
            t = i / sampling_frequency
            normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, t)
            voltage = normalized_amplitude * amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()

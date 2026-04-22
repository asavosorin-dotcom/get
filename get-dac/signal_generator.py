import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    value = np.sin(2 * np.pi * freq * time)
    value_shifted = value + 1
    value_normalized = value_shifted / 2
    return value_normalized

def wait_for_sampling_period(sampling_frequency):
    period = 1 / sampling_frequency
    time.sleep(period)

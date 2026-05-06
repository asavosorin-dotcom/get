import RPi.GPIO as GPIO
import time 

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.cleanup()
        GPIO.output(self.bits_gpio, 0)

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, dec2bin(number))

    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(compare_time)

            comp_value = GPIO.input(self.comp_gpio)
            if comp_value:
                return i

        return 255

    def get_sc_voltage(self):
        number_voltage = self.sequential_counting_adc()
        return number_voltage / 256 * self.dynamic_range

    def successive_approximation_adc(self):
        result = 0

        for bit in range(7, -1, -1):
            test_value = result | (1 << bit) 

            self.number_to_dac(test_value)
            time.sleep(compare_time)
    
            comp_value = GPIO.input(self.comp_gpio)

            if comp_value == 1:
                pass 
            else:
                result = test_value

        return result

    def get_sar_voltage(self):
        number_voltage = self.successive_approximation_adc()
        voltage = number_voltage / 256 * self.dynamic_range
        return voltage

if __name__ == "__main__":
    try:
        r2r_adc = R2R_ADC(3.292)

        while True:
            # voltage = r2r_adc.get_sc_voltage()
            voltage = r2r_adc.get_sar_voltage()
            print(f"Voltage {voltage: .3f}")
            time.sleep(0.5)

    finally:
        r2r_adc.deinit()

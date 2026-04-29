import RPi.GPIO as GPIO

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
            if (comp_value):
                return i

    def get_sc_voltage(self):
        number_voltage = self.sequential_counting_adc()
        return number_voltage / 256 * self.dynamic_range

try:
    r2r_adc = R2R_ADC(5)

    while (True):
        voltage = r2r_adc.get_sc_voltage()
        print(f"Voltage {voltage}")

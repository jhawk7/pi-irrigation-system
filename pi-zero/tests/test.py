from ..pkg.moisture_sensor import ADCMsensor
from ..pkg.water_pump import WaterPumpRelay

def main():
  pump = WaterPumpRelay(24)
  mp, raw = ADCMsensor.get_adc_moisture_reading(0)
  print(f'MP: {mp}\nRAW: {raw}\n\n')
  pump.release()
  


# Left plant dry
# MP: 21.66102
# RAW: 43610

# MP: 21.82373
# RAW: 43562

# MP: 21.44407
# RAW: 43674


# right plant dry
# MP: 24.42712
# RAW: 42794

# MP: 24.21017
# RAW: 42858

# MP: 24.64407
# RAW: 42730


# left plant wet
# MP: 90.28814
# RAW: 23365

# MP: 90.07119
# RAW: 23429


# right plant wet
# MP: 84.42712
# RAW: 25094

# MP: 84.42712
# RAW: 25094

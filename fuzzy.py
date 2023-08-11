

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create temperature and humidity variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define fuzzy membership functions
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['low'] & humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['low'] & humidity['high'], fan_speed['high'])
# Define more rules...

# Create fuzzy control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create simulation
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# Input temperature and humidity values
fan_sim.input['temperature'] = 75
fan_sim.input['humidity'] = 40

# Compute the result
fan_sim.compute()

print("Fan Speed:", fan_sim.output['fan_speed'])



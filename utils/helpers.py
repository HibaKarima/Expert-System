from skfuzzy import control as ctrl
from fuzzy.variables import temperature, status
from fuzzy.membership import temperature, status
# Rules

rule1 = ctrl.Rule(
    temperature['high'],
    status['danger']
)

rule2 = ctrl.Rule(
    temperature['medium'],
    status['warning']
)

rule3 = ctrl.Rule(
    temperature['low'],
    status['normal']
)
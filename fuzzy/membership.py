import skfuzzy as fuzz
from fuzzy.variables import cpu_usage , ram_usage , temperature, disk_health , boot_time , performance , overheating_risk , stability
import json

# LOAD FUZZY RANGES

with open("data/fuzzy_ranges.json", "r") as file:
    ranges = json.load(file)

# Add membership functions to INPUT variables

# cpu_usage
cpu_usage['low'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['low'])
cpu_usage['medium'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['medium'])
cpu_usage['high'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['high'])

# ram_usage
ram_usage['low'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['low'])
ram_usage['medium'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['medium'])
ram_usage['high'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['high'])

# temperature
temperature['cool'] = fuzz.trapmf(temperature.universe, ranges['temperature']['cool'])
temperature['warm'] = fuzz.trapmf(temperature.universe, ranges['temperature']['warm'])
temperature['hot'] = fuzz.trapmf(temperature.universe, ranges['temperature']['hot'])

# disk_health
disk_health['bad'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['bad'])
disk_health['normal'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['normal'])
disk_health['good'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['good'])

# boot_time
boot_time['fast'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['fast'])
boot_time['medium'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['medium'])
boot_time['slow'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['slow'])

# Add membership functions to OUTPUT variables

# performance
performance['low'] = fuzz.trapmf(performance.universe, ranges['performance']['low'])
performance['medium'] = fuzz.trapmf(performance.universe, ranges['performance']['medium'])
performance['high'] = fuzz.trapmf(performance.universe, ranges['performance']['high'])

# overheating_risk
overheating_risk['low'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['low'])
overheating_risk['medium'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['medium'])
overheating_risk['high'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['high'])

# stability
stability['unstable'] = fuzz.trapmf(stability.universe, ranges['stability']['unstable'])
stability['moderate'] = fuzz.trapmf(stability.universe, ranges['stability']['moderate'])
stability['stable'] = fuzz.trapmf(stability.universe, ranges['stability']['stable'])

# Export variable objects for inference.py
cpu = cpu_usage
ram = ram_usage
temp = temperature
disk = disk_health
boot = boot_time
performance_out = performance
overheat_out = overheating_risk
stability_out = stability
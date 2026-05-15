import json
from copy import deepcopy

import skfuzzy as fuzz

from fuzzy.context import get_parameterized_ranges

with open("data/fuzzy_ranges.json", "r") as file:
    BASE_RANGES = json.load(file)


def _apply_memberships(ranges, antecedents, consequents):
    cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise = antecedents[:6]
    disk_usage, free_space, battery_health, post_success, drive_detected = antecedents[6:]
    
    performance, overheating_risk, stability, storage_issue, battery_issue, boot_issue = consequents
    
    cpu_usage['low'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['low'])
    cpu_usage['medium'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['medium'])
    cpu_usage['high'] = fuzz.trapmf(cpu_usage.universe, ranges['cpu_usage']['high'])

    ram_usage['low'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['low'])
    ram_usage['medium'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['medium'])
    ram_usage['high'] = fuzz.trapmf(ram_usage.universe, ranges['ram_usage']['high'])

    temperature['cool'] = fuzz.trapmf(temperature.universe, ranges['temperature']['cool'])
    temperature['warm'] = fuzz.trapmf(temperature.universe, ranges['temperature']['warm'])
    temperature['hot'] = fuzz.trapmf(temperature.universe, ranges['temperature']['hot'])

    disk_health['bad'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['bad'])
    disk_health['normal'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['normal'])
    disk_health['good'] = fuzz.trapmf(disk_health.universe, ranges['disk_health']['good'])

    boot_time['fast'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['fast'])
    boot_time['medium'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['medium'])
    boot_time['slow'] = fuzz.trapmf(boot_time.universe, ranges['boot_time']['slow'])

    fan_noise['low'] = fuzz.trapmf(fan_noise.universe, ranges['fan_noise']['low'])
    fan_noise['normal'] = fuzz.trapmf(fan_noise.universe, ranges['fan_noise']['normal'])
    fan_noise['high'] = fuzz.trapmf(fan_noise.universe, ranges['fan_noise']['high'])

    disk_usage['low'] = fuzz.trapmf(disk_usage.universe, ranges['disk_usage']['low'])
    disk_usage['medium'] = fuzz.trapmf(disk_usage.universe, ranges['disk_usage']['medium'])
    disk_usage['high'] = fuzz.trapmf(disk_usage.universe, ranges['disk_usage']['high'])

    free_space['low'] = fuzz.trapmf(free_space.universe, ranges['free_space']['low'])
    free_space['medium'] = fuzz.trapmf(free_space.universe, ranges['free_space']['medium'])
    free_space['high'] = fuzz.trapmf(free_space.universe, ranges['free_space']['high'])

    battery_health['good'] = fuzz.trapmf(battery_health.universe, ranges['battery_health']['good'])
    battery_health['worn'] = fuzz.trapmf(battery_health.universe, ranges['battery_health']['worn'])
    battery_health['critical'] = fuzz.trapmf(battery_health.universe, ranges['battery_health']['critical'])

    post_success['no'] = fuzz.trapmf(post_success.universe, ranges['binary_yesno']['no'])
    post_success['yes'] = fuzz.trapmf(post_success.universe, ranges['binary_yesno']['yes'])
    drive_detected['no'] = fuzz.trapmf(drive_detected.universe, ranges['binary_yesno']['no'])
    drive_detected['yes'] = fuzz.trapmf(drive_detected.universe, ranges['binary_yesno']['yes'])

    performance['low'] = fuzz.trapmf(performance.universe, ranges['performance']['low'])
    performance['medium'] = fuzz.trapmf(performance.universe, ranges['performance']['medium'])
    performance['high'] = fuzz.trapmf(performance.universe, ranges['performance']['high'])

    overheating_risk['low'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['low'])
    overheating_risk['medium'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['medium'])
    overheating_risk['high'] = fuzz.trapmf(overheating_risk.universe, ranges['overheating_risk']['high'])

    stability['unstable'] = fuzz.trapmf(stability.universe, ranges['stability']['unstable'])
    stability['moderate'] = fuzz.trapmf(stability.universe, ranges['stability']['moderate'])
    stability['stable'] = fuzz.trapmf(stability.universe, ranges['stability']['stable'])

    storage_issue['low'] = fuzz.trapmf(storage_issue.universe, ranges['storage_issue']['low'])
    storage_issue['medium'] = fuzz.trapmf(storage_issue.universe, ranges['storage_issue']['medium'])
    storage_issue['high'] = fuzz.trapmf(storage_issue.universe, ranges['storage_issue']['high'])

    battery_issue['low'] = fuzz.trapmf(battery_issue.universe, ranges['battery_issue']['low'])
    battery_issue['medium'] = fuzz.trapmf(battery_issue.universe, ranges['battery_issue']['medium'])
    battery_issue['high'] = fuzz.trapmf(battery_issue.universe, ranges['battery_issue']['high'])

    boot_issue['none'] = fuzz.trapmf(boot_issue.universe, ranges['boot_issue']['none'])
    boot_issue['possible'] = fuzz.trapmf(boot_issue.universe, ranges['boot_issue']['possible'])
    boot_issue['critical'] = fuzz.trapmf(boot_issue.universe, ranges['boot_issue']['critical'])


def apply_context_thresholds(context_config=None):
    from fuzzy.variables import (
        cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise,
        disk_usage, free_space, battery_health, post_success, drive_detected,
        performance, overheating_risk, stability, storage_issue, battery_issue, boot_issue
    )
    
    antecedents = [
        cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise,
        disk_usage, free_space, battery_health, post_success, drive_detected
    ]
    consequents = [performance, overheating_risk, stability, storage_issue, battery_issue, boot_issue]
    
    if context_config is None:
        ranges = deepcopy(BASE_RANGES)
    else:
        ranges = get_parameterized_ranges(BASE_RANGES, context_config)
    
    _apply_memberships(ranges, antecedents, consequents)
    return ranges
import skfuzzy.control as ctrl


def build_fuzzy_rules(
    cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise,
    disk_usage, free_space, battery_health, post_success, drive_detected,
    performance, overheating_risk, stability,
    storage_issue, battery_issue, boot_issue
):

    rules = []

    rules.append(ctrl.Rule(
        temperature['hot'] & cpu_usage['high'] & fan_noise['high'],
        overheating_risk['high']
    ))

    rules.append(ctrl.Rule(
        temperature['hot'] & cpu_usage['high'] & fan_noise['low'],
        overheating_risk['high']
    ))

    rules.append(ctrl.Rule(
        temperature['warm'] & cpu_usage['high'] & fan_noise['high'],
        overheating_risk['medium']
    ))

    rules.append(ctrl.Rule(
        temperature['warm'] & ram_usage['high'] & fan_noise['high'],
        overheating_risk['medium']
    ))

    rules.append(ctrl.Rule(
        temperature['cool'] & cpu_usage['low'] & fan_noise['normal'],
        overheating_risk['low']
    ))

    rules.append(ctrl.Rule(
        temperature['hot'] & ram_usage['high'],
        overheating_risk['high']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['low'] & ram_usage['low'] & boot_time['fast'] & disk_health['good'],
        performance['high']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['medium'] & ram_usage['medium'] & disk_health['normal'],
        performance['medium']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['high'] & ram_usage['high'] & boot_time['slow'],
        performance['medium']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['high'] & boot_time['slow'] & disk_health['bad'],
        performance['low']
    ))

    rules.append(ctrl.Rule(
        disk_health['good'] & boot_time['fast'] & cpu_usage['medium'],
        performance['high']
    ))

    rules.append(ctrl.Rule(
        boot_time['slow'] & ram_usage['high'],
        performance['low']
    ))

    rules.append(ctrl.Rule(
        disk_health['good'] & cpu_usage['medium'] & temperature['cool'],
        stability['stable']
    ))

    rules.append(ctrl.Rule(
        boot_time['fast'] & cpu_usage['low'] & ram_usage['low'],
        stability['stable']
    ))

    rules.append(ctrl.Rule(
        boot_time['slow'] & disk_health['bad'],
        stability['unstable']
    ))

    rules.append(ctrl.Rule(
        ram_usage['high'] & disk_health['bad'],
        stability['unstable']
    ))

    rules.append(ctrl.Rule(
        temperature['hot'] & cpu_usage['high'] & fan_noise['low'],
        stability['unstable']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['medium'] & ram_usage['medium'] & disk_health['normal'] & temperature['warm'],
        stability['moderate']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['low'] & ram_usage['low'] & disk_health['good'] & temperature['cool'],
        stability['stable']
    ))

    rules.append(ctrl.Rule(
        disk_usage['high'] & free_space['low'],
        storage_issue['high']
    ))

    rules.append(ctrl.Rule(
        disk_usage['medium'] & free_space['medium'],
        storage_issue['medium']
    ))

    rules.append(ctrl.Rule(
        disk_usage['low'] & free_space['high'],
        storage_issue['low']
    ))

    rules.append(ctrl.Rule(
        battery_health['critical'],
        battery_issue['high']
    ))

    rules.append(ctrl.Rule(
        battery_health['worn'],
        battery_issue['medium']
    ))

    rules.append(ctrl.Rule(
        battery_health['good'],
        battery_issue['low']
    ))

    rules.append(ctrl.Rule(
        boot_time['slow'] & disk_health['bad'],
        boot_issue['critical']
    ))

    rules.append(ctrl.Rule(
        boot_time['slow'] & disk_health['normal'],
        boot_issue['possible']
    ))

    rules.append(ctrl.Rule(
        boot_time['fast'] & disk_health['good'],
        boot_issue['none']
    ))

    rules.append(ctrl.Rule(
        post_success['yes'],
        stability['stable']
    ))

    rules.append(ctrl.Rule(
        drive_detected['yes'],
        boot_issue['none']
    ))

    rules.append(ctrl.Rule(
        cpu_usage['high'] & ram_usage['high'],
        performance['low']
    ))

    rules.append(ctrl.Rule(
        temperature['hot'],
        overheating_risk['high']
    ))

    rules.append(ctrl.Rule(
        temperature['cool'],
        overheating_risk['low']
    ))

    rules.append(ctrl.Rule(
        boot_time['slow'],
        boot_issue['critical']
    ))

    rules.append(ctrl.Rule(
        disk_usage['high'],
        storage_issue['high']
    ))

    rules.append(ctrl.Rule(
        disk_usage['low'],
        storage_issue['low']
    ))

    return rules

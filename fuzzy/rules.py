# import skfuzzy.control as ctrl

# def build_fuzzy_rules(cpu, ram, temp, disk, boot, performance, overheating, stability):
#     rules = []

#     # Performance rules
#     rules.append(ctrl.Rule(
#         cpu['low'] & ram['low'] & boot['fast'] & disk['good'],
#         performance['high']
#     ))

#     rules.append(ctrl.Rule(
#         cpu['medium'] & ram['medium'] & disk['normal'],
#         performance['medium']
#     ))

#     rules.append(ctrl.Rule(
#         cpu['high'] & ram['high'] & boot['slow'],
#         performance['medium']
#     ))

#     rules.append(ctrl.Rule(
#         cpu['low'] & boot['slow'] & disk['bad'],
#         performance['low']
#     ))

#     rules.append(ctrl.Rule(
#         ram['high'] & cpu['high'] & disk['normal'],
#         performance['medium']
#     ))

#     rules.append(ctrl.Rule(
#         disk['good'] & boot['fast'] & cpu['medium'],
#         performance['high']
#     ))

#     rules.append(ctrl.Rule(
#         ram['low'] & cpu['high'] & boot['slow'],
#         performance['low']
#     ))

#     rules.append(ctrl.Rule(
#         boot['slow'] & disk['bad'],
#         performance['low']
#     ))

#     rules.append(ctrl.Rule(
#         ram['high'] & cpu['low'],
#         performance['medium']
#     ))

#     rules.append(ctrl.Rule(
#         disk['good'] & boot['fast'] ,
#         performance['high']
#     ))

#     rules.append(ctrl.Rule(
#         cpu['low'] & ram['low'] & temp['cool'] ,
#         performance['high']
#     ))

#     # Overheating risk rules
#     rules.append(ctrl.Rule(
#         temp['hot'] & cpu['high'],
#         overheating['high']
#     ))

#     rules.append(ctrl.Rule(
#         temp['warm'] & cpu['high'],
#         overheating['medium']
#     ))

#     rules.append(ctrl.Rule(
#         temp['hot'] & cpu['medium'],
#         overheating['high']
#     ))

#     rules.append(ctrl.Rule(
#         temp['cool'] & cpu['low'],
#         overheating['low']
#     ))

#     rules.append(ctrl.Rule(
#         temp['warm'] & ram['medium'],
#         overheating['medium']
#     ))

#     rules.append(ctrl.Rule(
#         temp['hot'] & boot['slow'] & ram['high'],
#         overheating['high']
#     ))

#     rules.append(ctrl.Rule(
#         temp['hot'] & ram['high'],
#         overheating['high']
#     ))

#     rules.append(ctrl.Rule(
#         temp['cool'] & cpu['medium'],
#         overheating['low']
#     ))

#     # Stability rules
#     rules.append(ctrl.Rule(
#         performance['high'] & overheating['low'] & disk['good'],
#         stability['stable']
#     ))

#     rules.append(ctrl.Rule(
#         performance['medium'] & overheating['medium'] & disk['normal'],
#         stability['moderate']
#     ))

#     rules.append(ctrl.Rule(
#         performance['low'] | overheating['high'],
#         stability['unstable']
#     ))

#     rules.append(ctrl.Rule(
#         boot['slow'] & disk['bad'],
#         stability['unstable']
#     ))

#     rules.append(ctrl.Rule(
#         performance['high'] & overheating['medium'],
#         stability['moderate']
#     ))

#     rules.append(ctrl.Rule(
#         performance['medium'] & overheating['low'],
#         stability['stable']
#     ))

#     rules.append(ctrl.Rule(
#         disk['good'] & cpu['medium'] & temp['cool'],
#         stability['stable']
#     ))

#     rules.append(ctrl.Rule(
#         boot['fast'] & cpu['low'],
#         stability['stable']
#     ))

#     rules.append(ctrl.Rule(
#         temp['hot'] & disk['bad'],
#         stability['unstable']
#     ))

#     rules.append(ctrl.Rule(
#         ram['high'] & disk['bad'],
#         stability['unstable']
#     ))

#     rules.append(ctrl.Rule(
#         ram['high'] & cpu['high'] & temp['hot'],
#         stability['unstable']
#     ))

#     return rules

# fuzzy/rules.py

FUZZY_RULES = [

    {
        "name": "High Overheating Risk",

        "conditions": {
            "temperature": "HIGH",
            "cpu_usage": "HIGH",
            "fan_noise": "HIGH"
        },

        "output": {
            "overheating_risk": "HIGH"
        }
    },

    {
        "name": "Moderate Performance Issue",

        "conditions": {
            "ram_usage": "HIGH",
            "startup_time": "HIGH"
        },

        "output": {
            "performance": "LOW"
        }
    },

    {
        "name": "Possible Storage Issue",

        "conditions": {
            "disk_usage": "HIGH",
            "boot_time": "HIGH",
            "freezing_frequency": "HIGH"
        },

        "output": {
            "storage_issue_risk": "HIGH"
        }
    }
]
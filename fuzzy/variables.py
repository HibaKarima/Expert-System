import numpy as np
from skfuzzy import control as ctrl
#Input
cpu_usage = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'cpu_usage'
)
ram_usage = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'ram_usage'
)
temperature = ctrl.Antecedent(
    np.arange(0,  121, 1),
    'temperature'
)
disk_health = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'disk_health'
)
boot_time = ctrl.Antecedent(
    np.arange(0, 201, 1),
    'boot_time'
)
fan_noise = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'fan_noise'
)
disk_usage = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'disk_usage'
)
free_space = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'free_space'
)
battery_health = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'battery_health'
)
post_success = ctrl.Antecedent(
    np.arange(0, 2, 1),
    'post_success'
)
drive_detected = ctrl.Antecedent(
    np.arange(0, 2, 1),
    'drive_detected'
)
# Output
performance = ctrl.Consequent(
    np.arange(0, 101, 1),
    'performance'
)
overheating_risk = ctrl.Consequent(
    np.arange(0, 101, 1),
    'overheating_risk'
)
stability= ctrl.Consequent(
    np.arange(0, 101, 1),
    'stability'
)
storage_issue = ctrl.Consequent(
    np.arange(0, 101, 1),
    'storage_issue'
)
battery_issue = ctrl.Consequent(
    np.arange(0, 101, 1),
    'battery_issue'
)
boot_issue = ctrl.Consequent(
    np.arange(0, 101, 1),
    'boot_issue'
)

   
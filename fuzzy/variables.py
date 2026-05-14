import numpy as np
from skfuzzy import control as ctrl
#CPU_USAGE = [0, 100]

# LOW:    [0, 0, 40]
# MEDIUM: [30, 50, 70]
# HIGH:   [60, 100, 100]


# RAM_USAGE = [0, 100]

# LOW:    [0, 0, 40]
# MEDIUM: [30, 50, 70]
# HIGH:   [60, 100, 100]

# TEMPERATURE = [0, 120]

# COOL:   [0, 0, 50]
# WARM:   [40, 60, 75]
# HOT:    [70, 120, 120]

# DISK_HEALTH = [0, 100]

# BAD:    [0, 0, 40]
# NORMAL: [30, 60, 80]
# GOOD:   [70, 100, 100]


# BOOT_TIME = [0, 200]

# FAST:   [0, 0, 40]
# NORMAL: [30, 60, 100]
# SLOW:   [80, 200, 200]

# ///////////////////
# PERFORMANCE = [0, 100]

# LOW:    [0, 0, 40]
# MEDIUM: [30, 50, 70]
# HIGH:   [60, 100, 100]


# OVERHEATING = [0, 100]

# LOW:    [0, 0, 40]
# MEDIUM: [30, 60, 80]
# HIGH:   [70, 100, 100]

# STABILITY = [0, 100]

# UNSTABLE: [0, 0, 40]
# MODERATE: [30, 50, 70]
# STABLE:   [60, 100, 100]


# Input
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

   
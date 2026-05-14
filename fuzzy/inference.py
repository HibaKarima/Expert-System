
import skfuzzy.control as ctrl
from fuzzy.rules import build_fuzzy_rules

from fuzzy.membership import (
    cpu,
    ram,
    temp,
    disk,
    boot,
    performance_out,
    overheat_out,
    stability_out
)

# BUILD RULES

rules = build_fuzzy_rules(
    cpu,
    ram,
    temp,
    disk,
    boot,
    performance_out,
    overheat_out,
    stability_out
)

# CONTROL SYSTEM

system_ctrl = ctrl.ControlSystem(rules)

system_simulation = ctrl.ControlSystemSimulation(system_ctrl)


# MAIN INFERENCE FUNCTION
def run_inference(cpu_value, ram_value, temp_value,
                  disk_value, boot_value):

    # Set Inputs
    system_simulation.input['cpu_usage'] = cpu_value
    system_simulation.input['ram_usage'] = ram_value
    system_simulation.input['temperature'] = temp_value
    system_simulation.input['disk_health'] = disk_value
    system_simulation.input['boot_time'] = boot_value

    # Compute
    system_simulation.compute()

    # Collect Results
    results = {
        "performance": round(
            system_simulation.output['performance'], 2
        ),

        "overheating_risk": round(
            system_simulation.output['overheating_risk'], 2
        ),

        "stability": round(
            system_simulation.output['stability'], 2
        )
    }

    return results
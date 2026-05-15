
import skfuzzy.control as ctrl
from fuzzy.rules import build_fuzzy_rules
from fuzzy.membership import apply_context_thresholds
from fuzzy.recommendations import get_recommendations

from fuzzy.variables import (
    cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise,
    disk_usage, free_space, battery_health, post_success, drive_detected,
    performance, overheating_risk, stability, storage_issue, battery_issue, boot_issue
)

apply_context_thresholds()

system_simulation = None


def _build_system():
    global system_simulation
    
    rules = build_fuzzy_rules(
        cpu_usage, ram_usage, temperature, disk_health, boot_time, fan_noise,
        disk_usage, free_space, battery_health, post_success, drive_detected,
        performance, overheating_risk, stability, storage_issue, battery_issue, boot_issue
    )
    
    system_ctrl = ctrl.ControlSystem(rules)
    
    system_simulation = ctrl.ControlSystemSimulation(system_ctrl)


def run_inference(cpu_value, ram_value, temp_value,
                  disk_value, boot_value, fan_value=0,
                  disk_usage_value=0, free_space_value=100,
                  battery_health_value=100, post_success_value=1,
                  drive_detected_value=1, context_config=None):

    def _safe_output(name, default=0.0):
        val = system_simulation.output.get(name, default)
        try:
            return round(float(val), 2)
        except (TypeError, ValueError):
            return round(float(default), 2)

    apply_context_thresholds(context_config)
    _build_system()
    
    system_simulation.reset()

    system_simulation.input['cpu_usage'] = cpu_value
    system_simulation.input['ram_usage'] = ram_value
    system_simulation.input['temperature'] = temp_value
    system_simulation.input['disk_health'] = disk_value
    system_simulation.input['boot_time'] = boot_value
    system_simulation.input['fan_noise'] = fan_value
    system_simulation.input['disk_usage'] = disk_usage_value
    system_simulation.input['free_space'] = free_space_value
    system_simulation.input['battery_health'] = battery_health_value
    system_simulation.input['post_success'] = post_success_value
    system_simulation.input['drive_detected'] = drive_detected_value

    system_simulation.compute()

    results = {
        "performance": _safe_output('performance'),
        "overheating_risk": _safe_output('overheating_risk'),
        "stability": _safe_output('stability'),
    }

    if 'storage_issue' in system_simulation.output:
        results['storage_issue'] = _safe_output('storage_issue')

    if 'battery_issue' in system_simulation.output:
        results['battery_issue'] = _safe_output('battery_issue')

    if 'boot_issue' in system_simulation.output:
        results['boot_issue'] = _safe_output('boot_issue')

    results['recommendations'] = get_recommendations(results, context_config)

    return results


def run_system(
    cpu_value,
    ram_value,
    temp_value,
    disk_value,
    boot_value,
    fan_value=0,
    disk_usage_value=0,
    free_space_value=100,
    battery_health_value=100,
    post_success_value=1,
    drive_detected_value=1,
    context_config=None,
):
    return run_inference(
        cpu_value=cpu_value,
        ram_value=ram_value,
        temp_value=temp_value,
        disk_value=disk_value,
        boot_value=boot_value,
        fan_value=fan_value,
        disk_usage_value=disk_usage_value,
        free_space_value=free_space_value,
        battery_health_value=battery_health_value,
        post_success_value=post_success_value,
        drive_detected_value=drive_detected_value,
        context_config=context_config,
    )
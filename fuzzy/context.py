from copy import deepcopy

def _normalize(value):
    if value is None:
        return "unknown"
    return str(value).strip().lower().replace(" ", "_")


def get_context_config(brand, laptop_type, os_type, usage_type):
    brand = _normalize(brand)
    laptop_type = _normalize(laptop_type)
    os_type = _normalize(os_type)
    usage_type = _normalize(usage_type)

    config = {
        "context": {
            "brand": brand,
            "laptop_type": laptop_type,
            "os_type": os_type,
            "usage_type": usage_type,
        },
        "thresholds": {
            "temp_high": 80,
            "cpu_expected": 70,
            "battery_expected_hours": 5,
            "fan_high": 80,
        },
        "expectations": {
            "performance_mode": "balanced",
            "thermal_profile": "standard",
            "primary_focus": "diagnosis",
        },
        "recommendation_path": {
            "overheating": [
                "Clean cooling fan",
                "Improve laptop ventilation",
            ],
            "performance": [
                "Close background applications",
                "Restart system",
            ],
            "storage": [
                "Free up disk space",
                "Backup important files",
            ],
            "battery": [
                "Check charger and power settings",
                "Reduce brightness and background load",
            ],
            "boot": [
                "Run startup repair",
                "Check drive detection in BIOS",
            ],
        },
        "adjustments": [],
    }

    if laptop_type in {"gaming", "gamer", "performance"}:
        config["thresholds"]["temp_high"] = 90
        config["thresholds"]["cpu_expected"] = 85
        config["thresholds"]["fan_high"] = 85
        config["expectations"]["thermal_profile"] = "aggressive"
        config["recommendation_path"]["performance"] = [
            "Reduce graphics settings",
            "Close background applications",
        ]
        config["adjustments"].append("gaming_profile")

    elif laptop_type in {"office", "business", "productivity"}:
        config["thresholds"]["temp_high"] = 75
        config["thresholds"]["cpu_expected"] = 60
        config["expectations"]["thermal_profile"] = "conservative"
        config["recommendation_path"]["performance"] = [
            "Close background applications",
            "Restart system",
        ]
        config["adjustments"].append("office_profile")

    elif laptop_type in {"ultrabook", "thin", "lightweight"}:
        config["thresholds"]["temp_high"] = 72
        config["thresholds"]["cpu_expected"] = 55
        config["thresholds"]["fan_high"] = 75
        config["expectations"]["thermal_profile"] = "cooling_sensitive"
        config["adjustments"].append("thin_and_light_profile")

    if os_type == "linux":
        config["thresholds"]["cpu_expected"] -= 10
        config["adjustments"].append("linux_tolerance")
    elif os_type in {"windows", "windows_11", "windows_10"}:
        config["adjustments"].append("windows_background_activity")

    if brand == "asus":
        config["thresholds"]["temp_high"] += 3
        config["adjustments"].append("asus_thermal_margin")
    elif brand == "lenovo":
        config["thresholds"]["temp_high"] -= 2
        config["adjustments"].append("lenovo_thermal_margin")
    elif brand == "hp":
        config["adjustments"].append("hp_service_profile")
    elif brand == "dell":
        config["adjustments"].append("dell_service_profile")

    if usage_type in {"gaming", "play", "playing"}:
        config["expectations"]["primary_focus"] = "performance"
        config["recommendation_path"]["performance"] = [
            "Reduce graphics settings",
            "Use cooling pad",
        ]
        config["adjustments"].append("gaming_usage")
    elif usage_type in {"office", "study", "productivity"}:
        config["expectations"]["primary_focus"] = "stability"
        config["recommendation_path"]["performance"] = [
            "Close background applications",
            "Restart system",
        ]
        config["adjustments"].append("office_usage")
    elif usage_type in {"diagnosis", "troubleshooting"}:
        config["expectations"]["primary_focus"] = "diagnosis"
        config["adjustments"].append("diagnosis_mode")

    config["summary"] = {
        "temp_high_threshold": config["thresholds"]["temp_high"],
        "expected_cpu_usage": config["thresholds"]["cpu_expected"],
        "battery_expected_hours": config["thresholds"]["battery_expected_hours"],
        "recommended_path": config["recommendation_path"].get(config["expectations"]["primary_focus"], []),
    }

    return config


def _clamp(value, lower, upper):
    return max(lower, min(upper, value))


def _shift_range(points, delta, lower_bound, upper_bound):
    return [
        _clamp(point + delta, lower_bound, upper_bound)
        for point in points
    ]


def get_parameterized_ranges(base_ranges, context_config):

    adjusted = deepcopy(base_ranges)
    thresholds = context_config.get("thresholds", {}) if context_config else {}
    adjustments = context_config.get("adjustments", []) if context_config else []

    temp_high = thresholds.get("temp_high", 80)
    cpu_expected = thresholds.get("cpu_expected", 70)
    fan_high = thresholds.get("fan_high", 80)

    temperature_hot_start = _clamp(temp_high - 20, 0, 120)
    temperature_hot_peak = _clamp(temp_high - 5, 0, 120)
    adjusted["temperature"]["hot"] = [
        temperature_hot_start,
        temperature_hot_peak,
        120,
        120,
    ]

    if "gaming_profile" in adjustments or "gaming_usage" in adjustments:
        adjusted["temperature"]["warm"] = [45, 60, 75, _clamp(temp_high, 0, 120)]
    elif "office_profile" in adjustments or "office_usage" in adjustments:
        adjusted["temperature"]["warm"] = [35, 50, 62, _clamp(temp_high, 0, 120)]

    cpu_high_start = _clamp(cpu_expected - 25, 0, 100)
    cpu_high_peak = _clamp(cpu_expected - 5, 0, 100)
    adjusted["cpu_usage"]["high"] = [cpu_high_start, cpu_high_peak, 100, 100]

    fan_high_start = _clamp(fan_high - 15, 0, 100)
    fan_high_peak = _clamp(fan_high, 0, 100)
    adjusted["fan_noise"]["high"] = [fan_high_start, fan_high_peak, 100, 100]

    if "linux_tolerance" in adjustments:
        adjusted["cpu_usage"]["medium"] = _shift_range(
            adjusted["cpu_usage"]["medium"], -5, 0, 100
        )
    elif "windows_background_activity" in adjustments:
        adjusted["cpu_usage"]["medium"] = _shift_range(
            adjusted["cpu_usage"]["medium"], 2, 0, 100
        )

    return adjusted
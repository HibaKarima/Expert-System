# fuzzy/context.py

def get_context_config(brand, laptop_type, os_type, usage_type):

    config = {
        "temp_high_threshold": 80,
        "expected_cpu_usage": 70,
        "battery_expected_hours": 5
    }

    # Laptop Type Adjustments
    if laptop_type == "gaming":
        config["temp_high_threshold"] = 90
        config["expected_cpu_usage"] = 90

    elif laptop_type == "office":
        config["temp_high_threshold"] = 75
        config["expected_cpu_usage"] = 60

    # OS Adjustments
    if os_type == "linux":
        config["expected_cpu_usage"] -= 10

    # Brand Adjustments
    if brand == "ASUS":
        config["temp_high_threshold"] += 3

    elif brand == "Lenovo":
        config["temp_high_threshold"] -= 2

    return config
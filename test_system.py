import json

from fuzzy.inference import run_inference

# Load test cases
with open("data/test_cases.json", "r") as file:
    test_cases = json.load(file)

# Run tests
for case in test_cases:

    print("\n========================")
    print("TEST:", case["name"])
    print("========================")

    inputs = case["inputs"]

    result = run_inference(
        cpu_value=inputs["cpu"],
        ram_value=inputs["ram"],
        temp_value=inputs["temp"],
        disk_value=inputs["disk"],
        boot_value=inputs["boot"]
    )

    print("Inputs:")
    print(inputs)

    print("\nResults:")
    print(result)
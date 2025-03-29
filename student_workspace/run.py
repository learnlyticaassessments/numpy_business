# run.py

import importlib.util
import os

# Ensure the report.txt file exists in the same folder as run.py
report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "report.txt"))
if not os.path.exists(report_path):
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("")  # Create an empty file if it doesn't exist

# Correct the driver_path to ensure it resolves correctly
driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "secret_tests", "driver.py"))
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"Driver file not found at {driver_path}")

solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "solution.py"))
spec = importlib.util.spec_from_file_location("driver", driver_path)
driver_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver_module)

if __name__ == "__main__":
    # Pass the corrected solution_path and ensure report.txt is in the correct location
    driver_module.test_student_code(solution_path)

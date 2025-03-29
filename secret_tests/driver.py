import importlib.util
import datetime
import os

def test_student_code(solution_path):
    report_dir = os.path.join(os.path.dirname(__file__), "..", "student_workspace")
    report_path = os.path.join(report_dir, "report.txt")
    os.makedirs(report_dir, exist_ok=True)

    spec = importlib.util.spec_from_file_location("student_module", solution_path)
    student_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_module)

    SalesAnalyzer = student_module.SalesAnalyzer
    report_lines = [f"\n=== Test Run at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ==="]

    test_cases = [
        {
            "desc": "Total sales per product",
            "func": "product",
            "matrix": [[100, 200], [300, 400]],
            "expected": [300, 700]
        },
        {
            "desc": "Total sales per region",
            "func": "region",
            "matrix": [[100, 200], [300, 400]],
            "expected": [400, 600]
        },
        {
            "desc": "Best selling product",
            "func": "best",
            "matrix": [[50, 50], [300, 100]],
            "expected": (1, 400)
        },
        {
            "desc": "Normalized sales",
            "func": "norm",
            "matrix": [[50, 100], [150, 200]],
            "expected": [[0.25, 0.5], [0.75, 1.0]]
        },
        {
            "desc": "Hidden Test: Zero matrix normalization",
            "func": "norm",
            "matrix": [[0, 0], [0, 0]]
        }
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            analyzer = SalesAnalyzer(case["matrix"])
            if case["func"] == "product":
                result = analyzer.total_sales_per_product()
            elif case["func"] == "region":
                result = analyzer.total_sales_per_region()
            elif case["func"] == "best":
                result = analyzer.best_selling_product()
            elif case["func"] == "norm":
                result = analyzer.normalize_sales()
            else:
                result = "Invalid"

            if "expected" in case and result == case["expected"]:
                msg = f"✅ Test Case {i} Passed: {case['desc']} | Expected={case['expected']}, Actual={result}"
            elif "expected" in case:
                msg = f"❌ Test Case {i} Failed: {case['desc']} | Expected={case['expected']}, Got={result}"
            else:
                msg = f"✅ Test Case {i} Passed: {case['desc']}"
        except Exception as e:
            msg = f"❌ Test Case {i} Crashed: {case['desc']} | Error={str(e)}"
        print(msg)
        report_lines.append(msg)

    with open(report_path, "a", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n")

if __name__ == "__main__":
    solution_file = os.path.join(os.path.dirname(__file__), "..", "student_workspace", "solution.py")
    test_student_code(solution_file)
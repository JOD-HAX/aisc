"""Run all 23 interactive AISC programs using the reference sample inputs."""

import ast
from pathlib import Path
import subprocess
import sys


PROJECT = Path(__file__).resolve().parent

CASES = [
    ("01_Perceptron_Learning/01_discrete_perceptron_unipolar_binary.py", """4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
0
1
10
""", ["Final w = [2.0, 1.0] b = -2.0", "[1.0, 1.0] -> 1"]),
    ("01_Perceptron_Learning/02_discrete_perceptron_bipolar_binary.py", """4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
10
""", ["Final w = [2.0, 2.0] b = -2.0", "[1.0, 1.0] -> 1"]),
    ("01_Perceptron_Learning/03_continuous_perceptron_unipolar_sigmoid.py", """4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
0
1
5000
""", ["Stopped at epoch 552", "[1.0, 1.0] -> 0.911 class 1"]),
    ("01_Perceptron_Learning/04_continuous_perceptron_bipolar_tanh.py", """4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
5000
""", ["Stopped at epoch 83", "[1.0, 1.0] -> 0.92 class 1"]),
    ("02_Hebbian_Learning/05_hebbian_learning_unipolar_binary.py", """4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
-2.5
1
""", ["Final w = [1.0, 1.0] b = -1.5", "[1.0, 1.0] -> 1"]),
    ("02_Hebbian_Learning/06_hebbian_learning_bipolar_binary.py", """4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
""", ["Final w = [2.0, 2.0] b = -2.0", "[1.0, 1.0] -> 1"]),
    ("02_Hebbian_Learning/07_hebbian_learning_unipolar_continuous.py", """4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
-2.5
1
""", ["Final w = [1.0, 1.0] b = -1.5", "[1.0, 1.0] -> 0.622"]),
    ("02_Hebbian_Learning/08_hebbian_learning_bipolar_continuous.py", """4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
""", ["Final w = [2.0, 2.0] b = -2.0", "[1.0, 1.0] -> 0.762"]),
    ("03_Graph_Search/09_depth_limited_search.py", """7
S A B
A C D
B E
C
D G
E G
G
S
G
3
""", ["Limit 3 -> goal found, path = ['S', 'A', 'D', 'G']"]),
    ("03_Graph_Search/10_depth_first_iterative_deepening.py", """7
S A B
A C D
B E
C
D G
E G
G
S
G
10
""", ["Trying limit 3", "Goal found, path = ['S', 'A', 'D', 'G']"]),
    ("03_Graph_Search/11_hill_climbing.py", """7
S 5 A B
A 3 C D
B 4 E
C 4
D 1 G
E 2 G
G 0
S
G
""", ["Path = ['S', 'A', 'D', 'G']"]),
    ("03_Graph_Search/12_a_star_search.py", """7
S 6 A 1 B 4
A 5 C 3 D 1
B 3 E 2
C 4
D 5 G 6
E 1 G 1
G 0
S
G
""", ["Path = ['S', 'B', 'E', 'G']", "Total cost = 7.0"]),
    ("04_Game_Trees/13_minimax.py", "3 5 6 9 1 2 0 -1\n2\nmax\n", ["Value of root = 5.0"]),
    ("04_Game_Trees/14_alpha_beta_pruning.py", "3 5 6 9 1 2 0 -1\n2\nmax\n", ["Pruned remaining children", "Value of root = 5.0"]),
    ("05_Fuzzy_Sets_and_Defuzzification/15_fuzzy_set_operations.py", "0.2 0.5 0.7 1.0\n0.6 0.3 0.9 0.4\n", ["Algebraic sum     = [0.68, 0.65, 0.97, 1.0]", "Algebraic product = [0.12, 0.15, 0.63, 0.4]"]),
    ("05_Fuzzy_Sets_and_Defuzzification/16_fuzzy_relation_composition.py", "2\n0.6 0.3\n0.2 0.9\n1.0 0.5 0.3\n0.8 0.4 0.7\n", ["Max-Min composition     = [[0.6, 0.5, 0.3], [0.8, 0.4, 0.7]]", "Max-Product composition = [[0.6, 0.3, 0.21], [0.72, 0.36, 0.63]]"]),
    ("05_Fuzzy_Sets_and_Defuzzification/17_weighted_average_defuzzification.py", "2 5 8\n0.3 0.8 0.5\n", ["Weighted average x* = 5.375"]),
    ("05_Fuzzy_Sets_and_Defuzzification/18_centroid_defuzzification.py", "1 2 3 4 5 6 7 8\n0.1 0.3 0.6 1.0 0.8 0.5 0.4 0.2\n", ["Centroid x* = 4.59"]),
    ("05_Fuzzy_Sets_and_Defuzzification/19_centre_of_sum_defuzzification.py", "1 2 3 4 5 6 7 8\n0.2 0.6 1.0 0.6 0.2 0 0 0\n0 0 0 0.3 0.7 1.0 0.7 0.3\n", ["Centre of sum x* = 4.607"]),
    ("05_Fuzzy_Sets_and_Defuzzification/20_height_defuzzification.py", "1 2 3 4 5 6 7 8\n0.2 0.6 1.0 0.6 0.2 0 0 0\n0 0 0 0.3 0.7 1.0 0.7 0.3\n", ["Height method x* = 4.5"]),
    ("05_Fuzzy_Sets_and_Defuzzification/21_centre_of_area_defuzzification.py", "1 2 3 4 5 6 7 8\n0.1 0.3 0.6 1.0 0.8 0.5 0.4 0.2\n", ["Total area = 3.9 Half = 1.95", "Centre of area x* = 4.0"]),
    ("06_Competitive_Learning/22_winner_take_all_learning.py", """6
1 1
2 1
1 2
8 8
9 8
8 9
2
2 2
7 7
0.5
0.5
5
""", ["Final W = [[1.34, 1.44], [8.29, 8.39]]", "[8.0, 9.0] -> winner neuron 1"]),
    ("06_Competitive_Learning/23_learning_vector_quantization.py", """6
1 1 0
2 1 0
1 2 0
8 8 1
9 8 1
8 9 1
2
2 2 0
7 7 1
0.5
0.5
5
""", ["Final W = [[1.34, 1.44], [8.29, 8.39]]", "[8.0, 9.0] -> class 1"]),
]


def main():
    failures = []
    for relative_path, sample_input, expected_parts in CASES:
        path = PROJECT / relative_path
        if not path.is_file():
            failures.append(f"{relative_path}: missing file")
            print(f"[FAIL] {relative_path} - missing")
            continue

        source = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(path))
            compile(tree, str(path), "exec")
            doc = ast.get_docstring(tree) or ""
            if "Description:" not in doc or "Theory:" not in doc:
                raise ValueError("description/theory header missing")
        except Exception as error:
            failures.append(f"{relative_path}: {error}")
            print(f"[FAIL] {relative_path} - source validation")
            continue

        completed = subprocess.run(
            [sys.executable, str(path)],
            input=sample_input,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        missing_parts = [part for part in expected_parts if part not in completed.stdout]
        if completed.returncode != 0 or missing_parts:
            details = f"exit={completed.returncode}, missing={missing_parts}"
            if completed.stderr.strip():
                details += f", stderr={completed.stderr.strip()}"
            failures.append(f"{relative_path}: {details}")
            print(f"[FAIL] {relative_path}")
        else:
            print(f"[PASS] {relative_path}")

    if failures:
        print("\nVerification failed:")
        for failure in failures:
            print("-", failure)
        return 1

    print("\nVerification passed: 23/23 interactive programs matched the reference samples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

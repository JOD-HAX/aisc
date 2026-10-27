# AISC - 23 Simple, Interactive Python Practicals

This VS Code-ready project follows the supplied **AISC Practicals - Every Code Explained, With Sample Inputs** reference. All 23 programs now read their datasets and parameters using `input()`, so the examiner can change the values without requiring code edits.

Every program contains:

- its official experiment number and descriptive filename;
- a description and short theory section at the top;
- user-input prompts matching the reference PDF;
- standard-library-only Python code;
- output verified with the reference sample input.

The programs use short variable names, direct formulas, and only the minimum
logic needed for the practical. This makes them easier to type, understand,
explain in a viva, and revise before the exam.

## Six learning families

| Folder | Experiments | Core skeleton |
|---|---:|---|
| `01_Perceptron_Learning` | 01-04 | Error-correcting weight updates; discrete or continuous activation |
| `02_Hebbian_Learning` | 05-08 | One-pass co-activity update `w += c*t*x` |
| `03_Graph_Search` | 09-12 | DLS, DFID, hill climbing, and A* |
| `04_Game_Trees` | 13-14 | Min-Max and Alpha-Beta pruning |
| `05_Fuzzy_Sets_and_Defuzzification` | 15-21 | Fuzzy operations, relation composition, and five crisp-output methods |
| `06_Competitive_Learning` | 22-23 | Winner-Take-All and supervised LVQ |

## Run a practical in VS Code

1. Open this `AISC_23_Python_Practicals` folder in VS Code.
2. Open the required numbered `.py` file.
3. Click **Run Python File** or use the task **Run current Python practical**.
4. Type the requested values, pressing Enter after each prompt.

Example:

```powershell
python 01_Perceptron_Learning/01_discrete_perceptron_unipolar_binary.py
```

The exact input lines for every program are listed in [`SAMPLE_INPUTS.md`](SAMPLE_INPUTS.md). Copy one line at a time when working interactively, or paste the whole block into the terminal when redirected input is supported.

## Verify everything

```powershell
python verify_all.py
```

The verifier compiles all 23 programs, confirms every description/theory header, runs each program with the PDF's sample input, and checks its key expected output.

## Important practical notes

- Experiments 01-08 accept any consistent number of input features even though the prompt says `x1 x2` for the two-input sample gates.
- Graph experiments require a line for every node, including leaves.
- Min-Max and Alpha-Beta expect a full tree with the same branching factor at every internal node.
- Fuzzy vectors and matrices must have compatible lengths.
- Centre of Area (Experiment 21) implements the PDF's discrete bisector definition, while Experiment 18 implements the centroid.
- Winner-Take-All and LVQ may print identical results for the supplied sample because each input is already closest to a correctly labeled prototype.

# aisc-2026
# aisc

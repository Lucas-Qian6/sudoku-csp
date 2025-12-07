# Sudoku CSP Solver

A Sudoku solver implemented using **Constraint Satisfaction Problem (CSP)** ideas.

## Overview

We model Sudoku as a CSP:

- **Variables:** the 81 cells of the 9×9 grid  
- **Domains:** digits `1–9` for each cell  
- **Constraints:** all-different constraints for every row, column, and 3×3 subgrid  

The solver uses a **backtracking search** enhanced with:

- **Minimum Remaining Values (MRV)** heuristic for variable ordering  
- **Forward checking** to prune inconsistent values early  
- A simple value-ordering strategy for trying digits `1–9`

This code is adapted from a course homework environment.

---

## Files

- `sudoku.py` – main CSP-based Sudoku solver  
- `sudokus_start.txt` – example unsolved puzzles (one per line)  
- `sudokus_finish.txt` – example solved puzzles (for reference/testing)  
- `sudoku_tester.py` – simple tester script (if used)  

---

## Usage

```bash
python3 sudoku.py <input_string>
```

Where <input_string> is an 81-character string representing the Sudoku board
(row by row, left to right), using 0 for empty cells, e.g.: 

```bash
003020600900305001001806400008102900700000008006708200002609500800203009005010300
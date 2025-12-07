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

This code is adapted from a course homework environment, but this repository contains **only my own implementation of the core CSP solver logic**, not the original starter framework.

---

## Files

- `sudoku.py` – main CSP-based Sudoku solver  
- `sudokus_start.txt` – example unsolved puzzles (one per line)  
- `sudokus_finish.txt` – example solved puzzles (for reference/testing)  
- `sudoku_tester.py` – simple tester script (if used)  

You can trim or adjust this section depending on what you actually commit.

---

## Installation

This project only requires Python 3.

```bash
python3 --version
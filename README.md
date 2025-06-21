# Finding-Missing-Links

This project explores a directed graph built from student interactions during an experiment, where each student could note peers who impressed them. The analysis includes two main components:

- **Random Walk with Teleportation** (1.py): Identifies the most influential students using a PageRank-like algorithm.
- **Matrix-Based Missing Link Prediction** (2.py): Predicts plausible but unobserved connections using linear algebra.

---

## Project Overview

During the experiment, students answered questions and recorded (via Google Forms) the names of those whose answers impressed them. The resulting dataset is used to:

- Build a directed graph (nodes: students, edges: "impressed by" relationships)
- Analyze influence and centrality
- Predict missing links that may represent undiscovered or unrecorded connections

---

## Features

- **Directed Graph Construction** from Excel data
- **Random Walk with Teleportation** for influence ranking
- **PageRank Validation** for leaderboard accuracy
- **Matrix Method** for missing link prediction
- **Graph Visualization** before and after link prediction

---

## Requirements

- Python 3.x
- pandas
- networkx
- numpy
- matplotlib

Install dependencies with:
pip install pandas networkx numpy matplotlib

---

## File Structure
```
project/
├── 1.py # Random Walk with Teleportation & Leaderboard
├── 2.py # Matrix Method for Missing Link Prediction
├── modified.xlsx # Input data (student impressions)
├── Project2.pdf 
└── README.md
```
---

## Usage

### 1. Prepare Your Data

- Place your impression data in `modified.xlsx`.
- The first column should contain student entry numbers.
- Each row lists the students that the row’s student was impressed by.

### 2. Run the Random Walk Leaderboard (1.py)

  python 1.py
- Reads the Excel file, builds the directed graph, and simulates a random walk with teleportation (0.85 probability) for 1,000,000 steps.
- Outputs a list of students (entry numbers) ranked by influence.

### 3. Run the Missing Link Prediction (2.py)

  python 2.py
- Builds the adjacency matrix, applies the matrix method to predict missing links, and visualizes the enhanced graph.
- Prints the final adjacency matrix and shows the graph (with both original and predicted edges).

---

## How the Analysis Works

### Random Walk with Teleportation (1.py)

- Simulates a random walker moving through the network.
- With 85% probability, moves to a neighbor; with 15%, teleports to a random node.
- The frequency of visits to each node determines its influence score.
- Closely matches results from the classic PageRank algorithm.

### Matrix Method for Missing Link Prediction (2.py)

- Constructs the adjacency matrix from the graph.
- For each possible missing edge, uses least-squares linear algebra to estimate the likelihood of a connection.
- If the computed score exceeds a threshold (0.4), the link is predicted as present.
- Produces a new graph including these predicted links, visualized for analysis.

---

## Example

Suppose your `modified.xlsx` looks like:

| EntryNumber | ImpressedBy1 | ImpressedBy2 |
|-------------|--------------|--------------|
| 2023CSB1001 | 2023CSB1002  | 2023CSB1003  |
| 2023CSB1002 | 2023CSB1003  |              |
| 2023CSB1003 |              |              |

- `1.py` will output a ranked list of entry numbers by influence.
- `2.py` will print the adjacency matrix and display the enhanced graph with predicted links.

---

## Customization

- **Threshold for Link Prediction:** Adjust the `0.4` value in `2.py` for stricter or looser link prediction.
- **Random Walk Steps:** Change `numsteps` in `1.py` for speed vs. accuracy trade-off.

---

## Results & Insights

- **Influence Analysis:** Identifies central and influential students in the network.
- **Link Prediction:** Suggests plausible connections that may have been missed in the original data.
- **Visualization:** Provides before/after network graphs for deeper insight.

---

**Tip:**  
Ensure your Excel file is clean and formatted as described for best results.

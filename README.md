
#  K-Means Clustering with Manhattan Distance

## Introduction
This project implements a modified version of the traditional K-Means clustering algorithm using Python.  
Instead of using the regular Euclidean distance, this version uses the **Manhattan distance** to calculate how close points are to their respective cluster centers.  

Additionally, it generates **random Cartesian points and cluster centers**, organizes them in a CSV file, and provides a simple 2D visualization using the `print()` function only.

---

## Features
- Random generation of **100 data points** and **10 initial cluster centers**.
- Reads points and centers from a **CSV file**.
- Uses **Manhattan Distance** for clustering instead of Euclidean.
- Simple **matrix-based visualization** of clusters printed to the console.
- No external plotting libraries used.

---

## How It Works
1. **Data Generation**:  
   A `data.csv` file is created containing 100 points and 10 cluster centers. Each point or center has random `(x, y)` coordinates between 0 and 49.

2. **Reading the Data**:  
   Points and centers are read from `data.csv` and stored separately.

3. **K-Means Clustering**:
   - Each point is assigned to the nearest cluster based on Manhattan distance.
   - Cluster centers are updated as the mean of all points assigned to them.
   - This process repeats until the centers no longer move (convergence).

4. **Visualization**:
   - A 2D matrix (50×50) is printed.
   - Different symbols are used to represent data points and cluster centers.

---

## Manhattan Distance
In this project, the **Manhattan Distance** between two points `(x1, y1)` and `(x2, y2)` is calculated as:
```
distance = |x1 - x2| + |y1 - y2|
```
This distance is more appropriate for grid-like paths and is simpler compared to Euclidean distance.

---

## File Structure
| File Name | Purpose |
|:---|:---|
| `data.csv` | Contains all randomly generated points and cluster centers |
| `kmeans.py` | Main script to run the clustering algorithm and visualization |

---

## Requirements
- Python 3.x
- No external libraries required except:
  - `csv` (built-in)
  - `random` (built-in)

---

## How to Run
1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python kmeans.py
   ```
3. Follow the prompts if necessary.
4. The 2D matrix visualization will be printed on the terminal after clustering.

---

## Notes
- The points are randomly generated within a 50x50 grid every time you run the data generator.
- The Manhattan distance makes clustering behavior slightly different compared to normal K-Means.
- The visualization is basic (only printed output), but enough to get an idea of cluster distribution.

---

## Author
This project was developed as part of a machine learning practice task to explore clustering algorithms with custom distance metrics and basic visualization.

---

#  Sample Output
```
. . . . 2 . . 2 . 1 .
. 1 . . 2 . . . . . .
. . . 1 . . 2 2 . 2 .
. . . . . . . 2 2 . .
1 . . . . 1 2 2 . . .
...
```
(Here numbers represent different cluster IDs.)

---

---


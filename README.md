# K-Means Clustering with Elbow Method

This project demonstrates **unsupervised learning** using the **K-Means Clustering** algorithm, along with the **Elbow Method** to determine the optimal number of clusters. It's implemented in Python from scratch using basic libraries like NumPy and matplotlib.

## 📌 Features

- Custom implementation of the K-Means clustering algorithm
- Elbow Method to visualize the ideal number of clusters (k)
- Simple and easy-to-read Python scripts
- Includes visual output to support analysis

## 🧠 Concepts Covered

- Unsupervised Learning
- Clustering Algorithms
- K-Means from Scratch
- Elbow Method for Optimal K Selection
- Random initialization of centroids

## 🗂️ Files

| File              | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| `kmeans.py`       | Implements the K-Means algorithm with random initialization |
| `elbow_method.py` | Uses the Elbow Method to find the best `k` value            |

## 🚀 How to Run

1. Clone this repo:

```bash
git clone https://github.com/yourusername/kmeans-elbow-method.git
cd unsupervised_learning
pip install numpy
python elbow_method.py
python kmeans.py
```

## Output

The Elbow Method will plot a graph showing distortion vs. number of clusters.
K-Means will show final clusters and centroids

## 🔮 Future Development

- 📈 **MATLAB Visualization**: Currently, all outputs are displayed in the terminal. A MATLAB version is planned to create more interactive and visually rich representations of the clusters and Elbow Method results.
- ⚙️ **GUI (Optional)**: Explore building a lightweight graphical user interface (with Tkinter) to allow users to load their own data and see clustering results visually.

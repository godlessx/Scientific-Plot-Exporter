# Scientific Plot Exporter

## Description

This project demonstrates how to create and export multiple mathematical graphs using Python, NumPy, and Matplotlib.

The program generates four different mathematical functions and displays them in separate subplots within a single figure.

## Functions

The project visualizes:

- Sine: `sin(x)`
- Cosine: `cos(x)`
- Tangent: `tan(x)`
- Exponential Decay: `exp(-x)`

## Features

- Generates four mathematical functions using NumPy.
- Creates multiple subplots using `plt.subplots()`.
- Adds legends and grid lines.
- Organizes plots using `fig.tight_layout()`.
- Automatically saves the figure as a PNG image.
- Exports images with 300 DPI resolution.

## Technologies Used

- Python 3
- NumPy
- Matplotlib

## Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command in your terminal:

```bash
python main.py
```

The program will display the four graphs and automatically save the visualization as:

`graphs.png`

## What I Learned

- Working with NumPy arrays.
- Creating multiple subplots.
- Understanding the Figure and Axes objects.
- Using Matplotlib's object-oriented interface.
- Adding legends, titles, and grid lines.
- Saving figures using `savefig()`.
- Adjusting image resolution using DPI.

## Future Improvements

- Add individual graph customization.
- Improve tangent visualization around asymptotes.
- Allow users to choose which functions to display.
- Export individual graphs into separate image files.
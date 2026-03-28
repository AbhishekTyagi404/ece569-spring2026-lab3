# Create the README.md file with the provided content

content = """# ECE 569 Lab 3 – Step 1 (Python)

## Overview
This repository contains the Python work for Step 1 of Lab 3. The notebook reads motion capture data of the Metafly and generates plots for position, velocity, orientation, angular velocity, and an error metric.

All computations use NumPy, and plots are created using Matplotlib inside a Jupyter Notebook.

---

## Files

- `Lab3_Robotics.ipynb`  
  Main notebook with all code and plots

- `Step1.py`  
  Contains required functions:
  - so3ToVec  
  - VecToso3  
  - AxisAng3  
  - MatrixLog3  
  - data handling and plotting functions  

- `tests.py`  
  Test file to verify function outputs  

- `mocap_data.csv`  
  Input dataset  

---

## How to Run

### Using Jupyter Notebook
1. Open Anaconda Prompt  
2. Go to the project folder  

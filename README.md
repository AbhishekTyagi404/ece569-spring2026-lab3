# ECE 569 – Lab 3

## Overview
This repository contains the work for Lab 3. The lab focuses on processing motion capture data and visualizing the Metafly using ROS.

---

## Repository Structure

- **Step1/**  
  Python implementation using NumPy and Matplotlib  
  Includes Jupyter Notebook, functions, and plots  

- **Step2/**  
  ROS-based visualization using RViz  
  Includes TF publisher and launch setup  

- **ws3/**  
  ROS workspace used for building and running Step 2  

---

## Getting Started

Clone the repository:

```
git clone https://github.com/AbhishekTyagi404/ece569-spring2026-lab3.git
cd ece569-spring2026-lab3/Lab3
```

---

## Step 1

- Implemented in Python  
- Uses Jupyter Notebook  
- Generates:
  - Position plots  
  - Velocity plots  
  - Orientation plots  
  - Angular velocity  
  - Error metric  

Refer to the README inside `Step1/` for details.

---

## Step 2

- Uses ROS 2 and RViz  
- Visualizes Metafly motion using mocap data  
- Publishes transforms between `world` and `base_link`  

To run:

```
cd ws3
colcon build --symlink-install
source install/setup.bash
ros2 launch metafly.launch.py
```

Enable **Show Trail** for `base_link` in RViz.

---

## Notes

- Step 1 and Step 2 can be done independently  
- All required outputs are included in the repository  
- Test cases for Step 1 pass successfully  

---

## Author

Abhishek Tyagi  
tyagi55@purdue.edu

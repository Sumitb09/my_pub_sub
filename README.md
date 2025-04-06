# my_pub_sub

A basic example of the Publisher/Subscriber (Pub/Sub) model using **ROS 2 (Robot Operating System 2)**. This project demonstrates how to create a simple ROS 2 package with Python nodes for publishing and subscribing to messages.

## 🚀 Features

- Simple ROS 2 Python package structure
- Publisher node: publishes messages at a fixed interval
- Subscriber node: listens and logs received messages
- Includes setup and packaging configuration

## 🧾 Requirements

- ROS 2 (Humble, Foxy, or other compatible distributions)
- Python 3.8+
- Colcon build system

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Sumitb09/my_pub_sub.git
cd my_pub_sub

# Source your ROS 2 environment
source /opt/ros/<distro>/setup.bash

# Build the package
colcon build --packages-select my_pub_sub

# Source the workspace
source install/setup.bash

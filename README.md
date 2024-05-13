# Catan Simulation in Python

A Settlers of Catan simulator for AI bots written in Python.

## Overview

This repository contains a Python-based simulator for the board game Settlers of Catan. It is designed to test and refine AI bots in a simulated environment. Users can execute predefined bots, as well as introduce their own custom bots into the game.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. The simulation is compatible with Python 3.x.

### Adding Your Bots

1. Navigate to the `Bots` folder.
2. Place your custom bot module or Python file in this folder.
3. Ensure your bot class is correctly defined within the module.

### Running the Simulator

To run the simulator, use the `main` module. Specify the bots to be executed and the number of games to be played. Each bot should be referenced by the module or file name, followed by a dot, and then the class name (e.g., `mymodule.myclass`).

### Results

After each game, the result is displayed in the console and the game trace is saved in JSON format in the `Traces` folder.

## Visualizing Results

To visualize game results:
1. Open the `index.html` file located in the `Visualizer` folder.
2. Load a JSON trace file by clicking on the three-dot icon located in the controls below the right side of the Catan board.

<img src="assets/visualizer_screenshot.png" width="900" alt="Screenshot of the visualizer">


## Contributing

Contributions to the Catan Simulation in Python are welcome! Please feel free to make changes and submit pull requests.

# Python Simulation Project

## About the Project

This project is a collection of Python simulation activities that I created while learning about **simulation and modeling**.

The main project is a **Student Registration Simulation** using **SimPy**. Ginawa ko ito to simulate how students arrive at a registration area and how their waiting time changes depending on the number of available counters.

## Main Simulation: Student Registration

The simulation compares different numbers of registration counters:

* 1 counter
* 2 counters
* 3 counters
* 4 counters
* 5 counters

Each setup is tested multiple times using different random conditions. The main focus is to observe the **average waiting time** and **maximum waiting time** of the students.

Based on the simulation, adding more counters generally reduces the waiting time of students. This helps show how simulation can be used to test a real-life situation before making an actual decision.

## Other Simulation

The project also contains a **Population Growth Simulation**, which demonstrates how a population changes over time using a fixed growth rate.

## Technologies Used

* Python
* SimPy
* NumPy
* Matplotlib
* Pandas
* SciPy
* Jupyter Notebook

## Project Structure

```text
python-simulation/
│
├── data/
├── notebooks/
├── src/
│   └── models/
│       └── registration_simulation.py
├── tests/
├── population_simulation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

First, activate the virtual environment and install the required libraries.

Then run the registration simulation:

```bash
python src/models/registration_simulation.py
```

The program will display the simulation results and compare the waiting times for different numbers of counters.

## Learning Outcome

Through this project, I learned how simulation can be used to represent a real-world process using Python. I also learned how changing variables, such as the number of counters, can affect the result of a simulation.

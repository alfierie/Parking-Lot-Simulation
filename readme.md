# Parking Lot Simulation using Streamlit and SimPy

## Overview

This project is a stochastic simulation of a parking lot system developed for the Stochastic Modeling and Simulation course.

The simulation models vehicle arrivals, parking occupancy, waiting queues, and vehicle departures under uncertain conditions. Users can interactively modify system parameters and observe how the parking lot performance changes in real time.

## Features

* Interactive Streamlit dashboard
* Stochastic vehicle arrivals using Poisson processes
* Random parking durations using Normal distributions
* Real-time parking occupancy visualization
* Queue length monitoring
* Performance statistics
* Sensitivity analysis for different parking capacities

## Stochastic Components

### Vehicle Arrivals

Vehicle arrivals are modeled using a Poisson process:

* Arrival Rate (λ): Vehicles per hour
* Inter-arrival times follow an Exponential Distribution

### Parking Duration

Parking duration is modeled using a Normal Distribution:

* Mean parking duration configurable by user
* Standard deviation = 20% of mean duration

### Queueing System

When the parking lot is full:

* Vehicles enter a waiting queue
* Vehicles are served on a First-Come-First-Served basis

## Technologies Used

* Python
* Streamlit
* SimPy
* Pandas
* Plotly

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/parking-lot-simulation.git
cd parking-lot-simulation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Adjustable Parameters

* Parking Capacity
* Vehicle Arrival Rate
* Average Parking Duration
* Simulation Duration

## Performance Metrics

The simulation reports:

* Total Vehicles Arrived
* Vehicles Served
* Average Waiting Time
* Maximum Queue Length
* Parking Occupancy Rate

## Sensitivity Analysis

Users can compare system performance under different parking capacities:

* Small Parking Lot
* Medium Parking Lot
* Large Parking Lot

This helps identify the optimal parking capacity while balancing utilization and waiting times.

## Project Structure

```text
parking-lot-simulation/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Authors

Group Members:

* Student 1
* Student 2
* Student 3

Universitas Gadjah Mada

## License

This project is developed for educational purposes.

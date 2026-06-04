# Parking Lot Simulation

An interactive stochastic simulation of a parking lot system built with Streamlit for the **Stochastic Modeling and Simulation** course.

The simulation models vehicle arrivals, parking occupancy, and vehicle departures under uncertainty. Users can modify parameters in real time and observe how the parking lot behaves through a live animated visualization.

---

## Project Overview

Parking facilities experience uncertain vehicle arrivals and departures throughout the day. Understanding how these stochastic factors affect occupancy can help managers optimize parking capacity and improve user experience.

This project simulates a parking lot where:

* Vehicles arrive randomly
* Parking durations vary randomly
* Parking spaces are limited
* Occupancy changes dynamically over time

The simulation allows users to experiment with different scenarios and observe their effects immediately.

---

## Objectives

* Model a real-world parking lot using stochastic processes
* Visualize parking occupancy through animation
* Analyze the impact of arrival rates and parking durations
* Demonstrate the use of simulation for decision making

---

## ⚙️ Features

### Interactive Controls

Users can adjust:

* Parking Capacity
* Vehicle Arrival Probability
* Average Parking Duration
* Simulation Length
* Animation Speed

### Live Animation

The parking lot updates in real time:

* 🟩 Empty Parking Space
* 🚗 Occupied Parking Space

Vehicles continuously enter and leave the parking lot during the simulation.

### Real-Time Metrics

The dashboard displays:

* Current Occupancy
* Occupancy Percentage
* Total Vehicle Arrivals
* Total Vehicle Departures

### Dynamic Visualization

* Live parking lot animation
* Occupancy trend chart
* Performance monitoring dashboard

---

## Stochastic Modeling

### Vehicle Arrivals

Vehicle arrivals are modeled probabilistically.

At each simulation step:

* A vehicle may arrive based on the selected arrival probability.
* Higher probabilities produce busier parking lots.

### Parking Duration

Parking durations are generated randomly using a Normal Distribution:

Duration ~ Normal(Mean Duration, 0.3 × Mean Duration)

This reflects real-world variability in parking behavior.

---

## Technologies Used

* Python
* Streamlit
* Pandas

---

## Project Structure

```text
parking-lot-simulation/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

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

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## Example Insights

Using the simulation, users can investigate questions such as:

* How many parking spaces are needed?
* What happens during peak traffic periods?
* How does parking duration affect occupancy?
* At what point does the parking lot become saturated?

---

## Academic Context

This project was developed as part of a Stochastic Modeling and Simulation course assignment.

The project demonstrates:

* Stochastic system modeling
* Random event simulation
* Interactive visualization
* Sensitivity analysis
* Data-driven decision making

---

## Team Members

Replace with your actual group members:

Diffie Alfierie Iswanto - 24/533049/TK/59056

---

## License

This project is intended for educational purposes only.

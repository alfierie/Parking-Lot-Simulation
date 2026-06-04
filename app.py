import streamlit as st
import pandas as pd
import plotly.express as px
import random
import simpy

st.set_page_config(
    page_title="Parking Lot Simulation",
    layout="wide"
)

st.title("🚗 Parking Lot Simulation")
st.markdown(
    """
    Stochastic Modeling and Simulation Project

    Vehicle arrivals follow a Poisson process while parking durations
    follow a Normal distribution.
    """
)

# =====================================
# Sidebar Parameters
# =====================================

st.sidebar.header("Simulation Parameters")

capacity = st.sidebar.slider(
    "Parking Capacity",
    10,
    200,
    50
)

arrival_rate = st.sidebar.slider(
    "Arrival Rate (vehicles/hour)",
    5,
    100,
    30
)

avg_parking_time = st.sidebar.slider(
    "Average Parking Duration (minutes)",
    30,
    300,
    120
)

simulation_hours = st.sidebar.slider(
    "Simulation Duration (hours)",
    1,
    24,
    8
)

# =====================================
# Statistics
# =====================================

stats = {
    "arrived": 0,
    "served": 0,
    "wait_times": [],
    "occupancy_history": [],
    "queue_history": []
}

# =====================================
# Vehicle Process
# =====================================

def vehicle(env, name, parking_lot):

    arrival_time = env.now

    stats["arrived"] += 1

    with parking_lot.request() as request:

        yield request

        wait_time = env.now - arrival_time
        stats["wait_times"].append(wait_time)

        stats["served"] += 1

        duration = max(
            10,
            random.normalvariate(
                avg_parking_time,
                avg_parking_time * 0.2
            )
        )

        yield env.timeout(duration)

# =====================================
# Arrival Generator
# =====================================

def vehicle_generator(env, parking_lot):

    counter = 0

    while True:

        interarrival = random.expovariate(
            arrival_rate / 60
        )

        yield env.timeout(interarrival)

        counter += 1

        env.process(
            vehicle(
                env,
                f"Car {counter}",
                parking_lot
            )
        )

# =====================================
# Monitoring Process
# =====================================

def monitor(env, parking_lot):

    while True:

        occupancy = len(parking_lot.users)

        stats["occupancy_history"].append({
            "time": env.now,
            "occupancy": occupancy
        })

        stats["queue_history"].append({
            "time": env.now,
            "queue": len(parking_lot.queue)
        })

        yield env.timeout(5)

# =====================================
# Run Simulation
# =====================================

if st.button("Run Simulation"):

    env = simpy.Environment()

    parking_lot = simpy.Resource(
        env,
        capacity=capacity
    )

    env.process(
        vehicle_generator(
            env,
            parking_lot
        )
    )

    env.process(
        monitor(
            env,
            parking_lot
        )
    )

    env.run(
        until=simulation_hours * 60
    )

    avg_wait = (
        sum(stats["wait_times"])
        / len(stats["wait_times"])
        if stats["wait_times"]
        else 0
    )

    occupancy_df = pd.DataFrame(
        stats["occupancy_history"]
    )

    queue_df = pd.DataFrame(
        stats["queue_history"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Vehicles Arrived",
        stats["arrived"]
    )

    col2.metric(
        "Vehicles Served",
        stats["served"]
    )

    col3.metric(
        "Average Wait (min)",
        round(avg_wait, 2)
    )

    col4.metric(
        "Max Queue",
        queue_df["queue"].max()
    )

    st.subheader("Parking Occupancy")

    fig_occ = px.line(
        occupancy_df,
        x="time",
        y="occupancy",
        title="Occupancy Over Time"
    )

    st.plotly_chart(
        fig_occ,
        use_container_width=True
    )

    st.subheader("Queue Length")

    fig_queue = px.line(
        queue_df,
        x="time",
        y="queue",
        title="Queue Length Over Time"
    )

    st.plotly_chart(
        fig_queue,
        use_container_width=True
    )

    st.subheader("Current Parking Lot")

    occupied = min(
        occupancy_df["occupancy"].iloc[-1],
        capacity
    )

    rows = 10
    cols = max(1, capacity // rows)

    count = 0

    for _ in range(rows):

        columns = st.columns(cols)

        for col in columns:

            if count < occupied:
                col.markdown("🟥")
            else:
                col.markdown("🟩")

            count += 1

            if count >= capacity:
                break

        if count >= capacity:
            break

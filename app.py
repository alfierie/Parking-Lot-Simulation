import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="Parking Lot Simulation",
    layout="wide"
)

st.title("🚗 Parking Lot Simulation")
st.markdown(
    """
    Interactive stochastic parking lot simulation.

    Vehicle arrivals are random and parking durations vary.
    Watch vehicles enter and leave the parking lot in real time.
    """
)

# =====================================================
# Sidebar Controls
# =====================================================

st.sidebar.header("Simulation Parameters")

capacity = st.sidebar.slider(
    "Parking Capacity",
    min_value=20,
    max_value=200,
    value=50,
    step=10
)

arrival_probability = st.sidebar.slider(
    "Arrival Probability",
    min_value=0.01,
    max_value=0.50,
    value=0.15,
    step=0.01
)

avg_parking_duration = st.sidebar.slider(
    "Average Parking Duration (steps)",
    min_value=5,
    max_value=50,
    value=20
)

simulation_steps = st.sidebar.slider(
    "Simulation Steps",
    min_value=50,
    max_value=500,
    value=200
)

speed = st.sidebar.slider(
    "Animation Speed (seconds)",
    min_value=0.05,
    max_value=1.0,
    value=0.20,
    step=0.05
)

# =====================================================
# Start Button
# =====================================================

if st.button("▶ Start Simulation"):

    parking_slots = [None] * capacity

    occupancy_history = []

    total_arrivals = 0
    total_departures = 0

    stats_placeholder = st.empty()
    parking_placeholder = st.empty()
    chart_placeholder = st.empty()

    for current_step in range(simulation_steps):

        # -----------------------------------------
        # Cars leaving
        # -----------------------------------------

        for i in range(capacity):

            if parking_slots[i] is not None:

                parking_slots[i] -= 1

                if parking_slots[i] <= 0:
                    parking_slots[i] = None
                    total_departures += 1

        # -----------------------------------------
        # New arrival
        # -----------------------------------------

        if random.random() < arrival_probability:

            total_arrivals += 1

            empty_slots = [
                i for i, slot in enumerate(parking_slots)
                if slot is None
            ]

            if empty_slots:

                chosen_slot = random.choice(empty_slots)

                duration = max(
                    1,
                    int(
                        random.normalvariate(
                            avg_parking_duration,
                            avg_parking_duration * 0.3
                        )
                    )
                )

                parking_slots[chosen_slot] = duration

        # -----------------------------------------
        # Statistics
        # -----------------------------------------

        occupied = sum(
            slot is not None
            for slot in parking_slots
        )

        occupancy_rate = (
            occupied / capacity
        ) * 100

        occupancy_history.append(
            occupancy_rate
        )

        # -----------------------------------------
        # Metrics
        # -----------------------------------------

        stats_placeholder.columns(4)

        col1, col2, col3, col4 = stats_placeholder.columns(4)

        col1.metric(
            "Occupied",
            occupied
        )

        col2.metric(
            "Occupancy %",
            f"{occupancy_rate:.1f}"
        )

        col3.metric(
            "Arrivals",
            total_arrivals
        )

        col4.metric(
            "Departures",
            total_departures
        )

        # -----------------------------------------
        # Parking Lot Visualization
        # -----------------------------------------

        grid_html = """
        <div style='font-size:35px; line-height:1.6'>
        """

        columns = 10

        for i in range(capacity):

            if parking_slots[i] is None:
                grid_html += "🟩"
            else:
                grid_html += "🚗"

            if (i + 1) % columns == 0:
                grid_html += "<br>"

        grid_html += "</div>"

        parking_placeholder.markdown(
            f"""
            ### Parking Lot Animation

            🚪 Entrance

            {grid_html}
            """,
            unsafe_allow_html=True
        )

        # -----------------------------------------
        # Occupancy Chart
        # -----------------------------------------

        chart_df = pd.DataFrame({
            "Occupancy %": occupancy_history
        })

        chart_placeholder.line_chart(
            chart_df
        )

        time.sleep(speed)

    st.success("Simulation Complete!")

# Ride-Hailing-Transaction-Strategy-Simulation
##1. overview
This project simulates a simplified ride-hailing platform (e.g. Meituan / Didi), focusing on transaction strategy design, including demand–supply matching, pricing incentives, and performance evaluation.
The goal is to study how different algorithmic strategies affect:
- Order fulfillment rate
- User waiting time
- Driver utilization
- Platform revenue proxy

---

## 2. Problem Background
Ride-hailing platforms face a classic demand–supply imbalance problem:
- Users want fast, cheap, reliable rides
- Drivers want higher income and shorter idle time
- The platform aims to maximize transaction efficiency and growth

This project abstracts the above into a simulation environment
and evaluates different transaction strategies.

---

## 3. System Design
The system consists of:
- Users generating ride requests
- Drivers distributed in a 2D city grid
- A matching engine assigning drivers to users
- Strategy modules controlling matching and pricing logic

---

## 4. Data Schema
All data are simulated to resemble real ride-hailing scenarios.

### 4.1 User
- user_id
- location (x, y)
- price_sensitivity
- patience_time

### 4.2 Driver
- driver_id
- location (x, y)
- vehicle_type
- availability

### 4.3 Order
- order_id
- user_id
- request_time
- trip_distance
- base_price
- subsidy
- assigned_driver_id
- accepted (0/1)

---

## 5. Strategy Modules
Implemented strategies include:
- Distance-based matching
- Waiting-time-aware matching
- Utility-based matching
- Subsidy-influenced acceptance modeling

---

## 6. Evaluation Metrics
Strategies are evaluated using:
- Order fulfillment rate
- Average waiting time
- Driver idle rate
- Revenue proxy

---

## 7. Experiments & Results
Multiple strategies are compared under identical demand–supply conditions.
Results show clear trade-offs between efficiency and cost.

---

## 8. Tech Stack
- Python
- NumPy / Pandas
- Matplotlib / Seaborn

---

## 9. Future Improvements
- Dynamic pricing
- Reinforcement learning-based strategy
- Causal evaluation (A/B testing)

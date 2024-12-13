import numpy as np

# Inputs
N = 5  # Number of base stations (example)
T = 10  # Time steps (example)
Umax = 100  # Maximum load per base station
L = 0.2  # Light sleep threshold (example)
acceptable_delay = 0.05  # Example acceptable delay

# Arrival and departure probabilities modeled using a Poisson process
arrival_lambda = 3  # Example arrival rate parameter
departure_lambda = 2  # Example departure rate parameter
vi = np.random.poisson(arrival_lambda, N) / 10  # Normalize to probabilities
wi = np.random.poisson(departure_lambda, N) / 10  # Normalize to probabilities

# Helper Functions
def J(ui, uj):
    # Decision function for deep sleep
    P_ui = ui / Umax
    P_uj = uj / Umax
    return P_ui + P_uj - (P_ui + P_uj)**2

def update_load(ui, arrivals, departures):
    return max(0, ui + arrivals - departures)

def transition_to_sleep(state, delay):
    if state < L and delay < acceptable_delay:
        return "Light Sleep"
    return "Deep Sleep"

# Initialization
X = np.zeros((T + 1, N))  # State of each base station over time
c_values = np.random.rand(T)  # Random parameter c for each time step

for t in range(1, T + 1):
    for i in range(N):
        c = c_values[t - 1]

        # User activity decisions
        if sum(vi[:i]) < c <= sum(vi[:i + 1]):  # User arrival at base station i
            if X[t - 1, i] == 0:  # Case 1: Base station is empty
                neighbors = [j for j in range(N) if j != i]
                max_j = max(neighbors, key=lambda j: J(1, X[t - 1, j]))
                if J(1, X[t - 1, max_j]) > 0:
                    X[t, max_j] += 1
                else:
                    X[t, i] = 1
            elif X[t - 1, i] + 1 > Umax:  # Case 2: Load exceeds capacity
                neighbors = [j for j in range(N) if X[t - 1, j] == 0]
                k = len(neighbors)
                if k > 0:
                    load_distribution = (X[t - 1, i] + 1) / (k + 1)
                    for j in neighbors:
                        X[t, j] = load_distribution
                    X[t, i] = load_distribution
            else:  # Case 3: Load within capacity
                X[t, i] = X[t - 1, i] + 1

        elif sum(vi) + sum(wi[:i]) < c <= sum(vi) + sum(wi[:i + 1]):  # User departure
            if X[t - 1, i] > 0:
                X[t, i] = max(0, X[t - 1, i] - 1)

        else:  # No user activity
            X[t, i] = X[t - 1, i]

        # Sleep transition evaluation
        load_ratio = X[t, i] / Umax
        if load_ratio < L:
            state = transition_to_sleep(load_ratio, delay=0.1)  # Placeholder for delay calculation
            if state == "Light Sleep":
                print(f"Base station {i} enters light sleep at time {t}.")
            elif state == "Deep Sleep":
                print(f"Base station {i} enters deep sleep at time {t}.")

# Output the final states
print("Final network state:")
print(X)

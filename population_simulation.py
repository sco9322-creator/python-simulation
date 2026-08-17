import numpy as np
import matplotlib.pyplot as plt

def population_growth_simulation(initial_pop, growth_rate, time_steps):
    """
    Simulate exponential population growth
    """
    population = [initial_pop]
    
    for t in range(1, time_steps):
        new_pop = population[-1] * (1 + growth_rate)
        population.append(new_pop)
    
    return population


# Run simulation
initial_population = 100
growth_rate = 0.05  # 5% growth per time step
time_steps = 50

results = population_growth_simulation(
    initial_population,
    growth_rate,
    time_steps
)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(time_steps), results, 'b-', linewidth=2)
plt.xlabel('Time Steps')
plt.ylabel('Population')
plt.title('Population Growth Simulation')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Initial population: {initial_population}")
print(f"Final population: {results[-1]:.2f}")
print(f"Growth factor: {results[-1]/initial_population:.2f}x")
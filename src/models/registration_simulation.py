import simpy
import random


def student(env, name, arrival_time, service_time, counter, waiting_times):
    # Wait until the student's arrival time
    yield env.timeout(arrival_time - env.now)

    actual_arrival_time = env.now

    # Request a registration counter
    with counter.request() as request:
        yield request

        # Calculate waiting time
        start_time = env.now
        waiting_time = start_time - actual_arrival_time

        waiting_times.append(waiting_time)

        # Registration/service
        yield env.timeout(service_time)


def run_simulation(number_of_counters, seed):
    # Set the random seed for this trial
    random.seed(seed)

    # Create simulation environment
    env = simpy.Environment()

    # Create registration counters
    counter = simpy.Resource(
        env,
        capacity=number_of_counters
    )

    # Store waiting times
    waiting_times = []

    # Store arrival time
    current_arrival_time = 0

    # Create 10 students
    for i in range(1, 201):

        # Random arrival interval: 1–3 minutes
        arrival_interval = random.uniform(0.5, 1.5)
        current_arrival_time += arrival_interval

        # Random registration time: 3–7 minutes
        service_time = random.uniform(3, 7)

        # Add student to simulation
        env.process(
            student(
                env,
                f"Student {i}",
                current_arrival_time,
                service_time,
                counter,
                waiting_times
            )
        )

    # Run simulation
    env.run()

    # Calculate results
    average_wait = sum(waiting_times) / len(waiting_times)
    maximum_wait = max(waiting_times)
    minimum_wait = min(waiting_times)

    return average_wait, maximum_wait, minimum_wait


def main():

    # Number of trials
    number_of_trials = 10

    # Counter configurations
    counter_configurations = [1, 2, 3, 4, 5]

    # Store results
    results = {}

    print("=" * 60)
    print("STUDENT REGISTRATION SIMULATION")
    print("=" * 60)

    # Run each counter configuration
    for counters in counter_configurations:

        average_waits = []
        maximum_waits = []
        minimum_waits = []

        print(f"\n--- {counters} COUNTER(S) ---")

        # Run 10 trials
        for trial in range(1, number_of_trials + 1):

            average, maximum, minimum = run_simulation(
                counters,
                seed=trial
            )

            average_waits.append(average)
            maximum_waits.append(maximum)
            minimum_waits.append(minimum)

            print(
                f"Trial {trial}: "
                f"Average = {average:.2f} min | "
                f"Max = {maximum:.2f} min | "
                f"Min = {minimum:.2f} min"
            )

        # Calculate overall averages
        overall_average = sum(average_waits) / len(average_waits)
        overall_maximum = sum(maximum_waits) / len(maximum_waits)
        overall_minimum = sum(minimum_waits) / len(minimum_waits)

        results[counters] = (
            overall_average,
            overall_maximum,
            overall_minimum
        )

        print(
            f"Overall Average Waiting Time: "
            f"{overall_average:.2f} minutes"
        )

    # Final comparison
    print("\n")
    print("=" * 60)
    print("FINAL COMPARISON")
    print("=" * 60)

    print(
        f"{'Counters':<12}"
        f"{'Avg Wait':<15}"
        f"{'Avg Max Wait':<15}"
        f"{'Avg Min Wait':<15}"
    )

    print("-" * 60)

    for counters, values in results.items():

        average, maximum, minimum = values

        print(
            f"{counters:<12}"
            f"{average:<15.2f}"
            f"{maximum:<15.2f}"
            f"{minimum:<15.2f}"
        )


if __name__ == "__main__":
    main()
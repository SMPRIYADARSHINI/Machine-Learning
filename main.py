import random
import matplotlib.pyplot as plt

# Simulate a Coin-toss experiment until 3 heads are obtained
def simulate_experiment():
    heads = 0
    tosses = 0
    while heads < 3:
        toss = random.randint(0, 1)  # 0 for tails, 1 for heads
        tosses += 1
        heads += toss

    return tosses
def main():
    trials = 1000
    tosses_list = []
    average_list = []
    # Perform the 1000 trials
    for i in range(1, trials):
        tosses = simulate_experiment()
        average_tosses = sum(tosses_list) / i
        average_list.append(average_tosses)
        tosses_list.append(tosses)
# finding the Average number of Tosses and Trials
    print("Average number of trials:", trials)
    print("Average:")
    for i, average in enumerate(average_list, start=1):
        print(f"{average: .2f}", end=" ")
        if i % 30 == 0:
            print()
# Graph Plotting
    plt.plot(average_list)
    plt.title('Average number of tosses: ' + str(sum(tosses_list) / trials))
    plt.xlabel("Trial Number")
    plt.ylabel("Number of Tosses to get Heads")
    plt.show()
if __name__ == "__main__":
    main()

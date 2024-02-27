def elect_next_budget_item(votes, balances, cost):
    # Initialize variables to keep track of the lowest cost item and its supporters
    min_cost_item = None
    min_cost_supporters = set()
    min_cost_per_supporter = float('inf')

    # Loop through each item and its cost
    for item, item_cost in cost.items():
        # Initialize variables to keep track of supporters who can afford the item
        affordable_supporters = set()

        # Check each voter's vote
        for i, voter_votes in enumerate(votes):
            # Check if the voter supports the current item
            if item in voter_votes:
                # Check if the voter's balance is enough to afford the item
                if balances[i] >= item_cost:
                    affordable_supporters.add(i)

        # If there are supporters who can afford the item
        if affordable_supporters:
            # Calculate the cost per supporter
            cost_per_supporter = item_cost / len(affordable_supporters)
            # If the cost per supporter is lower than the current minimum
            if cost_per_supporter < min_cost_per_supporter:
                min_cost_item = item
                min_cost_supporters = affordable_supporters
                min_cost_per_supporter = cost_per_supporter

    # If there is a minimum cost item and its supporters
    if min_cost_item and min_cost_supporters:
        # Print the elected item
        print(f"Round 1: \"{min_cost_item}\" is elected.")

        # Calculate and print the amount each supporter pays and their new balance
        for supporter_index in min_cost_supporters:
            payment = min_cost_per_supporter
            balances[supporter_index] -= payment
            print(
                f"Citizen {supporter_index + 1} pays {payment} and has {balances[supporter_index]:.2f} remaining balance.")
    else:
        print("No item elected in this round.")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage:
    votes = [{'Park in street X', 'Park in street Y'}, {'Park in street X'}, {'Park in street Y'}]
    balances = [2, 1.5, 2]
    cost = {'Park in street X': 0.5, 'Park in street Y': 1}

    elect_next_budget_item(votes, balances, cost)

# Method-of-Equal-Shares
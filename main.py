def elect_next_budget_item_try(votes, balances, cost):
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




# def check_item(item, votes_list, item_price, balances):
#     num_of_votes = len(votes_list)
#     price_per_votes = item_price / num_of_votes
#     pay_per_vote = [0] * num_of_votes
#
#     for vote in votes_list:
#         if balances[vote] < price_per_votes:

def create_votes_for_item(votes, cost):
    votes_for_item = {}

    for i, citizen_vote in enumerate(votes):
        for item in citizen_vote:
            if item not in votes_for_item:
                votes_for_item[item] = [i]
            else:
                votes_for_item[item].append(i)

    return votes_for_item


def elect_next_budget_item(votes, balances, cost):
    sorted_votes_for_item = dict(sorted(create_votes_for_item(votes, cost).items(), key=lambda item: len(item[1]), reverse=True))

    for item in sorted_votes_for_item:
        item_price = cost[item]
        num_of_votes = len(sorted_votes_for_item[item])
        price_for_one = item_price / num_of_votes
        price_for_vote = {}

        for vote in sorted_votes_for_item[item]:
            if balances[vote] >= price_for_one:
                price_for_vote[vote] = price_for_one
            else:
                price_for_vote[vote] = balances[vote]
                item_price -= balances[vote]
                num_of_votes -= 1
                price_for_one = item_price / num_of_votes






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage:
    votes = [{'X', 'Y'}, {'X', 'Z'}, {'Z'}, {'Z'}]
    balances = [2, 1.5, 2]
    cost = {'X': 2.6, 'Y': 4, 'Z': 3}
    # votes_for_item = {'X': [0, 1], 'Y': [0], 'Z': [1, 2]}


    # print(sorted_votes_for_item)

    # elect_next_budget_item(votes, balances, cost)


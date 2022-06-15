
class ChanceNode:

    def __init__(self, probs, costs):
        """
        :param probs: (list) probability of outcomes
        :param costs: (list) costs of outcomes
        """
        self.probs = probs
        self.costs = costs

    def get_expected_cost(self):
        """
        :return: the expected cost of this chance node
        """

        num_outcomes = len(self.probs) # number of outcomes
        exp_cost = 0 # expected cost initialized to be 0

        # go over possible outcomes
        for i in range(num_outcomes):
            # increment expected cost by (probability of this outcome) * (cost of this outcome)
            exp_cost += self.probs[i] * self.costs[i]

        return exp_cost


# create an instance of ChanceNode
myChanceNode = ChanceNode(probs=[0.1, 0.2, 0.7], costs=[10, 20, 30])
# print the expected cost of this chance node
print(myChanceNode.get_expected_cost())


class ChanceNode:

    def __init__(self, probs, costs):
        self.probs = probs  # probabilities of outcomes
        self.costs = costs  # costs of outcomes

    def get_expected_cost(self):
        """
        :return: the expected cost of this chance node
        """
        num_outcomes = len(self.probs) # number of outcomes
        exp_cost = 0 # expected cost initialized at 0
        for i in range(num_outcomes):
            exp_cost += self.probs[i] * self.costs[i]

        return exp_cost


# create an instance of ChanceNode
myChanceNode = ChanceNode(probs=[0.1, 0.2, 0.7], costs=[10, 20, 30])
# print the expect cost of this chance node
print(myChanceNode.get_expected_cost())

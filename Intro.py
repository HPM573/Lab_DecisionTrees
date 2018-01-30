
class ChanceNode:
    def __init__(self, name, cost, future_nodes, probs):
        self.name = name
        self.cost = cost # cost of visiting this node
        self.future_nodes = future_nodes  # list of future nodes
        self.probs = probs  # probabilities of outcomes

    def get_expected_cost(self):
        """
        :return: the expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting this node
        i = 0  # index to iterate over probabilities
        for thisNode in self.future_nodes:
            if type(thisNode) == ChanceNode:
                exp_cost += self.probs[i] * thisNode.get_expected_cost()
            elif type(thisNode) == TerminalNode:
                exp_cost += self.probs[i] * thisNode.get_cost()
            i += 1
        return exp_cost


class TerminalNode:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost  # cost of this terminal node

    def get_cost(self):
        """
        :return: the cost of this terminal node
        """
        return self.cost


# create the terminal nodes
T1 = TerminalNode('T1', 10)
T2 = TerminalNode('T2', 20)
T3 = TerminalNode('T3', 30)
T4 = TerminalNode('T4', 40)

# create the future nodes of C2
C2FutureNodes = [T1, T2, T3]
# create C2
C2 = ChanceNode('C2', 15, C2FutureNodes, [0.1, 0.2, 0.7])
# create the future nodes of C1
C1FutureNodes = [C2, T4]
# create C1
C1 = ChanceNode('C1', 0, C1FutureNodes, [0.5, 0.5])

# print the expect cost of C1
print(C1.get_expected_cost())

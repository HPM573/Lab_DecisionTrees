
class Node:
    """ base (master) class for nodes """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        """

        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        :param probs: (list) probability of future nodes
        """

        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        E[cost] = (cost of visiting this node)
                  + sum_{i}(probability of future node i)*(E[cost of future node i])
        """

        # expected cost initialized with the cost of visiting the current node
        exp_cost = self.cost

        # go over all future nodes
        i = 0
        for node in self.futureNodes:
            # increment expected cost by
            # (probability of visiting this future node) * (expected cost of this future node)
            exp_cost += self.probs[i] * node.get_expected_cost()
            i += 1

        return exp_cost


class TerminalNode(Node):

    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        """

        Node.__init__(self, name, cost)

    def get_expected_cost(self):
        """
        :return: cost of this terminal node
        """
        return self.cost


# create the terminal nodes
T1 = TerminalNode('T1', cost=10)
T2 = TerminalNode('T2', cost=20)
T3 = TerminalNode('T3', cost=30)
T4 = TerminalNode('T4', cost=40)
# create C2
C2 = ChanceNode('C2', cost=15, future_nodes=[T1, T2, T3], probs=[0.1, 0.2, 0.7])
# create C1
C1 = ChanceNode('C1', cost=0, future_nodes=[C2, T4], probs=[0.5, 0.5])

# print the expect cost of C1
print(C1.get_expected_cost())

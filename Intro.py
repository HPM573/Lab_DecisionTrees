
class Node:
    """ base (master) class for nodes """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of this node
        """

        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """

        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


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
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost


class TerminalNode(Node):

    def __init__(self, name, cost):
        Node.__init__(self, name, cost)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
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


class Node:
    """ base (parent) class for nodes """
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

        num_outcomes = len(self.probs)  # number of outcomes
        exp_cost = self.cost  # initialize with the cost of this node

        # go over possible outcomes
        for i in range(num_outcomes) :
            exp_cost += self.probs[i] * self.futureNodes[i].get_expected_cost()

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
        :return: cost of this visiting this terminal node
        """
        return self.cost


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        (assumes that future nodes can only be chance or terminal nodes)
        """

        Node.__init__(self, name, cost)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes
        :return: a dictionary of expected costs of future nodes with node names as dictionary keys
        """

        # a dictionary to store the expected cost of future nodes
        exp_costs = dict()
        # go over all future nodes
        for node in self.futureNode:
            # add the expected cost of this future node to the dictionary
            exp_costs[node.name] = self.cost + node.get_expected_cost()

        return exp_costs


#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode(name='T1', cost=10)
T2 = TerminalNode(name='T2', cost=20)
T3 = TerminalNode(name='T3', cost=30)
T4 = TerminalNode(name='T4', cost=40)
T5 = TerminalNode(name='T5', cost=50)
T6 = TerminalNode(name='T6', cost=60)
# create C2
C2 = ChanceNode(name='C2', cost=15, future_nodes=[T1, T2, T3], probs=[0.7, 0.1, 0.2])
# create C1
C1 = ChanceNode(name='C1', cost=25, future_nodes=[C2, T4], probs=[0.4, 0.6])
# create C3
C3 = ChanceNode(name='C3', cost=50, future_nodes=[T5, T6], probs=[0.2, 0.8])
# create D1
D1 = DecisionNode(name='D1', cost=0, future_nodes=[C1, C3])

# print the expected cost of C1 and C3
print(D1.get_expected_costs())

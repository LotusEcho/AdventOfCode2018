import os
import random


class Node:
    """
    >>> lonely_node = Node(None)
    >>> lonely_node.metadata = [2, 3]
    >>> lonely_node.compute_meta_value()
    5
    >>> lonely_node.get_test_string()
    '0 2 2 3'
    >>> child_one = Node(lonely_node)
    >>> child_one.metadata = [41, 5, 1]
    >>> child_one.compute_meta_value()
    47
    >>> child_one.get_test_string()
    ' 0 3 41 5 1'
    >>> lonely_node.children = [child_one]
    >>> lonely_node.compute_meta_value()
    52
    >>> lonely_node.get_test_string()
    '1 2 0 3 41 5 1 2 3'
    >>> child_two = Node(lonely_node)
    >>> child_two.metadata = [3, 3]
    >>> child_two.compute_meta_value()
    6
    >>> child_two.get_test_string()
    ' 0 2 3 3'
    >>> lonely_node.children.append(child_two)
    >>> lonely_node.compute_meta_value()
    58
    >>> lonely_node.get_test_string()
    '2 2 0 3 41 5 1 0 2 3 3 2 3'
    >>> grandchild_one = Node(child_two)
    >>> grandchild_one.metadata = [1]
    >>> grandchild_one.compute_meta_value()
    1
    >>> grandchild_one.get_test_string()
    ' 0 1 1'
    >>> child_two.children = [grandchild_one]
    >>> child_two.compute_meta_value()
    7
    >>> child_two.get_test_string()
    ' 1 2 0 1 1 3 3'
    >>> lonely_node.compute_meta_value()
    59
    >>> lonely_node.get_test_string()
    '2 2 0 3 41 5 1 1 2 0 1 1 3 3 2 3'
    """
    def __init__(self, parent):
        self.children = []
        self.metadata = []
        self.parent = parent

    def random_tree(self, depth_num):

        if depth_num > 0:
            random_children = random.randint(0, 3)
            current_children = 0
            depth_num -= 1
            while current_children < random_children:
                child = Node(self)
                child.random_tree(depth_num)
                self.children.append(child)
                current_children += 1
        self.metadata = random.sample(range(1, 100), random.randint(1, 9))

    def compute_meta_value(self):
        value = 0

        for child in self.children:
            value += child.compute_meta_value()
        for data_value in self.metadata:
            value += data_value
        return value

    def compute_real_value(self):
        value = 0

        if len(self.children) > 0:
            for data_reference in self.metadata:
                if len(self.children) >= data_reference:
                    value += self.children[data_reference-1].compute_real_value()
        else:
            for data_value in self.metadata:
                value += data_value
        return value

    def get_test_string(self):
        if self.parent is not None:
            test_string = " "
        else:
            test_string = ""
        test_string += f"{len(self.children)} {len(self.metadata)}"
        for child in self.children:
            test_string += child.get_test_string()
        for data_value in self.metadata:
            test_string += f" {data_value}"
        return test_string

    def construct_from_values(self, values):
        """
        This constructs the tree of nodes from a set of values. Most of the work is done on the classes themselves.
        
        >>> parent_node = Node(None)
        >>> test_node = Node(parent_node)
        >>> test_node.construct_from_values([0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2])
        [1, 1, 0, 1, 99, 2]
        >>> test_node.metadata
        [10, 11, 12]
        >>> test_node_2 = Node(parent_node)
        >>> test_node_2.construct_from_values([1, 1, 0, 1, 99, 2])
        []
        >>> test_node_2.metadata
        [2]
        >>> test_node_2.children[0].compute_meta_value()
        99

        :param values: The list of integers that represent the unparsed nodes.
        :return: The remaining values to be parsed.
        """
        num_children = int(values[0])
        num_metadata = int(values[1])
        values = values[2:]

        if num_children > 0:
            current_children = 0
            while current_children < num_children:
                child_node = Node(self)
                values = child_node.construct_from_values(values)
                self.children.append(child_node)
                current_children += 1
            self.metadata = values[:num_metadata]
        else:
            self.metadata = values[:num_metadata]
        return values[num_metadata:]

    @staticmethod
    def node_factory(input_string):
        values = [int(val) for val in input_string.split(" ")]

        parent_node = Node(None)

        parent_node.construct_from_values(values)

        return parent_node


def process_file(filename):
    """
    >>> node = process_file("day8_example.txt")
    >>> node.compute_meta_value()
    138
    >>> node.compute_real_value()
    66

    :param filename: The file name to parse to find the node definitions
    :return: The license key value for the navigation system.
    """
    input_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    input_string = input_file.readline().rstrip()
    return process_input(input_string)


def process_input(input_string):
    """
    >>> for i in range (0, 5):
    ...     parent_node = Node(None)
    ...     parent_node.random_tree(4)
    ...     new_node = process_input(parent_node.get_test_string())
    ...     parent_node.compute_meta_value() - new_node.compute_meta_value()
    0
    0
    0
    0
    0
    >>>

    :param input_string: The string from the file that represents the license tree.
    :return: The tree of Nodes
    """
    node = Node.node_factory(input_string)
    return node


if __name__ == "__main__":
    node = process_file("day8_input.txt")
    print(f"Meta Value: {node.compute_meta_value()} Real Value {node.compute_real_value()}")

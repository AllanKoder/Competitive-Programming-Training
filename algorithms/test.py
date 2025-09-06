def label_graph_minimize_outdegree(G):
    """
    Label the vertices of the graph such that the largest out-degree is minimized.
    Args:
    - G: a dictionary representing the graph where the key is the node, 
         and the value is a list of neighbors (adjacency list representation).

    Returns:
    - labelling: a dictionary where the keys are nodes and the values are their labels.
    """
    # Step 1: Sort vertices by their degree (number of edges)
    sorted_nodes = sorted(G.keys(), key=lambda node: len(G[node]))

    # Step 2: Assign labels starting from 1 to n (number of vertices)
    labelling = {}
    label = 1
    for node in sorted_nodes:
        labelling[node] = label
        label += 1

    return labelling

import unittest

class TestGraphLabeling(unittest.TestCase):

    def test_basic_graph(self):
        G = {
            1: [2, 3],
            2: [1, 3, 4],
            3: [1, 2, 5],
            4: [2],
            5: [3]
        }
        expected_labelling = {1: 3, 2: 4, 3: 5, 4: 1, 5: 2}
        result = label_graph_minimize_outdegree(G)
        self.assertEqual(result, expected_labelling)

    def test_single_node(self):
        G = {1: []}
        expected_labelling = {1: 1}
        result = label_graph_minimize_outdegree(G)
        self.assertEqual(result, expected_labelling)

    def test_two_nodes(self):
        G = {1: [2], 2: [1]}
        expected_labelling = {1: 1, 2: 2}
        result = label_graph_minimize_outdegree(G)
        self.assertEqual(result, expected_labelling)

    def test_star_graph(self):
        G = {
            1: [2, 3, 4],
            2: [1],
            3: [1],
            4: [1]
        }
        expected_labelling = {2: 1, 3: 2, 4: 3, 1: 4}
        result = label_graph_minimize_outdegree(G)
        self.assertEqual(result, expected_labelling)

    def test_disconnected_graph(self):
        G = {
            1: [2],
            2: [1],
            3: [4],
            4: [3]
        }
        expected_labelling = {1: 1, 2: 2, 3: 3, 4: 4}
        result = label_graph_minimize_outdegree(G)
        self.assertEqual(result, expected_labelling)

if __name__ == "__main__":
    unittest.main()

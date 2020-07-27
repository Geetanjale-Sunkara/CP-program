class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.max_index = 0

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
            self.max_index = max(self.max_index, node_from_val)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
            self.max_index = max(self.max_index, node_to_val)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for i in self.edges:
            edge_list.append((i.value, i.node_from.value, i.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        adjacency_list = [None] * (self.max_index + 1)
        for i in self.edges:
            if adjacency_list[i.node_from.value] == None:
                adjacency_list[i.node_from.value] = [
                    (i.node_to.value, i.value)]
            else:
                adjacency_list[i.node_from.value].append(
                    (i.node_to.value, i.value))
        return adjacency_list

    def get_adjacency_matrix(self):
        adjacency_matrix = [
            [0 for i in range(self.max_index + 1)] for j in range(self.max_index + 1)]
        for i in self.edges:
            adjacency_matrix[i.node_from.value][i.node_to.value] = i.value
        return adjacency_matrix

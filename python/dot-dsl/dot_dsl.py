NODE, EDGE, ATTR = range(3)
parameters = {NODE: 2, EDGE: 3, ATTR: 2}


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=None):
        self.nodes, self.edges, self.attrs = [], [], {}
        if not data:
            return
        for element in data:
            if not 2 < len(element) < 5:
                raise TypeError
            category, *value = element
            if category not in parameters or not len(value) == parameters[category]:
                raise ValueError
            if category == NODE:
                self.nodes.append(Node(value[0], value[1]))
            if category == EDGE:
                self.edges.append(Edge(value[0], value[1], value[2]))
            if category == ATTR:
                self.attrs[value[0]] = value[1]

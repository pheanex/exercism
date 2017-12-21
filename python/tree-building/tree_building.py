class Record:
    def __init__(self, record_id, parent_id):
        self.node_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if set(record.node_id for record in records) != set(range(len(records))):
        raise ValueError('Index not continuous')
    nodes = {record.node_id: Node(record.node_id) for record in records}
    for record in sorted(records, key=lambda r: r.node_id):
        parent_id = record.parent_id
        child_id = record.node_id
        if child_id < parent_id:
            raise ValueError('Parent ID > Child ID')
        if 0 != child_id == parent_id:
            raise ValueError('Cycle')
        if child_id == 0 and parent_id != 0:
            raise ValueError('Parent of root is not itself')
        if child_id == parent_id == 0:
            continue
        parent = nodes[parent_id]
        child = nodes[child_id]
        parent.children.append(child)

    return nodes[0] if records else None

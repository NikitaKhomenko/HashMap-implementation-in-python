class EntryNode:
    def __init__(self, node_entry=None):
        self.entry = node_entry
        self.next = None


class EntryLinkedList:
    def __init__(self):
        self.head = None
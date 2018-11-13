
class ListEntryNode:
    def __init__(self, data):
        "constructor to initiate this object"
        self.data = data
        self.next = None


class SingleEntryLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        "add an item at the end of the list"

        if not isinstance(item, ListEntryNode):
            item = ListEntryNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def override_list_item(self, item):
        "add an item at the end of the list"

        if not isinstance(item, ListEntryNode):
            item = ListEntryNode(item)

        if self.head.data.key == item.data.key:
            old_value = self.head.data.val
            self.head = item
            return old_value
        else:
            self.tail.next = item

        self.tail = item

        return

    def list_length(self):
        "returns the number of list items"

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"

        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return

    def unordered_search_for_existence(self, entry):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        result = False

        while current_node is not None:
            if current_node.data == entry:
                result = True

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return result

    def unordered_search_value(self, value_searched):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        result = False

        while current_node is not None:
            if current_node.data.val == value_searched:
                result = True

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return result

    def unordered_search_key(self, key_searched):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        result = False

        while current_node is not None:
            if current_node.data.key == key_searched:
                result = True

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return result

    def unordered_search_get_entry_by_key(self, key):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        while current_node is not None:
            if current_node.data.key == key:
                return current_node.data

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return None

    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

        return
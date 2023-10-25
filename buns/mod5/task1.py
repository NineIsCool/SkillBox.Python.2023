# task1
class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None

        val = self.end
        self.end = val.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        curr_node = self.end
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.pref


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()
print()

item = stack.pop()
print(item)

stack.print()

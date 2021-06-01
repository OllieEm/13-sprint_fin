# ID 51774953


from math import floor


ACTION = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: floor(x / y),
}


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return 'Error: no items to delete'

    def size(self):
        return len(self.items)


def calculator(input_string):

    stack = Stack()

    for operand in input_string:
        if operand in ACTION.keys():
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            operator = ACTION[operand]
            result = operator(operand2, operand1)
            stack.push(result)
        else:
            stack.push(operand)

    if stack.size == 1:
        return stack[0]
    else:
        return stack.pop()


if __name__ == '__main__':
    input_data = input().split()
    res = calculator(input_data)
    print(res)

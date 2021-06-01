# ID 51776976


class Deque:
    def __init__(self, max_size: int):
        self.__queue = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value: int):
        if self.size != self.max_size:
            self.__queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value: int):
        if self.size != self.max_size:
            self.__queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self):
        if self.is_empty():
            raise IndexError

        item = self.__queue[self.head]
        self.__queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError

        item = self.__queue[self.tail - 1]
        self.__queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return item


def main():
    count = int(input())
    size = int(input())
    queue = Deque(size)

    commands = {
        'push_back': queue.push_back,
        'push_front': queue.push_front,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }

    for _ in range(count):
        command = input()
        operation, *value = command.split()

        if value:
            try:
                result = commands[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)

            except IndexError:
                print('error')


if __name__ == '__main__':
    main()

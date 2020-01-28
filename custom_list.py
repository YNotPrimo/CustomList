from еrror_messages import *


class CustomList:

    def __init__(self, *args):
        self.seq = [x for x in args]
        self.length = len(args)

    def __repr__(self):
        return ', '.join([str(x) for x in self.seq])

    def __getitem__(self, item):
        return self.seq[item]

    def append(self, value):
        new_list = self.seq + [value]
        self.seq = new_list
        self.length += 1
        return self.seq

    def remove(self, index):
        if len(self.seq) > index:
            value = self.seq[index]
            del self.seq[index]
            self.length -= 1
            return value
        raise IndexError(RemoveError)

    def get(self, index):
        if len(self.seq) > index:
            return self.seq[index]
        raise IndexError(GetError)

    def extend(self, *args):
        new_list = self.seq + [x for x in args]
        self.seq = new_list
        self.length += len(args)
        return self.seq

    def insert(self, index, value):
        if len(self.seq) > index:
            self.seq = self.seq[:index] + [value] + self.seq[index:]
            self.length += 1
            return self.seq
        raise IndexError(InsertError)

    def pop(self):
        if len(self.seq) > 0:
            value = self.seq[len(self.seq) - 1]
            del self.seq[len(self.seq) - 1]
            self.length -= 1
            return value
        raise IndexError(RemoveError)

    def clear(self):
        del self.seq[:]
        self.length = 0
        return self.seq

    def index(self, value):
        for i in range(len(self.seq)):
            if self.seq[i] == value:
                return i
        return 1  # TODO ERROR

    def count(self, value):
        count = 0
        for i in range(len(self.seq)):
            if self.seq[i] == value:
                count += 1
        return count

    def reverse(self):
        return self.seq[::-1]

    def copy(self):
        return [x for x in self.seq]

    def size(self):
        return self.length

    def add_first(self, value):
        self.seq = [value] + self.seq
        return self.seq

    def dictionize(self):
        dct = {}
        for i in range(0, len(self.seq) - 1):
            if i % 2 == 0:
                if self.seq[i] not in dct:
                    if i + 1 < len(self.seq):
                        dct[self.seq[i]] = self.seq[i + 1]
                    else:
                        dct[self.seq[i]] = ""

        return dct

    def move(self, amount):
        moved = []
        for i in range(0, amount):
            moved.append(self.seq[0])
            del self.seq[0]
        self.seq.extend(moved)
        return self.seq

    def sum(self):
        sum = 0
        for x in self.seq:
            if not type(x) is int and not type(x) is float:
                x = len(x)
            sum += x
        return sum

    def overbound(self):
        biggest_value = self.seq[0]
        for i in range(0, len(self.seq)):
            checked_value = self.seq[i]
            if not type(checked_value) is int and not type(checked_value) is float:
                checked_value = len(checked_value)
            if biggest_value <= checked_value:
                biggest_value = checked_value
        return biggest_value

    def underbound(self):
        smallest_value = self.seq[0]
        for i in range(0, len(self.seq)):
            checked_value = self.seq[i]
            if not type(checked_value) is int and not type(checked_value) is float:
                checked_value = len(checked_value)
            if smallest_value > checked_value:
                smallest_value = checked_value
        return smallest_value

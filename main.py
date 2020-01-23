class CustomList:
    def __init__(self, *args):
        self.seq = [x for x in args]

    def __str__(self):
        return '[' + ', '.join(map(str, self.seq)) + ']'

    def __repr__(self):
        return '[' + ', '.join(map(str, self.seq)) + ']'

    def append(self, value):
        new_list = self.seq + [value]
        self.seq = new_list
        return self.seq

    def remove(self, index):
        if len(self.seq) > index:
            value = self.seq[index]
            del self.seq[index]
            return value
        else:  # TODO ERROR
            pass

    def get(self, index):
        if len(self.seq) > index:
            return self.seq[index]
        else:  # TODO ERROR
            pass

    def extend(self, *args):
        new_list = self.seq + [x for x in args]
        self.seq = new_list
        return self.seq

    def insert(self, index, value):
        if len(self.seq) > index:
            self.seq = self.seq[:index] + [value] + self.seq[index:]
            return self.seq
        else:  # TODO Error
            pass

    def pop(self):
        value = self.seq[len(self.seq) - 1]
        del self.seq[len(self.seq) - 1]
        return value

    def clear(self):
        del self.seq[:]
        return self.seq

    def index(self, value):
        for i in range(len(self.seq)):
            if self.seq[i] == value:
                return i

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

    def add_first(self, value):
        self.seq = [value] + self.seq
        return self.seq

    def dictionize(self):
        dicten = {}
        for i in range(0, len(self.seq) - 1):
            if i % 2 == 0:
                if self.seq[i] not in dicten:
                    if i + 1 < len(self.seq):
                        dicten[self.seq[i]] = self.seq[i + 1]
                    else:
                        dicten[self.seq[i]] = ""

        return dicten

    def move(self, amount):
        pass

    def sum(self):
        pass

    def overbound(self):
        pass

    def underbound(self):
        pass

    def forEach(self):
        pass


def main():
    a = CustomList(1, 2, 3, 4)
    print(a)  # [1, 2, 3, 4]
    print(a.append(5))  # [1, 2, 3, 4, 5]

    print(a.remove(1))  # 2
    print(a)  # [1, 3, 4, 5]

    print(a.get(2))  # 4
    print(a.extend(6, 7, 8))  # [1, 3, 4, 5, 6, 7, 8]
    print(a.insert(2, 10))  # [1, 3, 10, 4, 5, 6, 7, 8]

    print(a.pop())  # 8
    print(a)  # [1, 3, 10, 4, 5, 6, 7]

    print(a.index(6))  # 5
    print(a.count(1))  # 1

    print(a.reverse())  # [7, 6, 5, 4, 10, 3, 1]
    print(a.copy())  # [1, 3, 10, 4, 5, 6, 7]

    print(a.add_first(6))  # [6, 1, 3, 10, 4, 5, 6, 7]

    print(a.dictionize())

    print(a.clear())  # []


main()

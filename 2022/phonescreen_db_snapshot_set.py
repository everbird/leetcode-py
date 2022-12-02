#!/usr/bin/env python3

class SnapshotSet:
    def __init__(self):
        self.__snapshots = []
        self.__current_iters = []

    def add(self, snapshot):
        self.__snapshots.append(snapshot)

    def remove(self, snapshot):
        self.__snapshots.remove(snapshot)

    def __contains__(self, snapshot):
        return snapshot in self.__snapshots

    def __iter__(self):
        iter_id = id(iter(self.__snapshots))
        self.__current_iters[iter_id] = 0
        return iter(self.__snapshots)

    def __next__(self):
        iter_id = id(self)
        if self.__current_iters[iter_id] >= len(self.__snapshots):
            raise StopIteration
        snapshot = self.__snapshots[self.__current_iters[iter_id]]
        self.__current_iters[iter_id] += 1
        return snapshot


if __name__ == '__main__':
    ss = SnapshotSet()
    ss.add(1)
    ss.add(2)
    ss.add(3)
    ss.add(4)
    ss.remove(3)
    it1 = ss.__iter__()
    ss.remove(2)
    ss.add(5)
    it2 = ss.__iter__()

    print(list(it1))
    print(list(it2))

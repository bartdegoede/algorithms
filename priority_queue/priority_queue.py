from itertools import count
from heapq import heappop, heappush

class PriorityQueue(object):
    def __init__(self):
        self.priority_queue = []
        self.entries = {}
        self.counter = count()
        self.REMOVED = '<removed-task>'

    def add_task(self, task, priority=0):
        """
        Add a new task, or update the priority of an existing task
        """
        if task in self.entries:
            self.remove_task(task)
        # count is the tiebreaker when multiple tasks of the same priority are added
        # we'll return tasks in the order they were inserted (FIFO)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entries[task] = entry
        heappush(self.priority_queue, entry)

    def remove_task(self, task):
        """
        Mark an existing entry as REMOVED. Raise `KeyError` if not found.
        """
        entry = self.entries.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """
        Remove and return task with highest priority. Raise `KeyError` if empty.
        """
        while self.priority_queue:
            priority, count, task = heappop(self.priority_queue)
            if task is not self.REMOVED:
                del(self.entries[task])
                return task
        raise KeyError('Pop from empty queue')

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add_task('prepare work')
    pq.add_task('do work', priority=1)
    pq.add_task('validate work', priority=3)

    assert(pq.entries == {
        'prepare work': [0, 0, 'prepare work'],
        'do work': [1, 1, 'do work'],
        'validate work': [3, 2, 'validate work']
    })
    assert(pq.priority_queue == [[0, 0, 'prepare work'], [1, 1, 'do work'], [3, 2, 'validate work']])

    # update existing task
    pq.add_task('validate work', priority=2)
    assert(pq.entries == {
        'prepare work': [0, 0, 'prepare work'],
        'do work': [1, 1, 'do work'],
        'validate work': [2, 3, 'validate work']
    })
    assert(pq.priority_queue == [[0, 0, 'prepare work'], [1, 1, 'do work'], [3, 2, '<removed-task>'], [2, 3, 'validate work']])
    assert(pq.pop_task() == 'prepare work')
    assert(pq.pop_task() == 'do work')
    assert(pq.pop_task() == 'validate work')

    # add tasks with same priority
    pq = PriorityQueue()
    pq.add_task('step 1')
    pq.add_task('step 2')
    assert(pq.priority_queue == [[0, 0, 'step 1'], [0, 1, 'step 2']])
    assert(pq.pop_task() == 'step 1')
    assert(pq.pop_task() == 'step 2')

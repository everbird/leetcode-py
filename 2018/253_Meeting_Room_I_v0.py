import heapq
from operator import itemgetter


def meeting_room_ii(meetings):
    meetings.sort(key=itemgetter(1))
    h = []
    for meeting in meetings:
        start, end = meeting
        if h and start > h[0]:
            heapq.heappop(h)
        heapq.heappush(h, end)
    return len(h)


meetings = [[0, 30],[5, 10],[15, 20]]
expect = 2
r = meeting_room_ii(meetings)
print r == expect, r, expect

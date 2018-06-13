import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        len_y = len(heightMap)
        len_x = len(heightMap[0])
        visited = [[False] * len_x for i in range(len_y)]
        heap = []
        volumn = 0

        for j in range(len_y):
            for i in range(len_x):
                if j == 0 or i == 0 or j == len_y-1 or i == len_x-1:
                    heapq.heappush(heap, (heightMap[j][i], j, i))
                    visited[j][i] = True

        while heap:
            height, y, x = heapq.heappop(heap)
            for j, i in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                if 0 <= j < len_y and 0 <= i < len_x and not visited[j][i]:
                    volumn += max(height - heightMap[j][i], 0)
                    visited[j][i] = True
                    heapq.heappush(heap, (max(heightMap[j][i], height), j, i))
        return volumn


if __name__ == '__main__':
    test_input = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    s = Solution()
    test_output = s.trapRainWater(test_input)
    print test_output

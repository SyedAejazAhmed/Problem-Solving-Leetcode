import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        val = nums[:]
        prev = [-1] * n
        next = [-1] * n
        alive = [True] * n

        for i in range(n):
            if i > 0:
                prev[i] = i - 1
            if i < n - 1:
                next[i] = i + 1

        violations = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                violations += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (val[i] + val[i + 1], i))

        ops = 0

        while violations > 0:
            s, a = heapq.heappop(heap)
            b = next[a]

            if b == -1:
                continue
            if not alive[a] or not alive[b]:
                continue
            if val[a] + val[b] != s:
                continue

            pa = prev[a]
            nb = next[b]

            if pa != -1 and val[a] < val[pa]:
                violations -= 1
            if nb != -1 and val[nb] < val[b]:
                violations -= 1
            if val[b] < val[a]:
                violations -= 1

    
            val[a] = val[a] + val[b]
            alive[b] = False

            next[a] = nb
            if nb != -1:
                prev[nb] = a

            if pa != -1 and val[a] < val[pa]:
                violations += 1
            if nb != -1 and val[nb] < val[a]:
                violations += 1

            if pa != -1:
                heapq.heappush(heap, (val[pa] + val[a], pa))
            if nb != -1:
                heapq.heappush(heap, (val[a] + val[nb], a))

            ops += 1

        return ops

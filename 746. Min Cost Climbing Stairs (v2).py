class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        ind = len(cost) - 3
        print(cost[ind])
        cost.append(0)

        while ind >= 0:
            cost[ind] = cost[ind] + min(cost[ind+1], cost[ind+2])
            ind = ind - 1

        return min(cost[0], cost[1])

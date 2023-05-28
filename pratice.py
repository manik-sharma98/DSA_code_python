import math
import collections
from typing import Optional
def sorted(s,i):
    if i == len(s):
        return
    print(s[i])
    return sorted(s,i+1)
s = [1,2,3,4,5,6,7,9,100]
#print(sorted(s,0))

def lcs1(str1,str2): 
    memo = [[-1 for i in range(len(str2)+1)] for i in range(len(str1)+1)]
    def lcs(str1,str2,i,j):
        if i == 0 or j == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if str1[i-1] == str2[j-1]:
            memo[i][j] = 1 + lcs(str1,str2,i-1,j-1)
            return memo[i][j]
        else:
            memo[i][j] = max(lcs(str1,str2,i-1,j),lcs(str1,str2,i,j-1))
            return memo[i][j]
    return lcs(str1,str2,len(str1),len(str2))
#print(lcs1('abc','abc'))

def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
    color = {}
    dislikes_table = collections.defaultdict(list)

    for p1,p2 in dislikes:
        dislikes_table[p1].append(p2)
        dislikes_table[p2].append(p1)
    
    def dfs(pos):
        for i in dislikes_table[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
        return True

    for node in range(n):
        if node not in color:
            color[node] = 0
            if not dfs(node):
                return False
    return True       

def strr(s1,l,r):
    if l >= r:
        return True
    return (s1[l]==s1[r] and strr(s1,l+1,r-1))

#print(strr('aaab',0,3))

def maxProfit(prices: list[int]) -> int:
    dp = [[-1]*2 for i in range(len(prices))]

    def helper(i,buy):
        if i >= len(prices):
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        if buy:
            dp[i][buy] = max(-prices[i]+helper(i+1,0),helper(i+1,1))
        else:
            dp[i][buy] = max(prices[i]+helper(i+2,1),helper(i+1,0))
        return dp[i][buy]
    return helper(0,1)
#print(maxProfit([1,2,3,0,2]))


def all_path_to_target(graph):
    target = len(graph) - 1
    results = []

    def backtrack(curr_node,path):
        if curr_node == target:
            results.append(list(path))
            return
        for next_node in graph[curr_node]:
            path.append(next_node)
            backtrack(next_node,path)
            path.pop()
    path = [0]
    backtrack(0,path)
    return results

#print(all_path_to_target([[4,3,1],[3,2,4],[3],[4],[]]))

strs = ["rrjk","furt","guzm"]
def minDeletionSize(strs: list[str]) -> int:
        def issort(str1):
            res = 0
            for n in range(1,len(str1)):
                if str1[n] < str1[n-1]:
                    return 1
            return 0
        res = 0
        str1 = ''
        if len(strs[0]) == 1:
            for j in range(len(strs)):
                str1 = str1 + strs[j]
            res += issort(str1)
            str1 = ''
        else:    
            for i in range(len(strs[0])):
                for j in range(len(strs)):
                    str1 = str1 + strs[j][i]
                res += issort(str1)
                str1 = ''
        return res
#print(minDeletionSize(strs))

tasks = [2,2,3,3,2,4,4,4,4,4]
def minimumRounds(tasks: list[int]) -> int:
    count = {}
    for task in tasks:
        if task in count:
            count[task] += 1
        else:
            count[task] = 1
    if 1 in count.values(): return -1 
    res = 0
    for c in count.values():
        res += c // 3 + min(1,c%3)
    return res
#print(minimumRounds(tasks))

points = [[1,2],[2,3],[3,4],[4,5]]

def findMinArrowShots(points: list[list[int]]):
    points.sort(key = lambda x:x[1])
    arrows = 1
    first_end = points[0][1]
    for x_start,x_end in points:
        if first_end < x_start:
            arrows += 1
            first_end = x_end
    return arrows
#print(findMinArrowShots(points))

def isItpossible(s):
    l = len(s)-1
    s1 = s[:len(s)//2]
    s2 = s[(l//2)+1:]
    s1 = s1+s1
    if s1.count(s2):
        return 1
    else:
        return 0
#print(isItpossible('abccab'))
costs = [7]
def maxIceCream(costs: list[int], coins: int) -> int:
        costs.sort()
        bars = 0
        summ = 0
        for ic in costs:
            if summ < coins and coins >= ic:
                summ += ic
                bars += 1
        return bars
#print(maxIceCream(costs,7))

def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(cost)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
        return res
        
#print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

def maxPoints(points: list[list[int]]) -> int:
    n = len(points)
    if n == 1:
        return 1
    result = 2
    for i in range(n):
        cnt = collections.defaultdict(int)
        for j in range(n):
            if j != i:
                cnt[math.atan2(points[j][1] - points[i][1],points[j][0] - points[i][0])] += 1
        result = max(result, max(cnt.values()) + 1)
    return result
#print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
        ans = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
            
        dfs(root)
        return ans
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(None)
root.right.left = TreeNode(3)

#print(preorderTraversal(root))

adjacentPairs = [[2,1],[3,4],[3,2]]
#1743
#def restoreArray(self, adjacentPairs: list[list[int]])

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
    queue = [(p,q)]
    while queue:
        node1,node2 = queue.pop()
        if not node1 and not node2:
            continue
        elif None in [node1,node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append(node1.left,node2.left)
            queue.append(node1.right,node2.right)
    return True

def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
    adj = {i:[] for i in range(n)}

    for child,parent in edges:
        adj[child].append(parent)
        adj[parent].append(child)
    
    print(adj)
    
    def dfs(cur,parent):
        time = 0

        for child in adj[cur]:
            if child == parent:
                continue
            childtime = dfs(child,cur)
            if childtime or hasApple[child]:
                time += 2 + childtime
        return time
    return dfs(0,-1)
#print(minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]))

def minflips(s):
    zeros = 0
    ones = 0
    output = 0
    for c in s:
        if c == '0':
            zeros += 1
    output = zeros
    for c in s:
        if c == '0':
            zeros -= 1
        elif c == '1':
            ones += 1
        output = min(output, zeros+ones)
    return output
s = "00011000"    
#print(minflips(s))    

def kadane_algo(nums):
    output = 0
    summ = 0
    for i in range(len(nums)):
        summ = max(summ+nums[i],nums[i])
        output = max(output,summ)
    return output    
#print(kadane_algo( [-2, 3, -1, 2]))

def maxSubarraySumCircular(nums):
    curMin = math.inf
    curMax = -math.inf
    array_sum = 0
    max_sum = -math.inf
    min_sum = math.inf

    for i in range(len(nums)):
        array_sum += nums[i]

        curMax = max(curMax+nums[i],nums[i])
        max_sum = max(max_sum,curMax)

        curMin = min(curMin+nums[i],curMin)
        min_sum = min(min_sum,curMin)

    if min_sum == array_sum:
        return max_sum
    
    return max(max_sum,array_sum-min_sum)


def subarraysDivByK(nums,k):
    n = len(nums)
    output = 0
    for i in range(n):
        sub_sum = 0
        for j in range(i,n):
            sub_sum += nums[j]
            #print(sub_sum)
            if sub_sum%k == 0:
                output += 1
    return output

def subarraysDivByK_os(nums,k):
    remainder = collections.defaultdict(int)
    remainder[0] = 1
    res = prefix_sum = 0
    for n in nums:
        prefix_sum += n
        remainder_num = prefix_sum % k

        res += remainder[remainder_num]
        remainder[remainder_num] += 1

#print(subarraysDivByK([1,2,3],3))

def findSubsequences(nums):
    res = set()
    subsequences = []
    
    def back_track(index):
        if len(nums) == index:
            if len(subsequences) >= 2:
                res.add(tuple(subsequences))
            return
        if not subsequences or subsequences[-1] <= nums[index]:
            subsequences.append(nums[index])
            back_track(index+1)
            subsequences.pop()
        back_track(index+1)
    
    back_track(0)
    return res
    
print(findSubsequences([4,6,7,7]))

def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) < n-1:
            return -1
        indegrees = [0] * (n+1)
        outdegrees = [0] * (n+1)

        for a,b in trust:
            outdegrees[a] += 1
            indegrees[b] += 1
        
        for i in range(1,n+1):
            if indegrees[i] == (n-1)  and outdegrees[i] == 0:
                return i
        return -1

def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        graph = collections.defaultdict(list)

        for v,u in prerequisites:
            graph[u].append(v)

        prepMap = {}
        def dfs(crcs):
            if crcs not in prepMap:
                prepMap[crcs] = set()
                for next_crc in graph[crcs]:
                    prepMap[crcs] |= dfs(next_crc)
                prepMap[crcs].add(crcs)
            return prepMap[crcs]

        for i in range(numCourses):
            dfs(i)
        res= []
        for u,v in queries:
            res.append(u in prepMap[v])
        return res

maxx = 0
n = 4
a = [1,15,13,8]
for i in range(n):
    for j in range(i):
        if(i!=j):
            s = abs(a[i] - a[j]) + abs(i-j)
            maxx = max(maxx,s)
print(maxx)
print('....')

arr = [1,2,3,4,5,6,7,8,9,10]
print(arr.index(7))
m = 3
next_ele = arr[0]
for i in range(1,n):
    if 
points = [[1,2,5],[3,1,1],[3,3,3]]
dp = [[-1]*4 for i in range(len(points))]
def nj(day,last,points):
    if day == 0:
        maxi = 0
        for i in range(3):
            maxi = max(points[0][i],maxi)
        dp[day][last] = maxi
        return dp[day][last] 
    maxi = 0
    if dp[day][last] != -1:
        return dp[day][last]
    for i in range(3):
        if i != last:
            point = points[day][i] + nj(day-1,i,points)
            maxi = max(maxi,point)
    dp[day][last] = maxi
    return dp[day][last]

print(nj(2,3,points))

points = [[10,40,70],
              [20,50,80],
              [30,60,90]]
def nj_t(points):
    dp = [[-1]*4 for i in range(len(points))]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1,len(points)):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last],activity)
    return dp[len(points)-1][3]
print(nj_t(points))
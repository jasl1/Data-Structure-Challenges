class Solution(object):
    def numPairsDivisibleBy60(self, time):
        times ={}
        times[time[0]] = 1
        answer = 0
        for i in range(1, len(time)):
            t = time[i]
            sub = 60 - t%60
            
            while sub <= 500:
                if sub in times:
                    answer += times[sub]
                sub += 60

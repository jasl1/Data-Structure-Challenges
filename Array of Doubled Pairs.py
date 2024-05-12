class Solution(object):
    def canReorderDoubled(self, arr):
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        # Iterate through the array
        for num in sorted(arr, key=abs):
            if frequency[num] == 0:
                continue
            if frequency.get(2 * num, 0) == 0:
                return False
            frequency[num] -= 1
            frequency[2 * num] -= 1
        
        return True

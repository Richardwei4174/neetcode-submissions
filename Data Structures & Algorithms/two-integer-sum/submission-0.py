class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        counterPart = {} # we store it's counter part and current index
        answer = []
        i = 0
        for num in nums:
            counterNum = target - num
            if (num in counterPart): # see if we exist(if we do meaning we have a counterNum)
                answer.append(counterPart[num])
                answer.append(i)
                break
            else:
                counterPart[counterNum] = i #if we don't exist, we will add out counterParter
            i += 1
        return answer
        
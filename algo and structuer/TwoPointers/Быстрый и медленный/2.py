class Solution(object):
    def res(self, chars):
        if chars == " ":
            return [" "]
        slow = 0
        fast = 0
        cnt = 0
        r = len(chars)-1
        while fast <= r:
            if chars[fast] != " ":
                chars[slow]=chars[fast]
                slow += 1
                fast += 1
            else: 
                chars[slow] = " "
                slow += 1
                while fast <= r and chars[fast] == " ":
                    fast += 1
        del chars[slow:]
        return chars
        
chars = [" ", " "," "," ", "h", "i"," ", " "," ", "!", " "]
print(Solution().res(chars))
# нужно заменить все пробелы в начале и в конце массива на один пробле, а все остальные элементы оставить без изменений.
# ouput : [" ", "h", "i", " ", "!", " "]
# 
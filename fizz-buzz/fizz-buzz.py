class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # https://leetcode.com/problems/fizz-buzz/solution/
        ans = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        
        for num in range(1, n+1):
            nums_ans_str = ""
            
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    nums_ans_str += fizz_buzz_dict[key]
            if not nums_ans_str:
                nums_ans_str = str(num)
            
            ans.append(nums_ans_str)
        
        return ans
        
#         answer = [0] * n
        
#         for i in range(n): 
#             if (i+1) % 3 == 0 and (i+1) % 5 == 0:
#                 answer[i] = "FizzBuzz"
#             elif (i+1) % 3 == 0:
#                 answer[i] = "Fizz"                
#             elif (i+1) % 5 == 0:
#                 answer[i] = "Buzz"
#             else:
#                 answer[i] = str(i+1)
            
#         return answer
        
class Solution:
    def maximum69Number (self, num: int) -> int:

        # Compute the length of num
        num_c = num
        num_list = []

        l = 0
        while num_c:
            l += 1
            num_list.append(num_c%10)
            num_c = num_c // 10

        num_list = num_list[-1::-1]

        max_num = num

        for i in range(len(num_list)):

            if num_list[i] == 6:
                num_list[i] = 9
            else:
                num_list[i] = 6
            cur_num = int("".join(str(i) for i in num_list))

            max_num = max(max_num, cur_num)
            if num_list[i] == 6:
                num_list[i] = 9
            else:
                num_list[i] = 6
        
        return max_num

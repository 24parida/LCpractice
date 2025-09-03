class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_map = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        
        counter = 0
        curr_num = num
        res = ""
        places = ["", "Thousand ", "Million ", "Billion "]

        while curr_num > 0:
            last_three = str(curr_num)[-3:]
            temp_res = ""

            if int(last_three) == 0:
                pass
            elif len(last_three) != 3:
                if int(last_three) in ones_map:
                    temp_res = ones_map[int(last_three)] + " "
                else:
                    temp_res = tens_map[int(last_three)//10] + " "
                    if int(str(last_three[-1])) > 0:
                        temp_res += ones_map[int(str(last_three[-1]))] + " "
            else:
                if not int(last_three[0]) == 0:
                    temp_res += ones_map[int(last_three[0])] + " Hundred "

                if int(last_three[1:]) in ones_map:
                    temp_res += ones_map[int(last_three[1:])] + " "
                else:
                    if not int(last_three[1]) == 0:
                        print(int(last_three[1]))
                        temp_res += tens_map[int(last_three[1])] + " "
                    if not int(last_three[2]) == 0:
                        temp_res += ones_map[int(last_three[2])] + " "
            
            if not int(last_three) == 0:
                temp_res += places[counter]
            res = temp_res + res
            curr_num = curr_num // 1000
            counter += 1
        
        
        return res[:-1] if res[-1] == " " else res
        
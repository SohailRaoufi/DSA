import math
import io

import sys
input_string = """7
2 3 1 2
2 3 3 4
2 3 4 5
2 3 2 3
2 3 3 5
2 3 1 10
2 3 10 11
"""


sys.stdin = io.StringIO(input_string)


num_rows = 5
l_group = [0,1]
r_group = [2,3,4]


for i in range(int(input())):
    c,r,s1,s2 = list(map(int,input().split()))



    s1_row_num = math.ceil(s1 / num_rows)
    s2_row_num = math.ceil(s2 / num_rows)

    if s1_row_num == s2_row_num:
        s1_row = (s1 - 1) % num_rows
        s2_row = (s2 - 1) % num_rows
  
        if s1_row in l_group and s2_row in l_group:
            print("Yes")
            continue

        if s1_row in r_group and s2_row in r_group:
            diff = abs(s1_row - s2_row)
            if diff == 1:
                print("Yes")
                continue
            else:
                print("No")
                continue
        
        else:
            print("No")

    else:
        print("No")



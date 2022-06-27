log="the number of excel file is  the deppendeed [12345] s  ite lok"
import re
reg=r"\[(\d+)\]"

s=re.search(reg,log)

print(s[1])
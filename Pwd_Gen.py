import pwd
import random

low_case ="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number="0123456789"
symbol="@#$%*?\/"
use_for=low_case+upper_case+Number+symbol

length_for_pass =8
password= "".join(random.sample(use_for,length_for_pass))
print("Your password is:",password)
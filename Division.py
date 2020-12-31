'''
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

'''
a=input()
b=input()

i_div=float(a)//float(b)
f_div=float(a)/float(b)

print(i_div)
print(f_div)
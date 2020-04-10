'''
An augmented assignment evaluates the target 
(which, unlike normal assignment statements, 
cannot be an unpacking) and the expression list, 
performs the binary operation specific to the type of assignment
 on the two operands, and assigns the result to the original target.
 The target is only evaluated once.
 '''

x = 23

x += 1 #24

x -= 4 #20

x *= 5 #100

x // 4 #25

x /= 5 #5.0

x **= 2 # 25.0

x %= 5 # 0.0

Greeting = "Good "
Greeting += "Morning "
print(Greeting)
print()
Greeting *= 5
print(Greeting)

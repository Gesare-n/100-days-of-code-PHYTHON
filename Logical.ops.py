#This is a logical operations File 
#I am performing basic logical operations for demonstation

#Logical or
var_1 = 24
var_2 =38

Var= var_1 or var_2
#print(var)

#Logical AND
var_3=var_1 and var_2
print  (var_3)

#Logical NOT
var_4= not var_2
print(var_4)

#New set of examples of logical operations 
x=True
y=False

var_o =x or y
print (var_o)

#AND Test Run 
var_a =x and y
var_b =x and x
#print(var_b)

#NOT Test Run 
var_t =not y
var_f =not x
print(var_t)
#print (var_f)
#print(var_t)

#Demonstration of using logical operations 
p=True
q= False 

#Disjunction Demonstration 
#Demonstration 01
var_q = p or (not q)#p and negative q
var_s =(not p) and q #negative p and q
ans =var_q and var_s#full representation of the question
#print(ans)#print my ans

#Demonstration 02
p=True 
q=False 
r=True

#create segments of the question
var_p =p or q #True
var_q =r or (not q)#True

var_a1 = (var_p and var_q)

var_r = p or r #True

#full operation 
answer_2 =var_a1 or(not var_r)
print (answer_2)


#Demonstration 03 .
#QUESTION 1: ((pvq)^r)v (p ^r)v(q^r))
#QUESTION 2:(-P^-q) v (q^-r)

#Q1

p=True
q=True
r=False

var_1=p and q #(p v q)-True

var_2=var_1 and r #(p v q )^r)

var_3=p and r #(p^r)

var_4=q and r #(q^ r)

ans_1=var_2 or var_3 and var_4

print("Answer is",ans_1 )

#Q2
var_a =not(p and Q) #(-p ^-q)
var_b =q and not r #(q^-r)

ans_2 =var_a or var_b

print("Answer is",ans_2)




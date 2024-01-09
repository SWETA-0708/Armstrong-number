Without using function
num=int(input("enter a number:"))
sum=0
n1=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum +=digit ** n1
    temp //=10


if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
Using function
# def is_armstrong(num,power):
#     temp=num
#     sum_of_powers=0
#     while temp>0:
#         digit=temp % 10
#         sum_of_powers +=digit**power
#         temp //= 10
#         return sum_of_powers == num
# n=int(input("enter the number of digits:"))
# start_range=10**(n-1)
# end_range=10**n
# for num in range(start_range,end_range):
#     if is_armstrong(num,n):

#       print(num, end=" ")

#summation for question one
s=[8,2,3,0,7]
print(sum(s))



#reversing a string for question two
d="1,2,3,4,,a,b,c,d"
d="1,2,3,4,,a,b,c,d"[::-1]
print(d)



#multiplication for question three
k=[8,2,3,-1,7]
k=[8*2*3*-1*7]
print(k)


#print even numbers in a list


def numbers(even_numbers):
    even = []
    for x in even_numbers:
        if x % 2 ==0:
            even.append(x)
    print(f"even numbers are {even}")
numbers([1,2,3,4,5,6,7,8,9])

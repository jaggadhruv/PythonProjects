import math

print('This is Data Structure File');

power = 2**3;
print(power);

string = 'Mary';
print(string[1:-1]);
print(string[::-1]);

string2 = string + " and Jane";
print(string2);

print(string.upper());

print("This is {c} {f} {m} string".format(c="cool",f="funny",m="master"))

name  = "Sam"
age = 16;

print(f"The boy named as {name} is {age} years of age")

with open("myfile.txt", mode='r') as myfile:
    contents = myfile.read()

print(contents)

sqRoot = math.sqrt(4)
print("Answer 1 is: ", sqRoot, "Square Root")

s = "hello"
print("Answer 2 is: ", s[1])

print("Answer 3 is: ", s[::-1])

mylist = [1,2,[3,4,"hello"]]
mylist[2][2] = "goodbye"
print("Answer 4 is: ",mylist)

myline = [5,3,4,6,1]
myline.sort()
print(myline)

dictionary1 = {"simple_key": "hello"}
print("Answer 5 is: ",dictionary1["simple_key"])
dictionary2 = {"k1":{"k2":"hello"}}
print("Answer 6 is: ",dictionary2["k1"]["k2"])
dictionary3 = {"k1":[1,2,{"k2":["this is tricky",{"tough":[1,2,["hello"]]}]}]}
print("Answer 7 is: ",dictionary3["k1"][2]["k2"][1]["tough"][2])
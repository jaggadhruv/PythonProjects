print('This is Statements File');

x = 0

while x < 5:
    print(f"x is less than 5 and x is {x}")
    x = x + 1
else:
    print(f"x is greater than 5, we break here")


indexCount = 0
word = "Hello Brother"

for i in word:
    print(word[indexCount], indexCount)
    indexCount += 1

# input1 = input("What is your Name?")
# print(f"Welcome to the coding world, {input1}")

celcius = [0,10,20,30.45]

for temp in celcius:
    print(f"Temperature in celsius is {temp}")
    fahrenheit = (9/5)*temp + 32
    print(f"Converted temperature in fahrenheit is {fahrenheit}")

number = range(0,11)
list_even = []
list_odd = []

for num in number:
    if num%2==0:
        num_even = num
        list_even.append(num_even)
    else:
        num_odd = num
        list_odd.append(num_odd)

print("The odd numbers from the list are as follows: ")
print(list_odd)
print("The even numbers from the list are as follows: ")
print(list_even)

number2 = range(0,51)
divisibleby3 = []

for num in number2:
    if num%3==0:
        divisible3 = num
        divisibleby3.append(divisible3)

print(divisibleby3)

number3 = range(0,101)
listFizz = []
listBuzz = []
listFizzBuzz = []

for num in number3:
    if num%3==0:
        dividedby3 = num
        listFizz.append(dividedby3)

    if num%5==0:
        dividedby5 = num
        listBuzz.append(dividedby5)

    if num%3==0 and num%5==0:
        dividedby3and5 = num
        listFizzBuzz.append(dividedby3and5)

print(listFizz)
print(listBuzz)
print(listFizzBuzz)


st = "Print only the words that start with s in this sentence"
listWordsS = []

for alpha in st:
    words = st.split(" ")

print(words)

for item in words:
    if item[0] == "s":
        wordsWithS = item
        listWordsS.append(wordsWithS)

print(listWordsS)

st2 = "Create a list of first letters of every word in this string"

for alph in st2:
    words = st2.split(" ")

for item in words:
    print(item[0])


st3 = "Print every word in this sentence that has an even number of letters"
listEvenWords = []

for alph in st3:
    wordsEven = st3.split(" ")

for item in wordsEven:
    if len(item)%2 == 0:
        printWord = item
        listEvenWords.append(printWord)
print(wordsEven)
print(listEvenWords)

def greet(name):
    return "Hello, " + name
for _ in range(3):
    print(greet("Alice"))

for x in range(1,6):
    if x == 4:
        break
    print(x)


#Classes and objects lesson
class Car():
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.number_of_seats = None

    def seat_capacity(self, number_of_seats):
        self.number_of_seats = number_of_seats

    def display_properties(self):
        print(self.color, "and", self.max_speed, "and", self.mileage, "and", self.number_of_seats)


car_type_1 = Car(200, 20)
car_type_1.seat_capacity(5)
car_type_1.display_properties()
car_type_2 = Car(180, 25)
car_type_2.seat_capacity(4)
car_type_2.display_properties()


class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap


text1=TextAnalyzer("John.is ,a great great guy!")
print(text1.freqAll())

ama ='Ama nice to see you'
ama.split()
print(ama.split())

with open("C:\\Users\\USER\\Desktop\\Info.txt", "r") as Krah:
    #content=Krah.readline()
    #print(content)
    i=0
    for line in Krah:
        print(i, line)
        i+=1
    # while True:
    #     i=0
    #     content=Krah.readline()
    #     if not content:
    #         break
    #     i = i + i
    #     print(content)

with open("C:\\Users\\USER\\Desktop\\Info1.txt", "w") as WriteUp: #can create a new file or overwrites an existing one, use a if you want to add
    WriteUp.write("Ama is great with God \n")
    #print(WriteUp)

a=["Ama", "Joe", "Don"]
for line in a:
    print(line)
print(a)

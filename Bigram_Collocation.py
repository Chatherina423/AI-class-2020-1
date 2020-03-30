from nltk.book import  *
myList = ['Hello', 'my', 'name', 'is', 'Chatherina']

def myBigram(list):
    result =[]
    for i in range(len(list) - 1):
        result.append((list[i], list[i+1]))

    return result



def myCollocation(myText):
    fd = FreqDist(myBigram(myText))

    list = fd.most_common(20)
    result =[]
    for i in list:
        result.append(i[0][0]+' '+i[0][1])

    return result


print("\n")
print("=====this is the result of myBigram=========")
print(myBigram(myList))
print("===============================================")

print("\n")
print("=====this is the result of myCollocation========")
print(myCollocation(text1))
print("===============================================")

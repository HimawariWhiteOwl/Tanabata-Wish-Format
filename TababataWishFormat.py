from pythainlp.tokenize.multi_cut import find_all_segment, mmcut, segment
text = input("Enter Your Wish : ")
myText = segment(text)
tone = [" ั","็","ิ"," ํ"," ุ"," ู","่","้","๊","๋","ี","ื","เ"]

print(f"┏{'━'*5}┷{'━'*6}┓")
for index in range(len(myText)):
    counttone = 0
    wordlisttone = list(myText[index])
    for index2 in range(len(wordlisttone)):
        if (wordlisttone[index2] in tone):
            counttone += 1
    mystr = f"┃{myText[index].center(10)}{' '*counttone}   ┃"
    print(mystr)
print(f"┗{'━'*6}☆{'━'*5}┛")

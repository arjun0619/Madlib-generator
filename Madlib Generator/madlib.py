with open("D:\Python project 2025\Madlib Generator\story1.txt","r") as f:
    story1 = f.read()

with open("D:\Python project 2025\Madlib Generator\story2.txt","r") as f:
    story2 = f.read()

with open("D:\Python project 2025\Madlib Generator\story3.txt","r") as f:
    story3 = f.read()

with open("D:\Python project 2025\Madlib Generator\story4.txt","r") as f:
    story4 = f.read()

with open("D:\Python project 2025\Madlib Generator\story5.txt","r") as f:
    story5 = f.read()


def mad(story):
    fword = "<"
    lword = ">"
    findex = -1
    words=set()

    for i,char in enumerate(story):
        if char == fword:
            findex = i
        if char==lword and findex!=-1:
            word = story[findex:i+1]
            words.add(word)


    answer={}
    for i in words:
        ans= input("Enter a word for "+ i[1:-1] +" ")
        answer[i]=ans
        
    for i in words:
        story = story.replace(i,answer[i])

    print("\n",story)

stories=[story2,story3,story4,story5]

print("\nWelcome to Madlib Game.Hope you have some fun!\n")
print("Here Is your 1st story\n")

mad(story1)

for i in stories:
    ch = input("\nWould you like to continue (y/n) : ")
    if ch.lower()=="y":
        print("Here is another one\n")
        mad(i)
    else:
        break
print("\nThanks for playing :)\n")


import datetime

print("파일 이름을 입력하세요. (입력하지 않으면 'YYYY-MM-DD-Undefined.md'로 지정됩니다.)")
fileName = input("파일명 : ")

if len(fileName) is 0:
    fileName = "Undefined"

fileName = fileName.replace(" ", "-")

now = datetime.datetime.now()
fullFileName = now.strftime("%Y-%m-%d-"+fileName+".md")

newFile = open("./_posts/"+fullFileName, "w+")

newFile.write("---\n")
newFile.write("title: \n")
newFile.write("date: "+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
newFile.write("categories: \n")
newFile.write("tags: \n")
newFile.write("---\n")
newFile.write("\nWrite Here!\n")

newFile.close()
print(fullFileName+" 파일이 생성되었습니다.")
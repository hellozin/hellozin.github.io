import datetime
import sys

if len(sys.argv) == 1:
    print("파일명이 필요합니다.")
    sys.exit(1)

fileName = sys.argv[1]
for i in range(len(sys.argv)):
    if i < 2:
        continue
    else:
        fileName += "-" + sys.argv[i]
print(fileName)

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
"""
One. file's Definition
(1) text documents
Only use specific encoding method to build a document, such as UTF-8
(2) Binary file
no specific encoding method to build a document
case1:We can see more details in case1

Two. file's open and close, read and write
(1)file's open
    1) a.open(file path/file name,open mode<7 kinds>)
        file path:
            absolute path:here'/' we can instead of it by '\\'
            relative path:.a/b/三国演义.txt, when the file in the same path of file.py,we can omit it
        open mode:
            r: read only,if file not found, Python feedback FileNotFoundError.
            w: write and cover. If file not found, python build this file and write,if file exist,
                Python write and cover it.
            x: build and write. If file not found, python build this file and write, if file exist,
             python feedback FileExistsError.
            a: add mode, If file not found, python build this file and write, if file exist, python add contents to this
                file.
            b: Open this file in binary file's mode.
            t: Open this file in text file's mode.
            +: Use it with x/a/b/t/r/w together, in terms of get complex function.
            case2: exercise about file open and open mode.
    2) a.read(size)
    3) a.readline(size)
    4) a.readlines(hint)
(2)file's close
    1) a.close()
    2) a.write(s)
    3) a.write(s)
    4) a.writelines(lines)
    5) a.seek(offset)

Three. Read method
(1) a.read(size)
    read several words in this file, sum equals to size
(2) a.readline(size)
    read a line words in this file, location equals to size
(3) a.readlines(hint)
    read several line's words in this file, sum equals to hint
    If hint equals to nothing, python read all words of this file.
case3: usage about read files

Four: Write method
(1) file.write(s)
    write in file with 's'
(2) file.writelines(lines)
    write a list data into file,details below:
        ls= ["a", "b", "c"]
        file.writelines(ls)
        python's feedback is 'abc'
(3) file.seek(offset)
    change the location of pointer(指针).It is adjustment function of write action.
    file.seek(0/1/2)
    0-return to beginning location of this file.
    1-return to current location of this file.
    2-return to end of this file.
case4: Write function
"""

# case1
tf = open("三国演义.txt", "rt", encoding="UTF-8")
# rt means text file,rb means use binary file
for i in range(3000):
    print(tf.readline())
tf.close()

# case2
tf1 = open("三国演义.txt")
tf1.close()
tf2 = open("三国演义.txt", "rt")
tf2.close()
# read only ,text file mode.
tf3 = open("三国演义.txt", "w")
tf3.close()
tf4 = open("三国演义.txt", "a+")
tf4.close()
# add mode + read mode ,python omit the r, if it does not have +,
# we only can add contents to this file but can not read it.
tf4 = open("三国演义.txt", "x")
tf4.close()
tf4 = open("三国演义.txt", "wb")
tf4.close()

# case3
file_name = input("Please input the file name with path and file suffix name: ")
f_open = open(file_name, "r")
txt1 = f_open.read()
# read all contents in this file, and txt1 is a text file.
f_open.close()
# read all
file_name = input("Please input the file name with path and file suffix name: ")
f_open = open(file_name, "r")
txt2 = f_open.read(2)
# we can write our execution here to split this text.
while txt2 != "":
    txt2 = f_open.read(2)
# only read part of this txt file every time.
# read all contents in this file, and txt1 is a text file.
f_open.close()
# read specific part every time
file_name = input("Please input the file name with path and file suffix name: ")
f_open = open(file_name, "r")
for line1 in f_open.readlines():
    print(line1)
f_open.close()
# traverse every single line of this file.(method 1)
file_name = input("Please input the file name with path and file suffix name: ")
f_open = open(file_name, "r")
for line2 in f_open:
    print(line2)
f_open.close()
# traverse every single line of this file. use "in f_open" directly (method 2)

# case4
f_open = open("output.txt", "w+")
list1 = ["China", "American", "French"]
f_open.writelines(list1)
# when python run to here, the pointer's location is in end of txt,we need adjust out pointer to the beginning of file.
f_open.seek(0)
# after adjustment of pointer, we can print all contents in this file.
for line3 in f_open:
    print(line3)
f_open.close()

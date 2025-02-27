import os
# r = read
# w = write
# a = append
# x = Create

# Read - error if it doesn't exist
f = open("names.txt")
#print(f.readline())
#print(f.readline(4))

#print(f.readline())
#print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names_list.txt")
    print(f.read())
except:
    print("The File you want to do  read doesn't exist")
finally:
    f.close()

# Apeend - creates the file if it  doesn't exist
f = open("names.txt", "a")
f.write("JOSH\n")
f.close()

f = open("context.txt", "w")
f.write("I delete all of the Contexts")
f.close()

f = open("names.txt")
print(f.read())
f.close()
#Write (overwrite)
f = open("context.txt", "w")
f.write("I delete all of the Contexts")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file
# Opens a file  for writing, creates a file  if it does not exist
f = open("name_list.txt", "w")
f.close()

#Create  the specified file, but return the error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete the files

#avoid an error if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does exist")

with open("more_names.txt") as f:
    content = f.read()

with open("name.txt", "w") as f:
    f.write(content)
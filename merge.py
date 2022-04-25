import os

#create a new txt file called HW#6.txt
hw = open("HW#6.txt", "w")

#add s1.txt to the new txt file
os.system("git log --all > logSnap.txt")

filenames = ['snap1.txt', 'snap2.txt', 'snap3.txt', 'snap4.txt', 'snap5.txt', 's1.txt', 'logSnap.txt']
  
# Open file3 in write mode
with open('HW#6.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")


# create a new directory called Logs
os.mkdir("Logs")

#move files from the current directory to the Logs directory in windows
os.system("move snap1.txt Logs")
os.system("move snap2.txt Logs")
os.system("move snap3.txt Logs")
os.system("move snap4.txt Logs")
os.system("move snap5.txt Logs")
os.system("move logSnap.txt Logs")
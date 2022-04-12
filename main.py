import os
from git import Git, Repo

import time
import random



#create random number between 5-12 seconds
def random_time():
    randInt = random.randint(5,12)
    time.sleep(randInt)
    

time.sleep(5)
#this project uses git flow

# 2. Make  a repo in this directory
repo = Repo.init(".")

#create a file called s1.txt
s1 = open("s1.txt", "a")


random_time()
# 3. Checkout the master branch (not really needed, but a good idea anyway)
repo.git.checkout("master")
# 4. Use touch to create a file called s1
# create a file called s1.txt in write mode

random_time()
# 5.  s1 and add the letter "A" 
with open("s1.txt", "a") as s1:
    s1.write("A")


random_time()
# 6. Commit this file and name the commit "C1"
repo.index.add("s1.txt")
repo.index.commit("C1")

random_time()
# 7. Tag it as "v1.0"
repo.create_tag("v1.0")


random_time()
# 8. Create a new git branch called "Feature 1"
os.system("git flow feature start 1")


random_time()
# 9. Create a new branch called "Feature 2"
os.system("git flow feature start 2")

random_time()
# 10. Create a new branch called "Feature 3"
os.system("git flow feature start 3")

random_time()
#run command in previous directory
# os.chdir("..")
os.system("git log --all --decorate --oneline --graph > snap1.txt")

random_time()
# 11. Checkout Feature 1
repo.git.checkout("feature/1")

random_time()
# 12. Merge Master into Feature 1
repo.git.merge("master")

# 13. Edit s1 and add the letter "B" to it.
with open("s1.txt", "a") as s1:
    s1.write("B")


random_time()
# 14. Commit this file and name the commit "C2"
repo.index.add("s1.txt")
repo.index.commit("C2")

random_time()
# 15. Edit s1 and add the letter "C" to it.
with open("s1.txt", "a") as s1:
    s1.write("C")

random_time()
# 16. Commit this file and name the commit "C3"
repo.index.add("s1.txt")
repo.index.commit("C3")

random_time()
# 17. Edit s1 and add the letter "D" to it.
with open("s1.txt", "a") as s1:
    s1.write("D")

random_time()
# 18. Commit this file and name the commit "C4"
repo.index.add("s1.txt")
repo.index.commit("C4")


random_time()
# 19. Use git log --all --decorate --oneline --graph > snap1.txt to take a snapshot of your git configuration
# os.chdir("..")
os.system("git log --all --decorate --oneline --graph > snap1.txt")

random_time()
# 20. Checkout branch Feature 2
repo.git.checkout("feature/2")

random_time()
# 21. Merge Master into Feature 2
repo.git.merge("master")

random_time()
# 22. Edit s1 and add the letter "F" to it.
with open("s1.txt", "a") as s1:
    s1.write("F")

random_time()
# 23. Commit this file and name the commit "C6"
repo.index.add("s1.txt")
repo.index.commit("C6")

random_time()

# 24. Edit s1 and add the letter "G" to it.
with open("s1.txt", "a") as s1:
    s1.write("G")

random_time()
# 25. Commit this file and name the commit "C7"
repo.index.add("s1.txt")
repo.index.commit("C7")

random_time()

# 26. Checkout branch Feature 3
repo.git.checkout("feature/3")
random_time()

# 27. Merge Master into Feature 3
repo.git.merge("master")

# 28. Edit s1 and add the letter "G" to it.
with open("s1.txt", "a") as s1:
    s1.write("H")

random_time()

# 29. Commit this file and name the commit "C8"
repo.index.add("s1.txt")
repo.index.commit("C8")
random_time()

# 30. Edit s1 and add the letter "I" to it.
with open("s1.txt", "a") as s1:
    s1.write("I")

# 31. Commit this file and name the commit "C9"
repo.index.add("s1.txt")
repo.index.commit( "C9")
random_time()

# 32. Edit s1 and add the letter "J" to it.
with open("s1.txt", "a") as s1:
    s1.write("J")

random_time()
# 33. Commit this file and name the commit "C10"
repo.index.add("s1.txt")
repo.index.commit("C10")


random_time()
# 34. Checkout the Develop branch
repo.git.checkout("develop")


random_time()
# 35. Merge Master into Devleop
repo.git.merge("master")


random_time()
# 36. Merge the Feature 1 branch into the Develop branch.
repo.git.merge("feature/1")

# 37. It turns out that there was an error in Feature 1, it will need to be fixed in the Feature 1 branch

random_time()
# 38. Checkout the Feature 1 branch
repo.git.checkout("feature/1")

# 39. Edit s1 and add the letter "E" to it.
with open("s1.txt", "a") as s1:
    s1.write("E")


random_time()
# 40. Commit this file and name the commit "C5"
repo.index.add("s1.txt")

# 41. Use git log --all --decorate --oneline --graph > snap2.txt to take a snapshot of your git configuration
random_time()
os.system("git log --all --decorate --oneline --graph > snap2.txt")

random_time()
# 42. Checkout the Develop branch
repo.git.checkout("develop")


random_time()
# 43. Merge the Feature 1 branch into the Develop branch.
repo.git.merge("feature/1")


random_time()
# 44. Merge the Feature 2 branch into the Develop branch
repo.git.merge("feature/2")

random_time()
# 45. Merge the Feature 3 branch into the Develop branch
repo.git.merge("feature/3")

# 46. Use git log --all --decorate --oneline --graph > snap3.txt to take a snapshot of your git configuration
random_time()
os.system("git log --all --decorate --oneline --graph > snap3.txt")

random_time()
# 47. Testing of the features has now been completed on the develop branch. Feature 1 and Feature three have been determined to be ready for production – feature 2 is not yet ready.
# 48. Checkout the Release branch
os.system("git flow release start 1")
repo.git.checkout("release/1")

random_time()
# 49. Merge Master into Release
repo.git.merge("master")

# os.system("git stash drop")
random_time()
# 50. Merge Feature 1 into Release
repo.git.merge("feature/1")

random_time()
# 51. Merge Feature 3 into Release
repo.git.merge("feature/3")

random_time()
# 52. Merge Release into Master
repo.git.merge("release/1")

random_time()
# 53. Tag it as "v2.0"
repo.git.tag("v2.0")

# 54. Use git log --all --decorate --oneline --graph > snap4.txt to take a snapshot of your git configuration
random_time()
os.system("git log --all --decorate --oneline --graph > snap4.txt")


random_time()
# 55. A problem with the master branch has been found.
# 56. Checkout the Hot Fix branch
os.system("git flow hotfix start 1")

random_time()
repo.git.checkout("hotfix/1")

random_time()
# 57. Merge master into Hot Fix
repo.git.merge("master")

# 58. Edit s1 and add the letter "K" to it.
with open("s1.txt", "a") as s1:
    s1.write("K")

random_time()
# 59. Commit this file and name the commit "C11"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C11")

random_time()

# 60. Checkout Develop
repo.git.checkout("develop")
random_time()

# 61. Merge Hot Fix into Develop
repo.git.merge("hotfix/1")
random_time()

# 62. Checkout Master
repo.git.checkout("master")
random_time()

# 63. Merge Hot Fix into Master
repo.git.merge("hotfix/1")
random_time()

# 64. Tag it as "v2.1"
repo.git.tag("v2.1")

random_time()
# 65. Use git log --all --decorate --oneline --graph > snap5.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap5.txt")
random_time()

os.system("git log --all > logSnap.txt")
random_time()

#create a new txt file called HW#6.txt
hw = open("HW#6.txt", "w")

#add s1.txt to the new txt file

filenames = ['snap1.txt', 'snap2.txt', 'snap3.txt', 'snap4.txt', 'snap5.txt', 'logSnap.txt']
  
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

#move files from the current directory to the Logs directory
os.system("mv snap*.txt Logs")
#move logSnap.txt to the Logs directory
os.system("mv logSnap.txt Logs")

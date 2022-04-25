from itertools import count
import os
from git import Git, Repo

import time
import random

#create random number between 5-12 seconds
def random_time():
    print("Still Running Script ") 
    randInt = random.randint(7,14)
    time.sleep(randInt)
    
#this project uses git flow

# 2. Make  a repo in this directory
repo = Repo.init(".")

#create a file called s1.txt
s1 = open("s1.txt", "a")



# 3. Checkout the master branch (not really needed, but a good idea anyway)
repo.git.checkout("master")
# 4. Use touch to create a file called s1
# create a file called s1.txt in write mode


# 5.  s1 and add the letter "A" 
with open("s1.txt", "w") as s1:
    s1.write("A\n")


random_time()
# 6. Commit this file and name the commit "C1"
repo.index.add("s1.txt")

random_time()
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

random_time()
# 13. Edit s1 and add the letter "B" to it.
with open("s1.txt", "a") as s1:
    s1.write("B\n")


random_time()
# 14. Commit this file and name the commit "C2"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C2")

random_time()
# 15. Edit s1 and add the letter "C" to it.
with open("s1.txt", "a") as s1:
    s1.write("C\n")

random_time()
# 16. Commit this file and name the commit "C3"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C3")

random_time()
# 17. Edit s1 and add the letter "D" to it.
with open("s1.txt", "a") as s1:
    s1.write("D\n")

random_time()
# 18. Commit this file and name the commit "C4"
repo.index.add("s1.txt")
random_time()
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


# 22. Edit s1 and add the letter "F" to it.
with open("s1.txt", "a") as s1:
    s1.write("F\n")

random_time()
# 23. Commit this file and name the commit "C6"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C6")


random_time()
# 24. Edit s1 and add the letter "G" to it.
with open("s1.txt", "a") as s1:
    s1.write("G\n")

random_time()
# 25. Commit this file and name the commit "C7"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C7")


random_time()
# 26. Checkout branch Feature 3
repo.git.checkout("feature/3")

random_time()
# 27. Merge Master into Feature 3
repo.git.merge("master")

# 28. Edit s1 and add the letter "G" to it.
with open("s1.txt", "a") as s1:
    s1.write("H\n")


random_time()
# 29. Commit this file and name the commit "C8"
repo.index.add("s1.txt")
random_time()
repo.index.commit("C8")


# 30. Edit s1 and add the letter "I" to it.
with open("s1.txt", "a") as s1:
    s1.write("I\n")
    
random_time()
# 31. Commit this file and name the commit "C9"
repo.index.add("s1.txt")

random_time()
repo.index.commit( "C9")

random_time()
# 32. Edit s1 and add the letter "J" to it.
with open("s1.txt", "a") as s1:
    s1.write("J\n")

random_time()
# 33. Commit this file and name the commit "C10"
repo.index.add("s1.txt")
random_time()
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
    s1.write("E\n")


random_time()
# 40. Commit this file and name the commit "C5"
repo.index.add("s1.txt")

random_time()
repo.index.commit("C5")

# 41. Use git log --all --decorate --oneline --graph > snap2.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap2.txt")

print("Do the rest of the steps from 42 onwards, then when you finish run merge.py to commpile the results")


# # 42. Checkout the Develop branch
# repo.git.checkout("develop")



# # 43. Merge the Feature 1 branch into the Develop branch.
# repo.git.merge("feature/1")


# # 44. Merge the Feature 2 branch into the Develop branch
# repo.git.merge("feature/2")


# # 45. Merge the Feature 3 branch into the Develop branch
# repo.git.merge("feature/3")

# # 46. Use git log --all --decorate --oneline --graph > snap3.txt to take a snapshot of your git configuration

# os.system("git log --all --decorate --oneline --graph > snap3.txt")

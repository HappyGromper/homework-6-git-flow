import os
from git import Git, Repo


#this project uses git flow

# 2. Make  a repo in this directory
repo = Repo.init(".")

# have git ignore "snap1.txt"
s1 = open("s1.txt", "w")

# 3. Checkout the master branch (not really needed, but a good idea anyway)
repo.git.checkout("master")
# 4. Use touch to create a file called s1
# create a file called s1.txt in write mode

# 5. Edit s1 and add the letter "A" to it]
s1.write("A")

# 6. Commit this file and name the commit "C1"
repo.index.add("s1.txt")
repo.index.commit("C1")

# 7. Tag it as "v1.0"
repo.create_tag("v1.0")

# 8. Create a new git branch called "Feature 1"
os.system("git flow feature start 1")

# 9. Create a new branch called "Feature 2"
os.system("git flow feature start 2")

# 10. Create a new branch called "Feature 3"
os.system("git flow feature start 3")

#run command in previous directory
# os.chdir("..")
os.system("git log --all --decorate --oneline --graph > snap1.txt")

# 11. Checkout Feature 1
repo.git.checkout("feature/1")

# 12. Merge Master into Feature 1
repo.git.merge("master")

# 13. Edit s1 and add the letter "B" to it.
s1.write("B")

# 14. Commit this file and name the commit "C2"
repo.index.add("s1.txt")
repo.index.commit("C2")

# 15. Edit s1 and add the letter "C" to it.
s1.write("C")

# 16. Commit this file and name the commit "C3"
repo.index.add("s1.txt")
repo.index.commit("C3")

# 17. Edit s1 and add the letter "D" to it.
s1.write("D")

# 18. Commit this file and name the commit "C4"
repo.index.add("s1.txt")
repo.index.commit("C4")

# 19. Use git log --all --decorate --oneline --graph > snap1.txt to take a snapshot of your git configuration
# os.chdir("..")
os.system("git log --all --decorate --oneline --graph > snap1.txt")


# 20. Checkout branch Feature 2
repo.git.checkout("feature/2")

# 21. Merge Master into Feature 2
repo.git.merge("master")

# 22. Edit s1 and add the letter "F" to it.
s1.write("F")

# 23. Commit this file and name the commit "C6"
repo.index.add("s1.txt")
repo.index.commit("C6")

# 24. Edit s1 and add the letter "G" to it.
s1.write("G")

# 25. Commit this file and name the commit "C7"
repo.index.add("s1.txt")
repo.index.commit("C7")

# 26. Checkout branch Feature 3
repo.git.checkout("feature/3")

# 27. Merge Master into Feature 3
repo.git.merge("master")

# 28. Edit s1 and add the letter "G" to it.
s1.write("H")

# 29. Commit this file and name the commit "C8"
repo.index.add("s1.txt")
repo.index.commit("C8")

# 30. Edit s1 and add the letter "I" to it.
s1.write("I")

# 31. Commit this file and name the commit "C9"
repo.index.add("s1.txt")
repo.index.commit( "C9")

# 32. Edit s1 and add the letter "J" to it.
s1.write("J")

# 33. Commit this file and name the commit "C10"
repo.index.add("s1.txt")
repo.index.commit("C10")

# 34. Checkout the Develop branch
repo.git.checkout("develop")

# 35. Merge Master into Devleop
repo.git.merge("master")

# 36. Merge the Feature 1 branch into the Develop branch.
repo.git.merge("feature/1")

# 37. It turns out that there was an error in Feature 1, it will need to be fixed in the Feature 1 branch

# 38. Checkout the Feature 1 branch
repo.git.checkout("feature/1")

# 39. Edit s1 and add the letter "E" to it.
s1.write("E")

# 40. Commit this file and name the commit "C5"
repo.index.add("s1.txt")

# 41. Use git log --all --decorate --oneline --graph > snap2.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap2.txt")

# 42. Checkout the Develop branch
repo.git.checkout("develop")

# 43. Merge the Feature 1 branch into the Develop branch.
repo.git.merge("feature/1")

# 44. Merge the Feature 2 branch into the Develop branch
repo.git.merge("feature/2")

# 45. Merge the Feature 3 branch into the Develop branch
repo.git.merge("feature/3")

# 46. Use git log --all --decorate --oneline --graph > snap3.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap3.txt")

# 47. Testing of the features has now been completed on the develop branch. Feature 1 and Feature three have been determined to be ready for production – feature 2 is not yet ready.
# 48. Checkout the Release branch
os.system("git flow release start 1")
repo.git.checkout("release/1")

# 49. Merge Master into Release
repo.git.merge("master")

# os.system("git stash drop")

# 50. Merge Feature 1 into Release
repo.git.merge("feature/1")

# 51. Merge Feature 3 into Release
repo.git.merge("feature/3")

# 52. Merge Release into Master
repo.git.merge("release/1")

# 53. Tag it as "v2.0"
repo.git.tag("v2.0")

# 54. Use git log --all --decorate --oneline --graph > snap4.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap4.txt")

# 55. A problem with the master branch has been found.
# 56. Checkout the Hot Fix branch
os.system("git flow hotfix start 1")
repo.git.checkout("hotfix/1")

# 57. Merge master into Hot Fix
repo.git.merge("master")

# 58. Edit s1 and add the letter "K" to it.
s1.write("K")

# 59. Commit this file and name the commit "C11"
repo.index.add("s1.txt")
repo.index.commit("C11")

# 60. Checkout Develop
repo.git.checkout("develop")

# 61. Merge Hot Fix into Develop
repo.git.merge("hotfix/1")

# 62. Checkout Master
repo.git.checkout("master")

# 63. Merge Hot Fix into Master
repo.git.merge("hotfix/1")

# 64. Tag it as "v2.1"
repo.git.tag("v2.1")

# 65. Use git log --all --decorate --oneline --graph > snap5.txt to take a snapshot of your git configuration

os.system("git log --all --decorate --oneline --graph > snap5.txt")

os.system("git log --all > logSnap.txt")

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
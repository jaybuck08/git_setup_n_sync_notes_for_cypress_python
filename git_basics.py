


# To link tests to your GIT account (automatically with vs code)::

# create new repository in git e.g "ecommerce_testing" and copy the link
# Go to VS code and type "git init" in the treminal of the test or file you want to link
# click source control (left side of screen) and click the tree radio buttons/dots at the top (more actions)
# select remote & add remote, select the remote locationfrom the dropdown that appears at the top, give it a name "e.g origin".  This automatically connects your repositiry to vs code
# commit (always add a comment) and publish branch. Go back to your repository in git and referesh to see.

# type "git branch Felix" '  (note that "Felix is the branch name & can be renamed anything") in the terminal to create new branch or
# click source control and click the tree radio buttons/dots above then click "branch" - "create branch"

# ------------------------------------------------------------------------------------------------
# setting global username and email for git in vs code:   - note that this needs to be set b4 any work is done. individuals must have access before data can be edited in git

# git config --global user.name    example username - "John Doe"
# git config --global user.email   example email - "johndoe@example.com"
# _________________________________________________________________________________________________


# _________________________________________________________________________________________________

# setting up files in vs code to link to Github (manually with the script in vs code terminal)

#1 git init  :initailses the git in your system from the folder you are currently in. (the folder created from this is not visible in vs code)

# git add . 
#       :this adds all the files/folder. It helps add a folder/file from a directory to prepare it to be pushed to github repository (other repository mgt software; gitbucket, azuredev)


#2 git add cooler.py  : this adds only the folder or file "cooler.py""  
#3 git commit -m "first commit"  : this adds the file to git
#4 git branch -M main   : here you create a branch called "main"  . note that vs code automatically give you a branch called "masters"

#5 git remote add repo https://github.com/jaybuck08/git_beginners.git  
#       : this links vs code to the repository in git. note that "repo" is a variable name & always add ".git" at the end of the repository url 

#6 git push -u repo main : this pushes "repo"  to the "main" branch in github

# to update another file in same folder (after using steps 1 - 6 above): use the below - 
# git add . 
# git commit -m "updated file"        - note that "updated file" is just a comment and can be anything
# git push -u repo main

#___________________________________________________________________________________________________________

# pull files from git to vs code

#from vs code do the below in your terminal:
#1 git init : if you have not initialized git)
#2 git remote add origin https://github.com/jaybuck08/git_beginners.git 
#3 git pull origin main ;interprete =  the varaiable origin (holding: https://github.com/jaybuck08/git_beginners.git ) is being pulled from the main branch


#___________________________________________________________________________________________________________

# ignoring files in git

#1 add file ".gitignore" in vs code
#2 add any file name e.g. "cooler.py" 
#3 once you commim/sync the file will not be updated in the next run
#4 if you had already added a file the first time, you will need to clear cache first using the below #5 before proceeding

#5 "git rm -r --cached ." : when trying to pusg again, this is used to clear the cache for files on vs code that have already been pushed to git
# .env   : these files are used to save secert keys e.g. passwords for your eyes only.

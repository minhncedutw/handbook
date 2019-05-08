
#### --------------------------------------------------
#### **Force** pull (overwrite existed files)
```commandline
git fetch --all
git reset --hard origin/master
```

#### --------------------------------------------------
#### **Undo** add hasn't been commit
```commandline
git reset
```

#### **Undo** commit hasn't been pushed
1. To revert the latest commit and discard changes in the committed file do:
```commandline
git reset --hard HEAD~1
```
2. To revert the latest commit but retain the local changes (on disk) do:
```commandline
git reset --soft HEAD~1
```

[Reference source](https://stackoverflow.com/questions/4114095/how-to-revert-a-git-repository-to-a-previous-commit)

#### --------------------------------------------------
#### Merge a file from 'master' branch to another branch
```commandline
git checkout <branch> # change to branch, where you want to merge to
git checkout origin/master path/to/file
```

#### Merge branch 'test' to 'master'
```commandline
git checkout master # change to branch 'master', where you want to merge to
git pull origin master # update 'master' to avoid error
git merge test # merge branch 'test' to current branch
```

#### Update a branch from master
```commandline
git checkout <branch>
git fetch
git rebase origin/master
```

#### --------------------------------------------------
#### delete remote branch
```commandline
git push origin --delete <remote branch name>
```

#### delete local branch
```commandline
git branch --delete <local branch name>
```

#### --------------------------------------------------
#### Safe pull(pull from remote but keep modified local, then push to remote)
```commandline
git add .
git commit -am "..."

git fetch --all
git pull

git push -u origin master
```

#### --------------------------------------------------
#### Adjust remote links
Modify the link of remote 'origin'
```commandline
git remote set-url origin https://minhncedutw@bitbucket.org/minhncedutw/test02.git
```
Rename remote named 'origin' to 'github'
```commandline
git remote rename origin github
```
Delete remote origin
```commandline
git remote rm origin
```
Add another remote named 'bit'
```commandline
git remote add bit https://minhncedutw@bitbucket.org/minhncedutw/test02.git
```
List remotes
```commandline
git remote -v
```

#### --------------------------------------------------
#### Push a local project to remote blank repository
```commandline
git init
git remote add origin https://minhncedutw@bitbucket.org/minhncedutw/test02.git
git add .
git commit -am "..."
git push -u origin master
```

#### --------------------------------------------------
#### Pull
```commandline
git pull origin master
```

#### --------------------------------------------------
#### Push
```commandline
git add .
git commit -am "..."
git push -u origin master
```

```commandline
# reset to previous commit
git checkout <commit_id>
git checkout -b <new branch> <commit_id>
git checkout HEAD~X // x is the number of commits t go back

git reflog
git checkout HEAD@{...}

git stash
git reset --hard 0d1d7fc32
git stash pop

[source](https://stackoverflow.com/questions/4114095/how-to-revert-a-git-repository-to-a-previous-commit)
```

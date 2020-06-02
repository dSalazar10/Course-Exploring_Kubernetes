Useful Git commands

1) Cloning a remote repo: git clone <url> <where-to-clone>:

`git clone https://github.com/my-user/remote_repo.git .`


2) Viewing information about a remote repo:
- Repository information: `git remote -v`
- List of branches in repo: `git branch -a`
- View logs of commited files: `git log`


3) Making changes:
- Show changes that have been made: `git diff`
- Checking the status of a repo: `git status`
- Add all the changes: `git add -A`
- Commit the changes locally: `git commit -m "Some Message"`
- Pull changes from remote repo (git pull <repo-name> <branch>): `git pull origin master`
- Push changes to remote repo (git push <repo-name> <branch>): `git push origin master`
Cloning a GitHub Repo for use with SSH in Cloud9 Programming Environment

1) Create an SSH key to allow for an encrypted connection to GitHub:

`ssh-keygen -t rsa`

2) Display your Cloud9 Environment's public RSA key:

`cat ~/.ssh/id_rsa.pub`

3) Navigate to your GitHub account's personal settings.

4) Click on the "SSH and GPG Keys" tab.

5) Click on the green button labeled "New SSH Key".

6) Give it a name and the public rsa key from step 2.

7) Clone your repo in the current working directory:

`git clone git@github.com:[user-name]/[repo-name].git`

8) Enter "yes" when prompted to connect to GitHub.

9) Start coding!
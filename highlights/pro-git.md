
---
#  Pro Git
## by Scott Chacon
---

 - loc 102 - Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

 - loc 165 - Git thinks of its data more like a set of snapshots of a miniature filesystem. Every time you commit, or save the state of your project in Git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.

 - loc 175 - Most operations in Git only need local files and resources to operate – generally no information is needed from another computer on your network.

 - loc 182 - This also means that there is very little you can’t do if you’re offline or off VPN.

 - loc 188 - Everything in Git is check-summed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it.

 - loc 196 - When you do actions in Git, nearly all of them only add data to the Git database.

 - loc 203 - Git has three main states that your files can reside in: committed, modified, and staged. Committed means that the data is safely stored in your local database. Modified means that you have changed the file but have not committed it to your database yet. Staged means that you have marked a modified file in its current version to go into your next commit snapshot.

 - loc 296 - The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:

 - loc 303 - you can configure the default text editor that will be used when Git needs you to type in a message.

 - loc 316 - If you want to check your settings, you can use the git config --list command to list all the settings

 - loc 328 - you can get the manpage help for the config command by running $ git help config

 - loc 331 - try the #git or #github channel on the Freenode IRC server (irc.freenode.net). These channels are regularly filled with hundreds of people who are all very knowledgeable about Git and are often willing to help.

 - loc 346 - git init This creates a new subdirectory named .git that contains all of your necessary repository files – a Git repository skeleton. At this point, nothing in your project is tracked yet.

 - loc 364 - git clone https://github.com/libgit2/libgit2 That creates a directory named “libgit2”, initializes a .git directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version.

 - loc 384 - The main tool you use to determine which files are in which state is the git status command.

 - loc 396 - Untracked basically means that Git sees a file you didn’t have in the previous snapshot (commit); Git won’t start including it in your commit snapshots until you explicitly tell it to do so.

 - loc 401 - To begin tracking the README file, you can run this: $ git add README

 - loc 419 - git add is a multipurpose command – you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved.

 - loc 434 - Git stages a file exactly as it is when you run the git add command.

 - loc 459 - The rules for the patterns you can put in the .gitignore file are as follows: Blank lines or lines starting with # are ignored. Standard glob patterns work. You can start patterns with a forward slash (/) to avoid recursivity. You can end patterns with a forward slash (/) to specify a directory. You can negate a pattern by starting it with an exclamation point (!).

 - loc 498 - git diff by itself doesn’t show all changes made since your last commit – only changes that are still unstaged

 - loc 511 - git diff --cached to see what you’ve staged so far (--staged and --cached are synonyms):


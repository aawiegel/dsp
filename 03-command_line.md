# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > ### pwd
> > Show the current working directory.
> > ### mkdir (-p)
> > Create a new directory. Use the -p option to create multiple subdirectories at the same time.
> > ### rmdir
> > Remove a directory. This only works if the directory is empty.
> > ### touch
> > Create a new, empty file.
> > ### rm (-rf)
> > Remove a file. Use the option -rf to remove a directory and its files recursively.
> > ### mv filepath1 filepath2
> > Moves or renames a file from filepath1 to filepath2
> > ### ls (-a)
> > List files in a directory. The -a option shows all files, including hidden files. See below for more options.
> > ### cp filepath1 filepath2
> > Copy files from filepath1 to filepath2.
> > ### man command
> > Displays the help information/manual for a program.
> > ### less textfile
> > Displays first few lines of a text file and allows scrolling through.
---
### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ### ls
> > List files in a directory.
> > ### ls -a
> > List all files in a directory, including hidden files
> > ### ls -l
> > List the detailed information in a directory, including permissions, date created, etc.
> > ### ls -lh
> > List the detailed information in a directory with human readable byte sizes for files.
> > ### ls -lah
> > List all the detailed information in a directory, including hidden files.
> > ### ls -t
> > List all the files in order of time created.
> > ### ls -Glp
> > List the detailed information in a directory without group information and with slashes at the end of directories.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ### ls -m
> > List all files as a comma-separated list.
> > ### ls -ld
> > Display detailed information about the current directory.
> > ### ls -R
> > List all files in the current directory and each subdirectory.
> > ### ls -1
> > List all files with only one entry per line
> > ### ls *.[format]
> > List all files in the directory of the given file extension.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows passing long argument lists to commands that have a limit on the number of arguments. For example, if you wanted to remove all files in the current directory that had the extension "txt", you would use the following command:
```console
find . -name "*.txt" -type f -print | xargs /bin/rm -f
```

 


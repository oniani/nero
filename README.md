# Deadline
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/oniani/deadline/blob/master/LICENSE/)
![python 3_+](https://img.shields.io/badge/python-3+-green.svg)
![Made_for Terminal](https://img.shields.io/badge/UNDER-DEVELOPMENT-red.svg)

Terminal is one of the most important applications for developers. In theory, one could do virtually anything using nothing other than a UNIX terminal. **Deadline** is a tiny app which runs in the terminal. Its main goal is to help organizing daily tasks within a terminal window.

## Installation and getting started

Installation is very simple and straightforward. There are two major ways to install **Deadline** on your machine.

1. Through **Python** package installer

Run the command  `pip install deadline` and you are good to go!

2. Through **GitHub**

Run the command `git clone https://github.com/oniani/deadline` and once the repository is cloned, drop it in whatever directory you want. Then do `cd` in that directory and run `python3 setup.py` and **Deadline** will start setting up its environment on your machine

Once **Deadline** is set up, type `deadline` in the **terminal** and the app will start running.

## Usage and functionality
**Deadline** has a very simple interface which is just a list of tasks with corresponding deadlines.

Here is the list of its functionalities:
* `help` - shows a manual for the commands
* `license` - shows the license for the app
* `ls` - display all the tasks
* `ls --title` - list the tasks only
* `ls --dl` - list the deadlines only
* `add` - add task
* `rm` - remove task by its index or the name (if there are  multiple tasks with the same name, you will also be asked for the index)
* `h` - show all the commands you used in the current session
* `clear` - clear the window
* `stop` - stop running the application and save my edits
* `encrypt` - enable optional encryption of the tasks

## How does it work?

**Deadline** is also very simple in terms of logic. Every task is stored in `.txt` file and the app either reads or writes to the file, depending on the command.
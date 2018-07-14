# Deadline
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/oniani/deadline/blob/master/LICENSE/)
![python 3_+](https://img.shields.io/badge/python-3+-green.svg)

Terminal is the core app for the software development. In theory, one could do virtually anything using nothing other than a UNIX terminal. **Deadline** is a tiny app which runs in the terminal and helps organize tasks.

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
* `ls` - list all tasks
* `ls --ttl` - list titles only
* `ls --ddl` - list deadlines only
* `add` - add a task
* `rm` - remove a task by its index
* `h` - show command history for the current session
* `clear` - clear the terminal window
* `stop` - stop running the app and save my edits

## How does it work?
**Deadline** is also very simple in terms of logic. Every task is stored in `.txt` file and the app either reads or writes to the file, depending on the command.

## License
[MIT](https://www.github.com/oniani/LICENSE)

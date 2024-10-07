#!/usr/bin/env python3
from typing import Dict

from keyslib.builder import bind_multi

APP = "htop"

DEFAULT_BINDS: Dict[str, str] = {
    "SHOW_HELP": "<f1> # Show htop help",
    "SHOW_SETTINGS": "<f2> # Show htop settings",
    "TOGGLE_TREE": "<f5> # Toggle tree view",
    "TOGGLE_HEADER": "<hash> # Toggle header",
    "CLOSE_APP": "<f10> # Close htop",
    "SHOW_ENV": "e # Show process environment",
    "TOGGLE_PATH": "p # Toggle program path",
    "TOGGLE_MERGED": "m # Toggle merged command",
    "SHOW_OPEN_FILES": "l # Show open files for process",
    "SHOW_LOCKS": "x # Show file locks for process",
    "START_TRACE": "s # Trace syscalls with strace for process",
    "SHOW_FULL_COMMAND": "w # Show full command for process",
    "TOGGLE_UPDATES": "z # Toggle process list updates",
    "FILTER_USER": "u # Filter processes by user",
    "TOGGLE_USER_THREADS": "H # Toggle user process threads",
    "TOGGLE_KERNEL_THREADS": "K # Toggle kernel threads",
    "TOGGLE_CONTAINERS": "O # Toggle processes in containers",
    "TOGGLE_FOLLOW": "F # Toggle cursor follows process",
    "TOGGLE_TREE_ALL": "<mul> # Toggle all tree folds",
    "TOGGLE_TREE_CURRENT": "<plus> # Toggle current process tree",
}
bind_multi(APP, DEFAULT_BINDS)

SEARCH_BINDS: Dict[str, str] = {
    "ENTER_SEARCH": "<f3> #search Search processes",
    "ENTER_SEARCH_INCREMENTAL": "<f3>+/ #search Search processes (incremental)",
    "NEXT_RESULT": "<f3> #search Next result",
    "PREVIOUS_RESULT": "(shift)<f3> #search Previous result",
}
bind_multi(APP, SEARCH_BINDS)

FILTER_BINDS: Dict[str, str] = {
    "ENTER_FILTER": "<f4> #filter Filter process list",
    "ENTER_FILTER_INCREMENTAL": "<f4>+/ #filter Filter process list (incremental)",
    "EXIT_FILTER": "<enter> #filter Exit filter mode",
    "CLEAR_FILTER": "<escape> #filter Clear filter",
}
bind_multi(APP, FILTER_BINDS)

SORT_BINDS: Dict[str, str] = {
    "ENTER_SORT": "<f6> #sort Sort process list",
    "SELECT_SORT": "<enter> #sort Select current sort",
    "CANCEL_SORT": "<escape> #sort Cancel sort",
    "SORT_PID": "N #sort Sort by process ID (PID)",
    "SORT_CPU": "P #sort Sort by CPU usage %",
    "SORT_MEM": "M #sort Sort by memory usage %",
    "SORT_TIME": "T #sort Sort by CPU time",
    "SORT_INVERT": "I #sort Invert sort order",
}
bind_multi(APP, SORT_BINDS)

SIGNAL_BINDS: Dict[str, str] = {
    "ENTER_SIGNAL": "<f9> #signal Send signal to process",
    "SEND_SIGNAL": "<enter> #signal Confirm signal selection",
    "CANCEL_SIGNAL": "<escape> #signal Cancel signal selection",
    "TERM_PROCESS": "<f9>+1+5+<enter> #signal Terminate selected process",
    "KILL_PROCESS": "<f9>+9+<enter> #signal Kill selected process",
}
bind_multi(APP, SIGNAL_BINDS)

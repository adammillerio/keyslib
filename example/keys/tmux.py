#!/usr/bin/env python3
from typing import Dict

from keyslib import KeySequence
from keyslib.builder import bind_multi, bind

APP = "tmux"

PREFIX = KeySequence("(ctrl)b")

bind(APP, "KEYS_COMPLETE", "(ctrl)<space> #keys Show completion palette")

SESSION_BINDS: Dict[str, KeySequence] = {
    # Session management
    "RENAME_SESSION": PREFIX + "$          #session Rename session",
    "DETACH_SESSION": PREFIX + "d          #session Detach from session",
    "SHOW_SESSION": PREFIX + "s            #session Show all sessions",
    "SHOW_PREVIEW": PREFIX + "w            #session Show session and window preview",
    "PREVIOUS_SESSION": PREFIX + "<lparen> #session Previous session",
    "NEXT_SESSION": PREFIX + "<rparen>     #session Next session",
}
bind_multi(APP, SESSION_BINDS)

WINDOW_BINDS: Dict[str, KeySequence] = {
    # https://tmuxcheatsheet.com
    # Window management
    "CREATE_WINDOW": PREFIX + "c   #window Create window",
    "RENAME_WINDOW": PREFIX + ",   #window Rename current window",
    "CLOSE_WINDOW": PREFIX + "&    #window Close current window",
    "LIST_WINDOW": PREFIX + "w     #window List windows",
    "PREVIOUS_WINDOW": PREFIX + "p #window Previous window",
    "NEXT_WINDOW": PREFIX + "n     #window Next window",
    "TOGGLE_WINDOW": PREFIX + "l   #window Toggle last active window",
    # TODO: Add some sort of ability to specify sequence literals ie
    # "COPY_CAPTURE_PANE": PREFIX + ":" + "capture-pane",
}
bind_multi(APP, WINDOW_BINDS)

PANE_BINDS: Dict[str, KeySequence] = {
    # Pane management
    "CLOSE_PANE": PREFIX + "x                    #pane Close current pane",
    "TOGGLE_PANE": PREFIX + ";                   #pane Toggle last active pane",
    "MOVE_PANE_LEFT": PREFIX + "{                #pane Move the current pane left",
    "MOVE_PANE_RIGHT": PREFIX + "}               #pane Move the current pane right",
    "TOGGLE_PANE_LAYOUT": PREFIX + "<space>      #pane Toggle between pane layouts",
    "NEXT_PANE": PREFIX + "o                     #pane Switch to next pane",
    "SHOW_PANE_NUMBERS": PREFIX + "q             #pane Show pane numbers",
    "TOGGLE_PANE_ZOOM": PREFIX + "z              #pane Toggle pane zoom",
    "CONVERT_PANE_WINDOW": PREFIX + "1           #pane Convert pane into a window",
    "SPLIT_WINDOW_VERTICAL": PREFIX + "%         #pane Create vertical split",
    "SPLIT_WINDOW_HORIZONTAL": PREFIX + "<quote> #pane Create horizontal split",
    # TODO: Implement handling of arrow keys
    # # Resize current pane height up
    # "RESIZE_PANE_UP": "(ctrl)<up>",
    # # Resize current pane height down
    # "RESIZE_PANE_DOWN": "(ctrl)<down>",
    # # Resize current pane left
    # "RESIZE_PANE_LEFT": "(ctrl)<left>",
    # # Resize current pane right
    # "RESIZE_PANE_RIGHT": "(ctrl)<right>",
}
bind_multi(APP, PANE_BINDS)

MISC_BINDS: Dict[str, KeySequence] = {
    "SHOW_COMMAND_PROMPT": PREFIX + ": #misc Enter command mode",
    "LIST_KEYS": PREFIX + "?           #misc List key bindings in tmux",
    "ENTER_COPY": PREFIX + "[          #misc Enter copy mode",
    "ENTER_CLOCK_MODE": PREFIX + "t    #misc Display a large clock",
    # Enter copy mode and scroll one page up
    # TODO: Handle <pageup> unicode escape sequence
    # "ENTER_COPY_UP": PREFIX + "<pageup>",
}
bind_multi(APP, MISC_BINDS)


# Select window <n>
WINDOW_SELECT_BINDS: Dict[str, KeySequence] = {
    f"SELECT_WINDOW_{n}": PREFIX + f"{n} #window_select Select window {n}"
    for n in range(0, 10)
}
bind_multi(APP, WINDOW_SELECT_BINDS)

# Select pane <n>
PANE_SELECT_BINDS: Dict[str, KeySequence] = {
    "SELECT_PANE_UP": PREFIX + "<up>       #pane_select Select pane above",
    "SELECT_PANE_DOWN": PREFIX + "<down>   #pane_select Select pane below",
    "SELECT_PANE_LEFT": PREFIX + "<left>   #pane_select Select pane to the left",
    "SELECT_PANE_RIGHT": PREFIX + "<right> #pane_select Select pane to the right",
}
PANE_SELECT_BINDS.update(
    {
        f"SELECT_PANE_{n}": PREFIX + f"q+{n} #pane_select Select pane {n}"
        for n in range(0, 10)
    }
)
bind_multi(APP, PANE_SELECT_BINDS)

# tmux plugin manager
# https://github.com/tmux-plugins/tpm
TPM_BINDS: Dict[str, KeySequence] = {
    "UPDATE_PLUGINS": PREFIX + "U         #tpm Update plugins",
    "UNINSTALL_PLUGINS": PREFIX
    + "(alt)u #tpm Uninstall plugins not in the plugin list",
    "RELOAD_PLUGINS": PREFIX
    + "I #tpm Install any new plugins and refresh tmux environment",
}
bind_multi("tmux", TPM_BINDS)

# tmux-resurrect plugin binds
# https://github.com/tmux-plugins/tmux-resurrect
RESURRECT_BINDS: Dict[str, KeySequence] = {
    "SAVE_SESSION": PREFIX + "(ctrl)s    #resurrect Save current session",
    "RESTORE_SESSION": PREFIX + "(ctrl)r #resurrect Restore saved session",
}
bind_multi("tmux", RESURRECT_BINDS)

# tmux-logging plugin binds
# https://github.com/tmux-plugins/tmux-logging
LOGGING_BINDS: Dict[str, KeySequence] = {
    "CLEAR_HISTORY": PREFIX + "(alt)c #logging Clear the history for the current pane",
    "TOGGLE_LOGGING": PREFIX
    + "P     #logging Toggle logging of the current pane to file",
    "PRINT_SCREEN": PREFIX
    + "(alt)p  #logging Save visible text of the current pane to file",
    "SAVE_HISTORY": PREFIX
    + "(alt)P  #logging Save entire history of the current pane to file",
}
bind_multi("tmux", LOGGING_BINDS)

# TODO: Figure out what I want to do with these, since they are "contextual"
# keybinds
# COPY_MODE_BINDS = {
#     # Quit copy mode
#     "COPY_EXIT": "q",
#     # Copy: Go to top line
#     "COPY_GO_TOP": "g",
#     # Copy: Go to bottom line
#     "COPY_GO_BOTTOM": "G",
#     # Copy: Scroll up
#     "COPY_SCROLL_UP": "<up>",
#     # Copy: Scroll down
#     "COPY_SCROLL_DOWN": "<down>",
#     # Copy: Move cursor up
#     "COPY_MOVE_UP": "k",
#     # Copy: Move cursor down
#     "COPY_MOVE_DOWN": "j",
#     # Copy: Move cursor left
#     "COPY_MOVE_LEFT": "h",
#     # Copy: Move cursor right
#     "COPY_MOVE_RIGHT": "l",
# }
#
# bind_multi("tmux", COPY_MODE_BINDS)

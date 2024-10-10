# keyslib

`keyslib` is a Python library for working with key sequences. It has a standard
grammar for expressing them, as well as `pathlib`-like overloads of standard binary
operators for composing key sequences in code:

```python
from keyslib import KeySequence

TMUX_PREFIX = KeySequence("(ctrl)b")
TMUX_CREATE_WINDOW = TMUX_PREFIX + "c"

# (ctrl)b+c
print(TMUX_CREATE_WINDOW)
```

In addition to key parsing, `keyslib` also has formatters for other applications and their key sequence formats, as well as a `keys` CLI:
```sh
# For a tmux send-keys command:
keys format tmux "(ctrl)b+c"
C-b c

# For a Visual Studio Code keybindings.json file:
keys format vscode "(ctrl)b+c"
ctrl+b c

# For a call to the Hammerspoon mac automation framework:
keys format hammerspoon "(ctrl)b+c"
hs.eventtap.keyStroke({"ctrl"}, "b"); hs.eventtap.keyStroke({}, "c");
```

The `keys` CLI can also directly control applications using the `send` command:
```sh
# tmux send-keys 'C-b' 'c'
keys send tmux "(ctrl)b+c"

# echo '\x02c' | wezterm cli send-text --no-paste
keys send wezterm "(ctrl)b+c"

# hs -q -c 'hs.eventtap.keyStroke({"ctrl"}, "b"); hs.eventtap.keyStroke({}, "c");'
keys send hammerspoon "(ctrl)b+c"
```

Collections of key bindings can be stored in the form of "keys files", which are
just [dotenv](https://saurabh-kumar.com/python-dotenv/#file-format) files:

[`example/binds/tmux.env`](example/binds/tmux.env):
```sh
CREATE_WINDOW='(ctrl)b+c                 #window Create window'
SPLIT_WINDOW_VERTICAL='(ctrl)b+%         #pane Create vertical split'
SPLIT_WINDOW_HORIZONTAL='(ctrl)b+<quote> #pane Create horizontal split'
```

These files can be written by hand or generated via Python and the `keys build`
command. See [`example/keys/tmux.py`](example/keys/tmux.py) for an example.

Putting it all together, the [`tools/kcmp.sh`](tools/kcmp.sh) script provides
an interactive key completion menu via the [fzf](https://github.com/junegunn/fzf)
CLI:

`tools/kcmp.sh tmux nvim`:
![keyslib-kcmp.png](https://raw.githubusercontent.com/adammillerio/i/refs/heads/main/keyslib-kcmp.png)

In this example, keys are loaded from `~/.config/keyslib/binds/nvim.env` and are
sent via a `tmux send-keys` command.

Additionally, a tmux plugin is available to bind `kcmp.sh` to a hotkey:
![keyslib-tmux-htop.png](https://raw.githubusercontent.com/adammillerio/i/refs/heads/main/keyslib-tmux-htop.png)


When the complete hotkey (`(ctrl)<space>` by default) is pressed, the plugin
will use `tmux list-panes -F '#{pane_current_command}'` to determine the current
running command. If there is a matching keys file at
`~/.config/keyslib/binds/<cmd>.env`, it will be displayed in a tmux window via
`kcmp.sh`. The selected key sequence is then sent to the active pane via tmux.
This provides a context-specific "command palette" like experience for terminal
applications.


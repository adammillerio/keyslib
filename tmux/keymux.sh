#!/bin/bash
# keymux.sh
# Simple helper script for routing to keys completion for the current tmux pane
# This is bound to @keys_completion_key in the keyslib tmux plugin

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get the current command of the pane this is running in (ie nvim)
CURRENT_CMD=$(tmux list-panes -F '#{pane_current_command}')

# Attempt to run key completion for current command
"${CURRENT_DIR}/kcmp.sh" tmux "${CURRENT_CMD}"

RETURN_CODE=$?
if [[ ${RETURN_CODE} == 2 ]]; then
    # No selection, silently ignore
    exit 0
else
    exit ${RETURN_CODE}
fi


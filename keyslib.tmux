#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$CURRENT_DIR/tmux/variables.sh"


main() {
    tmux bind-key -T prefix "$completion_key" run-shell "$CURRENT_DIR/tmux/keymux.sh"
    # TODO: This should be enabled via a separate option
    tmux bind-key -T root "C-$completion_key" run-shell "$CURRENT_DIR/tmux/keymux.sh"
}

main

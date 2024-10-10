#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

default_complete_key="Space"
complete_key=$(tmux show-option -gqv "@keys_complete_key")
complete_key=${logging_key:-$default_complete_key}

main() {
    tmux bind-key -T prefix "$complete_key" run-shell "$CURRENT_DIR/tools/keymux.sh"
    # TODO: This should be enabled via a separate option
    tmux bind-key -T root "C-$complete_key" run-shell "$CURRENT_DIR/tools/keymux.sh"
}

main

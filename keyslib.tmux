#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

default_complete_key="Space"
complete_key=$(tmux show-option -gqv "@keys_complete_key")
complete_key=${complete_key:-$default_complete_key}

main() {
    # Run general keys completion, which will invoke kcmp tmux <app> with <app> being
    # filled in with the command running in the current pane
    # This is bound without the prefix to (ctrl)<space> directly, as well as
    # (ctrl)b+<space> to handle either case, the prefix invocation also has the bkt
    # cache disabled for development
    tmux bind-key -T prefix "$complete_key" run-shell "$CURRENT_DIR/tools/keymux.sh"
    # TODO: This should be enabled via a separate option
    tmux bind-key -T root "C-$complete_key" run-shell "$CURRENT_DIR/tools/keymux.sh"
}

main

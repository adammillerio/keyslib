#!/usr/bin/env bash
# Key binding options and defaults

default_completion_key="Space"
completion_key=$(tmux show-option -gqv "@keys_completion_key")
completion_key=${logging_key:-$default_completion_key}

#!/usr/bin/env bash
# kcmp.sh
#
# open keys completion menu for app
#
# Given a sender and an app, this will load the app.env binds file in the keys
# dir and display a fzf completion menu. The selection will then be sent via the
# provided sender through the keys send command.

KEYS_SENDER=${1:?'ERROR: KEYS_SENDER not provided'}
KEYS_APP=${2:?'ERROR: KEYS_APP not provided'}

# Command for running keys - defaults to running keys cli via uvx (uv tool run)
# https://github.com/astral-sh/uv
KEYS=${KEYS_CMD:-'uvx --from keyslib keys'}

# Local state dir for storing fzf query history - defaults to ~/.local/state/keyslib
KEYS_XDG=${XDG_STATE_HOME:-"${HOME}/.local/state"}
KEYS_LOCAL_DIR=${KEYS_LOCAL_DIR:-"${KEYS_XDG}/keyslib"}

# Store query history in ~/.local/state/keyslib/history
KEYS_HISTORY_DIR=${KEYS_HISTORY_DIR:-"${KEYS_LOCAL_DIR}/history"}

# Cache commands using bkt if installed
KEYS_CACHE_DISABLE=${KEYS_CACHE_DISABLE:-}
if [[ ${KEYS_CACHE_DISABLE} ]] || ! command -v bkt >& /dev/null; then
    KEYS_CACHE="${KEYS}"
else
    KEYS_CACHE_TTL=${KEYS_CACHE_TTL:-'15m'}
    KEYS_CACHE_STALE=${KEYS_CACHE_STALE:-'5m'}
    KEYS_CACHE="bkt --discard-failures --ttl=${KEYS_CACHE_TTL} --stale=${KEYS_CACHE_STALE} -- ${KEYS}"
fi

# Create history directory if non-existent
if ! [ -d ${KEYS_HISTORY_DIR} ]; then
    mkdir -p "${KEYS_HISTORY_DIR}"
fi

# List all keys for app, using special formatting for fzf, see the cli help
# for more info
# NOTES:
# --history ...
# History can be navigated with (ctrl)h and (ctrl)l respectively
# --delimiter "\\t"
# --with-nth 3
# Using tab as a delimiter, display the 3rd field
# This corresponds to all text after the space separated doctag ( #) that was
# replaced with a tab delimiter by keys list --fzf
# --bind 'focus...
# Use tab delimiters in fzf formatted output to extract only the key sequence
# itself, and display that as the header. This is done outside of keys because
# it is a sync operation in the UI, so it has to be as fast as possible
KEYS_CMD=$(${KEYS_CACHE} list --fzf "${KEYS_APP}" | fzf \
    --history "${KEYS_HISTORY_DIR}/${KEYS_APP}" \
    --prompt '# ' \
    --ansi \
    --no-multi \
    --delimiter "\\t" \
    --with-nth 3 \
    --tmux 'bottom,80%,50%' \
    --no-info \
    --header '' \
    --bind 'ctrl-h:prev-history' \
    --bind 'ctrl-j:down' \
    --bind 'ctrl-k:up' \
    --bind 'ctrl-l:next-history' \
    --bind 'focus:transform-header:echo {} | cut -f 2' \
    --tiebreak 'begin,chunk')

RETURN_CODE=$?
if [[ ${RETURN_CODE} == 130 ]]; then
    # fzf exit code 130: Interrupted with CTRL-C or ESC
    # No user selection, silently ignore
    exit 0
fi

# Send selection, using special bind parsing for fzf, see the cli help for more
# info
${KEYS} send --fzf "${KEYS_SENDER}" "${KEYS_CMD}"


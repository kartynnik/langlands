#!/bin/sh
command-exists() {
  command -v "$1" > /dev/null 2>&1
}

copy-to-clipboard() {
  if command-exists wl-copy; then
    # Wayland
    wl-copy
  elif command-exists xclip; then
    # X11 / xclip
    xclip -selection clipboard
  elif command-exists xsel; then
    # X11 / xsel
    xsel --clipboard --input
  elif command-exists pbcopy; then
    # macOS
    pbcopy
  elif command-exists clip; then
    # Windows Subsystem for Linux (WSL)
    clip
  else
    echo "Please ensure that a clipboard copy tool (wl-copy, xclip, xsel, or pbcopy) is installed." >&2
    return 1
  fi
}

$(dirname "$0")/summarize.sh | copy-to-clipboard

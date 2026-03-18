#!/bin/sh
this=$(basename $(dirname "$(readlink -f "$0")"))/..
cd ..
find "$this" -name '.git' -prune -o -name '*.mhtml' -prune -o -name 'PASTED' -prune -type f -print |
  while IFS= read -r filename; do
    echo "========> FILENAME: $filename"
    cat "$filename"
  done

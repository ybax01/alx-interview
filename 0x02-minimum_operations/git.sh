#!/bin/bash

# Simple shell for pushing, with possible custom commit message if desired
commit_message=${1:-az}

git add .

git commit -m "$commit_message"

git push

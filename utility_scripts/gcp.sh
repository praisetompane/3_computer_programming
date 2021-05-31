#!/bin/sh
#quick utility to add, commit files and push files

message=$1

git add .
git commit -m"$message"
git push




#!/usr/bin/env bash

if pytest ; then
    black .
    git add .
    git commit -m "$(echo $@)"
fi
git reset --hard
git status

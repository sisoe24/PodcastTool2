#!/bin/bash
 
# build linux standalone package with pyinstaller
# https://pyinstaller.readthedocs.io/en/stable/usage.html

pyinstaller src/main.py \
    --distpath "$HOME" \
    --icon include/img/app.png \
    --noconfirm \
    -n PodcastTool \
    -p src:podcasttool \
    --add-data src:. \
    --add-data docs:docs \
    --add-data log:log \
    --add-data archive:archive \
    --add-data include:include \

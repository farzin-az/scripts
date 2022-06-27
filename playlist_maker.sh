!#/usr/bin/bash

for file in $(ls (*.mp4|*.mkv|*.wmv|*.avi|*.3gp|*.mov))
do
    echo file >> playlist.m3u
done

#!/bin/sh

mkdir data 

cd data

if [[ $OSTYPE == 'darwin'* ]]; then
	curl -L https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2023.csv -o play_by_play_2023.csv
else
	wget https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2023.csv
fi


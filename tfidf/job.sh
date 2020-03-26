#!/bin/bash

WCDIR=/home/tfidf
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

mapreduce_map_input_file="Dracula-1879.txt"
mapreduce_map_input_file="AliceInWonderland-1865.txt"
mapreduce_map_input_file="ATaleOfTwoCities-1859.txt"
mapreduce_map_input_file="CommonSense-1776.txt"
mapreduce_map_input_file="Frankenstein-1818.txt"
mapreduce_map_input_file="HuckleberryFinn-1885.txt"
mapreduce_map_input_file="JaneEyre-1847.txt"
mapreduce_map_input_file="MaryRowlandson-1770.txt"
mapreduce_map_input_file="Metamorphosis-1915.txt"
mapreduce_map_input_file="MobyDick-1851.txt"
mapreduce_map_input_file="PeterPan-1902.txt"
mapreduce_map_input_file="PrideAndPrejudice-1813.txt"
mapreduce_map_input_file="SherlockHolmes-1892.txt"
mapreduce_map_input_file="Siddhartha-1922.txt"
mapreduce_map_input_file="TheImportanceOfBeingEarnest.txt"
mapreduce_map_input_file="TheLegendOfSleepyHollow.txt"
mapreduce_map_input_file="TheTimeMachine-1895.txt"
mapreduce_map_input_file="TomSawyer-1876.txt"
mapreduce_map_input_file="TYW-1952.txt"
mapreduce_map_input_file="WarAndPeace-1869.txt"

printf "1st MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/Map1.py,$WCDIR/Reduce1.py \
    -mapper  $WCDIR/Map1.py                      \
    -reducer $WCDIR/Reduce1.py                   \
    -input   Gutenberg/'*'                          \
    -output  Out1
printf "\n2nd MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/Map2.py,$WCDIR/Reduce2.py \
    -mapper  $WCDIR/Map2.py                        \
    -reducer $WCDIR/Reduce2.py                     \
    -input   Gutenberg/'*'                                  \
    -output  Out2
printf "\n3rd MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/Map3.py,$WCDIR/Reduce3.py \
    -mapper  $WCDIR/Map3.py                        \
    -reducer $WCDIR/Reduce3.py                     \
    -input   Out1/'*',Out2/'*'                                  \
    -output  Out3 

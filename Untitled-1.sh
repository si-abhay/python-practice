#!/bin/bash
input file "data.txt" output file="result.txt" lines=$(cat "$input_file" | wc -w) echo "Total number of lines in $input_file: $lines"
if [[ $lines -lt 10 ]]; then head -5 "$input_file" > "$output_file
" else
tail n +$((lines / 2)) "$input_file" | head -5 > "$output_file"
fi
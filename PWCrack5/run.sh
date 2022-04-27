#!/bin/bash

#!/bin/bash
input="./dictionary.txt"
while IFS= read -r line
do
  echo $line | python level5.py | grep "pico"
done < "$input"
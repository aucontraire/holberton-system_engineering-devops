#!/bin/bash
sort | uniq -c -w 10 | sort -g -r | head -11 | cut -d$'\t' -f1 | tr -s " " | cut -d" " -f3

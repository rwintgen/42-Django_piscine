#!/bin/sh

curl -s --head "$1" | grep --ignore-case ^location | cut --delimiter=' ' --fields=2
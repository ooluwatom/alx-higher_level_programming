#!/bin/bash
# Bash script that makes a request and display response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2

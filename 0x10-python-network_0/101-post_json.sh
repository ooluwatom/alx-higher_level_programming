#!/bin/bash
# Bash script to send a JSON post request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

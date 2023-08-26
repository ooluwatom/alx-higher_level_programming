#!/bin/bash
# Bash script to display the response status code
curl -o /dev/null -sw "%{http_code}" "$1"

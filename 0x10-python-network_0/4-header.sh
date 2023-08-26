#!/bin/bash
# Bash script to display body of a response
curl -s "$1" -X GET -H "X-School-User-Id: 98"

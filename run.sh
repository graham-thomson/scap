#!/bin/bash

for i in $(seq 1 7); do python scap.py && echo "now sleeping for an hour..." && sleep 3600; done

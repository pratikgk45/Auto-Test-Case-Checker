#!/bin/bash
chmod +x gen.sh
chmod +x scripts/ver.sh
chmod +x scripts/run.sh
shopt -s expand_aliases
alias gen=./gen.sh
cd scripts
alias ver=./ver.sh
alias run=./run.sh
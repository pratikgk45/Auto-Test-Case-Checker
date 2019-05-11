#!/bin/bash
chmod +x sol.sh
chmod +x scripts/ver.sh
chmod +x scripts/run.sh
shopt -s expand_aliases
alias sol=./sol.sh
cd scripts
alias ver=./ver.sh
alias run=./run.sh
cd ..
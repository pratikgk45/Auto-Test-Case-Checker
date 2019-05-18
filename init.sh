#!/bin/bash
chmod +x sol.sh
chmod +x static/ver.sh
chmod +x static/run.sh
shopt -s expand_aliases
alias sol=./sol.sh
cd static
alias ver=./ver.sh
alias run=./run.sh
cd ..
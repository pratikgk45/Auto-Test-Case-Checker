#!/bin/bash
chmod +x sol.sh
chmod +x scripts/ver.sh
chmod +x scripts/run.sh
shopt -s expand_aliases
alias sol=./sol.sh
cd scripts
alias ver=./ver.sh
alias run=./run.sh
mkdir MathJax-2.7.3
git clone https://github.com/mathjax/MathJax.git ./scripts/MathJax-2.7.3/
cd ..

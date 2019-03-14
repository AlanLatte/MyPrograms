#!/usr/bin/env bash
varname=$*
g++ $varname -o main && chmod a+x main && ./main

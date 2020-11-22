#!/usr/bin/env bash
conda create -n calculator python=3.7
source activate calculator
conda install flask=1.12
conda install parameterized=0.7.4

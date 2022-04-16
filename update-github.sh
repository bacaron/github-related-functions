#!/bin/bash

directory=$1

cd ${directory}
git add .
git commit -m "Reason: update README"
git push --all

cd ../
rm -rf ${directory}

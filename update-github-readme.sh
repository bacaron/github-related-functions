#!/bin/bash

directory=$1
reponame=$2
username=$3
# all=$4
readme_file=$5
branches=($4)

cd ${directory}

echo "updating github readme for $reponame"

for i in ${branches[*]}
do
  echo "branch $i"
  git clone https://github.com/${username}/${reponame}.git -b $i
  cp ${readme_file} ${reponame}/ && cd ${reponame}
  git add README.md
  git commit -m "reason: update README"
  git push

  cd ${directory}
  rm -rf ${reponame}
done

# if [[ ${all} == true ]]; then
#
#   # override branch input
#   branches=`git ls-remote --heads https://github.com/${username}/${reponame|} | cut -f3 -d"/"`
#
#   # loop through branches, update readme, push, and remove dir.
#   for i in ${branches}
#   do
#     echo "branch $i"
#     git clone https://github.com/${username}/${reponame} -b $i
#     cp ${readme_file} ${reponame}/ && cd ${reponame}
#     git add README.md
#     git commit -m "reason: update README"
#     git push
#
#     cd ${directory}
#     rm -rf ${reponame}
#   done
# else
#   git clone https://github.com/${username}/${reponame} -b ${branches}
#   cp ${readme_file} ${reponame}/ && cd ${reponame}
#   git add README.md
#   git commit -m "reason: update README"
#   git push
#
#   cd ${directory}
#   rm -rf ${reponame}
# fi








#     git checkout -b ${i}
#     git add README.md
#
#
# git add .
# git commit -m "Reason: update README"
# git push --all
#
# cd ../
# rm -rf ${directory}

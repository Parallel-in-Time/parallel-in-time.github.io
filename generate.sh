#!/bin/sh

CONFIGS="_config.yml _octopress.yml"
FOLDERS="_data _events_past _events_upcomming _groups _includes _layouts _plugins _posts _sass _templates css fonts images js news"
FILES="about.html codes.html events.html feed.xml groups.html index.html projects.html"

git update-index --refresh --unmerged -q > /dev/null || :
if git diff-index --quiet HEAD; then
  echo "Generating gh-pages"
else
  echo "Repository is dirty. Not generating anything to avoid data loss."
fi

git checkout master
rm -rf ./*
git checkout source $CONFIGS $FOLDERS $FILES
git reset HEAD

octopress build \
  && rm -rf $CONFIGS $FOLDERS $FILES \
  && mv -fv _site/* . \
  && rm -rf _site \
  && git add -A \
  && git commit -m "Generated gh-pages for `git log source -1 --pretty=short --abbrev-commit`" -m "[skip ci]" \
  && git push origin master

git checkout source

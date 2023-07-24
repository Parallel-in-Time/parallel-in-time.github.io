## Local Development

### Start Development Environment
`docker run --rm -v "$PWD":/usr/src/app -w /usr/src/app ruby:3.2.2 bash -c "bundle config set --local path '/usr/src/app/vendor' && bundle install && bundle exec jekyll serve --livereload"`
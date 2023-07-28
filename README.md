## Local Development

### Start Development Environment

`docker run --rm -p 35729:35729 -p 4000:4000 -v "$PWD":/usr/src/app -w /usr/src/app ruby:3.2.2 bash -c "bundle config set --local path '/usr/src/app/vendor' && bundle install && bundle exec jekyll serve --livereload --host=0.0.0.0"`

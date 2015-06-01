require 'jekyll/scholar'

module Jekyll
  module TrimIEEECitation
    def trim_ieee_citation(input)
      input.gsub(/\[[0-9]+\]/, '')
    end
  end
end

require 'uri'

module MarkdownFilter
  class Markdown < BibTeX::Filter
    def apply(value)
      value.to_s.gsub(URI.regexp(['http','https','ftp'])) { |c| "<a href=\"#{$&}\">#{$&}</a>" }
    end
  end
end

Liquid::Template.register_filter(Jekyll::TrimIEEECitation)

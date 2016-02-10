require 'jekyll/scholar'

module Jekyll
  module TrimIEEECitation
    def trim_ieee_citation(input)
      input.gsub(/\[[0-9]+\]/, '')
    end
  end
end

require 'uri'

module Jekyll
  class Scholar
    class Markdown < BibTeX::Filter
      def apply(value)
        value.to_s.gsub(URI.regexp(['http','https','ftp'])) do |c|
          "<a href=\"#{$&}\" target=\"_blank\">#{$&}</a>"
        end
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::TrimIEEECitation)

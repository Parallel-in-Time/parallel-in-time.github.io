module Jekyll
  module UrlFilter
    def trim_url(input)
      input.strip!
      input.gsub(/^http[s]?:\/\//, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::UrlFilter)

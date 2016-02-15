module Jekyll
  module Tags
    class CurrenyYearTag < Liquid::Tag
      def initialize(tag_name, markup, tokens)
        super
        @markup = markup.strip
      end

      def render(context)
        "#{Date.today.year}"
      end
    end
  end
end

Liquid::Template.register_tag('current_year', Jekyll::Tags::CurrenyYearTag)

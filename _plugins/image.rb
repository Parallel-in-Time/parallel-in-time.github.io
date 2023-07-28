module Jekyll
  module Tags
    class ImageTagError < StandardError
      def initialize(msg)
        super
      end
    end

    class ImageTag < Liquid::Tag
      def initialize(tag_name, markup, tokens)
        @markup = markup.strip
        @markup = split_string_with_quotes(@markup)

        # the source of the image
        @img = @markup[0].gsub("'", "").gsub('"', '')
        if(not @img.include? "/")
          @img = "/assets/images/#@img"
        end

        # contains every attribute (i.e. alt or class)
        @attributes = ''

        # gets the alt attribute
        @alt = @markup.select {|sub| sub.include? "alt:"}[0]

        # gets the class attribute
        @class = @markup.select {|sub| sub.include? "class:"}[0]

        if @alt != nil
          @alt[":"] = "="
          @alt.gsub("'", '"')
          @attributes += "#@alt "
        end

        if @class != nil
          @class[":"] = "="
          @class.gsub("'", '"')
          @attributes += "#@class "
        end


      end
      def render(context)
        @img = Liquid::Template.parse(@img).render(context)
        "<img src=\"#@img\" #@attributes >"
      end
    end
  end
end

# splits strings at spaces but not if the spaces are inside quotes
def split_string_with_quotes(str)
  words = []
  current_word = ''
  in_quotes = false

  str.each_char do |char|
    if char == ' ' && !in_quotes
      words << current_word unless current_word.empty?
      current_word = ''
    else
      current_word += char
      if char == '"' || char == "'"
        in_quotes = !in_quotes
      end
    end
  end

  words << current_word unless current_word.empty?
  words
end

Liquid::Template.register_tag('image', Jekyll::Tags::ImageTag)
Liquid::Template.register_tag('img', Jekyll::Tags::ImageTag)

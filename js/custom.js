$(document).ready(function() {
    $('article.post-content .content > p:first').addClass('lead');
    
    $('div.reference > span.doi')
        .wrapInner('<a href="http://dx.doi.org/'+this.innerHTML+'"></a>');
    $('div.reference > span.arxivid')
        .wrapInner('<a href="//arxiv.org/abs/'+this.innerHTML+'"></a>');
    $('div.reference > span.mendeley').each(function() {
        var link = this.innerHTML;
        $(this).replaceWith('<a class="mendeley hidden-xs" role="button" href="'
            + link
            + '" title="Read on Mendeley" target="_blank">'
            + '<i class="fa fa-search"></i></a>');
    });
    $('div.reference > a.mendeley').each(function() {
        $(this).parent().prepend($(this).clone());
        $(this).remove();
    });
});

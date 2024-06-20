var toggle_meta_aside = function(desired_state) {
    var meta_aside = $('#meta-aside');

    if (desired_state === 'show' && meta_aside.hasClass('invisible')) {
        // make aside meta visible again
        $('#show-meta-aside').addClass('invisible');
        meta_aside.removeClass('invisible').addClass('in');
        $('article div#main-content').addClass('col-lg-7').removeClass('col-lg-12');

    } else if (desired_state === 'hide' && !meta_aside.hasClass('invisible')) {
        // make aside meta invisible
        $('#show-meta-aside').removeClass('invisible');
        meta_aside.addClass('invisible').removeClass('in');
        $('article div#main-content').removeClass('col-lg-7').addClass('col-lg-12');
    }
};

$(document).ready(function() {
    // activate tooltips
    $('[data-toggle="tooltip"]').tooltip();

    $('#hide-meta-aside').click(function() {
        toggle_meta_aside('hide')
    });

    $('#show-meta-aside').click(function() {
        toggle_meta_aside('show')
    });

    $('article.post-content[data-with-lead="true"]').find('.content > p:first').addClass('lead');

    var event_article = $('.post-event article');
    if (event_article.attr('data-page-type') === 'event_subpage') {
        // we are on an event's sub-page
        toggle_meta_aside('hide');
    }

    //
    // Beautify Ref Lists
    //
    $('ol.bibliography').each(function() {
        $(this).addClass('list-group');
        $(this).find('li').each(function() {
            $(this).addClass('list-group-item');
            $(this).find('.bibtex-entry-container').addClass('container-fluid')
                .find('>div').addClass('row')
                .find('.bibtex-ref-meta').removeClass('hidden');
            $(this).find('.bibtex-ref-entry').addClass('col-md-9 col-sm-12');
        });
    });
});

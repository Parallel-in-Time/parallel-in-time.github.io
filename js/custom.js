$(document).ready(function() {
    // from http://stackoverflow.com/a/20469901/588243
    $.extend({
        replaceTag: function (currentElem, newTagObj, keepProps) {
            var $currentElem = $(currentElem);
            var i, $newTag = $(newTagObj).clone();
            if (keepProps) {//{{{
                newTag = $newTag[0];
                newTag.className = currentElem.className;
                $.extend(newTag.classList, currentElem.classList);
                $.extend(newTag.attributes, currentElem.attributes);
            }//}}}
            $currentElem.wrapAll($newTag);
            $currentElem.contents().unwrap();
            // return node; (Error spotted by Frank van Luijn)
            return this; // Suggested by ColeLawrence
        }
    });
    $.fn.extend({
        replaceTag: function (newTagObj, keepProps) {
            // "return" suggested by ColeLawrence
            return this.each(function() {
                jQuery.replaceTag(this, newTagObj, keepProps);
            });
        }
    });

    $('article.post-content .content > p:first').addClass('lead');

    //
    // Beautify Ref Lists
    //
    $('ol.bibliography').replaceTag('<dl>', true);
    $('dl.bibliography').each(function() {
        $(this).addClass('dl-horizontal');
        $(this).find('li').each(function() {
            $(this).find('.bibtex-ref-id').removeClass('hidden').replaceTag('<dt>', true);
            $(this).find('.bibtex-ref-entry').replaceTag('<dd>', true);
            $(this).find('.bibtex-ref-entry span').addClass('col-xs-12 col-md-9 col-lg-10').replaceTag('<div>', true);
            $(this).find('.bibtex-ref-entry div.buttons').removeClass('hidden');
            $(this).find('.bibtex-ref-entry').wrapInner('<div class="row"></div>');
            $(this).replaceTag('<div>', true);
        });
    });
});

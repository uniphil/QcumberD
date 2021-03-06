/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

 
// Enable Dropdown boxes
$('.dropdown-header').click(function () {
    $(this).parent().next().slideToggle('medium');
    return false;
});


// Enrollment checking button
var subj_abbr = $('.subject-data').data('abbr');
var course_number = $('.course-data').data('number');

$('.check-enrollment').on('click', function (e) {
    //Get data
    var solus_id = $(this).parents('.section-data').data('solus-id');

    var url = "/enrollment/" + subj_abbr + "/" +  course_number + "/" + solus_id +"/";
    var container = $(this).parent();

    //Add a spinner
    $(this).remove();
    container.append('<img src="/static/img/ajax-loader.gif" alt="Loading" height="17" width="17">Gathering enrollment from SOLUS... (May take up to 15s)');

    //Fetch the enrollment data
    container.load(url);

    var label = subj_abbr + " " +  course_number + " (" + solus_id +")";
    _gaq.push(['_trackEvent', "enrollment", "request", label]);
});


// Track search events
$('.search-form').on('submit', function(e) {
    var form = $(this).parents().hasClass('hero-unit') ? 'index' :
        $(this).parents().hasClass('nav') ? 'search bar' : '???';
    var search_query = $(this).children('[type=search]').val();
    
    _gaq.push(['_trackEvent', 'search', form, search_query]);
    //return false; // for debugging, stops form from submitting.
});

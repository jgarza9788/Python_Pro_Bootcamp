/*!
* this file is for custom JS
*/

// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.sidenav');
//     var instances = M.Sidenav.init(elems, options);
// });

// custom toogle menu for moblie

$(document).ready(function(){

    $("#menu-button").click(function(){
        // $("#mobile-menu").toggle();

        console.log($("#mobile-menu").hasClass('is-visible'))

        if ($("#mobile-menu").hasClass('is-visible') == false) 
        {
            $("#mobile-menu").addClass('is-visible');
            $(document).scrollTop(0)
            // $("#mobile-menu").removeClass('not-visible');
        }
        else
        {
            $("#mobile-menu").removeClass('is-visible');
            // $("#mobile-menu").addClass('not-visible');
        }
        
    });


    $(".dropdown-trigger").dropdown();

});



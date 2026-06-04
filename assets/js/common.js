$(document).ready(function(){
    $('.toggle_nav').click(function () {
        if ($('#sidebar #nav_accordion').is(":visible") === true) {
            $('#main-content').css({
                'margin-left': '0px'
            });
            $('#sidebar').css({
                'margin-left': '-250px'
            });
            $('#sidebar #nav_accordion').hide();
            $("#maincontainer").addClass("sidebar-closed");
        } else {
            $('#main-content').css({
                'margin-left': '250px'
            });
            $('#sidebar #nav_accordion').show();
            $('#sidebar').css({
                'margin-left': '0px'
            });
            $("#maincontainer").removeClass("sidebar-closed");
        }
    });

  
    

    $('.has-submenu').on('click', function(){
      $(this).toggleClass('current'); 
      if($(this).parent('.has-submenu').hasClass('current'))
        {
            
        }
        else{
          $(this).addClass('current');
        }
    });


    $('.btn-toggle').click(function() {
      $(this).find('.btn').toggleClass('active');  
      
      if ($(this).find('.btn-primary').length>0) {
        $(this).find('.btn').toggleClass('btn-primary');
      }
      $(this).find('.btn').toggleClass('btn-default');
    }); 
    
    



    $('.responsive').slick({
        dots: true,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
        ]
      });


     

      
});

$(document).ready(function() {
    $('.profile > span:first-child').text('Robert Green');
    $('.profile > span:last-child').text('Asset Manager');
    // $('.userEmail').text('');
});
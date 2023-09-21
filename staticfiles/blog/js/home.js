$(window).scroll(function() {
  if ($(document).scrollTop() > 10) { //use `this`, not `document`
      $('.section').css({
          'display': 'none'
      });
  }
});
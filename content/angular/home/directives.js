define(function  (require) {
    var angular = require('angular');

    return angular.module('home.directives',[])
      .directive('multipleEmails', function () {
      return {
        require: 'ngModel',
        link: function(scope, element, attrs, ctrl) {
          ctrl.$parsers.unshift(function(viewValue) {
            var emails = viewValue.split(',');
            // define single email validator here
            var re = /\S+@\S+\.\S+/; 
              
            // angular.foreach(emails, function() {
              var validityArr = emails.map(function(str){
                  return re.test(str.trim());
              }); // sample return is [true, true, true, false, false, false]
              // console.log(emails, validityArr); 
              var atLeastOneInvalid = false;
              angular.forEach(validityArr, function(value) {
                if(value === false)
                  atLeastOneInvalid = true; 
              }); 
              if(!atLeastOneInvalid) { 
                // ^ all I need is to call the angular email checker here, I think.
                ctrl.$setValidity('multipleEmails', true);
                return viewValue;
              } else {
                ctrl.$setValidity('multipleEmails', false);
                return undefined;
              }
            // })
          });
        }
      };
    })
    .directive('loading', function () {
          return {
            restrict: 'E',
            replace:true,
            template: '<div class="wg_loading loading-button"><img src="http://www.nasa.gov/multimedia/videogallery/ajax-loader.gif" width="20" height="20" /></div>',
            link: function (scope, element, attr) {
                  scope.$watch('loading', function (val) {
                      if (val)
                          $(element).show();
                      else
                          $(element).hide();
                  });
            }
          }
      })
  .directive('scrollOnClickGoToContactForm', [ '$animate', function($animate) {
      return {
        restrict: 'A',
        link: function(scope, $elm) {
          $elm.on('click', function() {
            $("body").animate({scrollTop: $("#contact_us").offset().top - 70}, "slow");
          });
        }
      }
    }]) 
});

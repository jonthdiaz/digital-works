define(function  (require) {
    'use strict';

    var angular = require('angular');

    return angular.module('home.controllers', [])
            .controller('FormContactController',['$scope','HomeService',
                function  ($scope, HomeService) {
                  $scope.url_create_contact = "";
                  $scope.form_contact_q = false;
                  
                  $scope.form_contact_submit = function  (e) {
                    var self = this;
                    $scope.form =  angular.element(e.target);
                    
                    if(self.formContact.$valid){
                        $scope.form_contact_q = true;   
                        HomeService.request_create_contact(url, form).then(function  (data) {
                            if(data.success){

                            }else{
                                
                            }
                        });

                    }
                  }
            }])
})
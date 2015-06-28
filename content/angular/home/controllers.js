define(function  (require) {
    'use strict';

    var angular = require('angular');

    return angular.module('home.controllers', [])
            .controller('FormContactController',['$scope','HomeService','$timeout',
                function  ($scope, HomeService, $timeout) {
                  $scope.url_create_contact = "";
                  $scope.contact = {
                    name: '',
                    email: '',
                    observations: '',
                  }
                  var oriContact = angular.copy($scope.contact);
                  $scope.form_contact_q = false;
                  $scope.form_contact_error = false;
                  $scope.form_contact_success = false;
                  $scope.form_contact_submit = function  (e) {
                    var self = this;
                    $scope.form =  angular.element(e.target);
                    if(self.formContact.$valid){
                        $scope.form_contact_q = true;   
                        HomeService.request_create_contact($scope.url_create_contact, $scope.form).then(function  (data) {
                            if(data.success){
                                $scope.form_contact_success = true;
                                $scope.reset_form();
                                   $timeout(function  () {
                                     $scope.form_contact_success = false;
                                   }, 4000)
                            }else{
                                $scope.form_contact_error = true;
                            }
                        });
                    }
                  }
                  $scope.reset_form = function  () {
                      $scope.contact = angular.copy(oriContact);
                      $scope.formContact.$setPristine();
                  }
            }])
})
define(function  (require) {
    var angular = require("angular");

    return angular.module('home.services', [])
        .factory('HomeService', ['$http','$q', function($http, $q){
            function create_contact (url, form) {
                var deferred = $q.defer();
                $http({
                    method: "post",
                    url: url,
                    data:form.serialize(),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                }).success(function  (data) {
                   deferred.resolve(data); 
                });
                return deferred.promise;
            }
            return {
                request_create_contact: create_contact,                
            };
        }])
})
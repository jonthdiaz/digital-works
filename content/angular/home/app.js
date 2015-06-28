define(function  (require) {
    'use strict';
    var angular = require('angular');
    var angularAMD = require('angularAMD');
    var controllers = require("controllers");
    var services = require("services");
    var directives = require("directives");

    var app = angular.module('home', [
            controllers.name,
            services.name,
            directives.name,
        ])

    return angularAMD.bootstrap(app);
});

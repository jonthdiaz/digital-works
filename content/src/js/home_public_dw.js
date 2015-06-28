require.config({
    paths:{
        'jquery':'../../components/jquery/dist/jquery',
        'angular':'../../components/angular/angular',
        'angularAMD':'../../components/angularAMD/angularAMD',
        'bootstrap': '../../components/bootstrap-sass-official/assets/javascripts/bootstrap.min',
        'app': '../../angular/home/app',
        'controllers': '../../angular/home/controllers',
        'services': '../../angular/home/services',
        'directives': '../../angular/home/directives',
    },
    shim:{
        'jquery':{
            exports : 'jQuery'
        },
        'angular': {
            exports: 'angular',
        },
        'angularAMD':['angular'],
        'bootstrap':{
            deps: ['jquery']
        },
        'controllers':['angular'],
        'services':['angular'],
        'directives':['angular'],
        'app':['angular', 'controllers', 'services', 'directives'],
    },
    deps:['app'],
});

require(['jquery', 'bootstrap'],function  ($, bootstrap) {
   $(document).ready(function  () {
       
   });
});
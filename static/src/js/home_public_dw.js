require.config({
    paths:{
        'jquery':'../../components/jquery/dist/jquery',
        'angular':'../../components/angular/angular',
        'angularAMD':'../../components/angularAMD/angularAMD',
        'bootstrap': '../../components/bootstrap-sass-official/assets/javascripts/bootstrap.min'
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
        }
    },
});

require(['jquery', 'bootstrap'],function  ($, bootstrap) {
   $(document).ready(function  () {
       
   });
});
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
        'init_dom': '../../angular/home/init_dom',
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
        'init_dom': ['jquery', 'bootstrap'],
        'app':['angular', 'controllers', 'services', 'directives'],
    },
    deps:['app', 'jquery', 'bootstrap', 'init_dom'],
});
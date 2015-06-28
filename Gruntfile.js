module.exports = function (grunt) {
    grunt.initConfig({
        pkd: grunt.file.readJSON('package.json'),
        meta:{
            project: 'digital-workers',
            version: '0.1',
            banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Tutorya <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */'
        },

        uglify: {
            options:{
                banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Tutorya. Build Time: <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */',
                mangle: false,
                compress: true
            },

            build:{
                files: {
                    'content/build/js/home_public_dw.min.js': ['content/src/js/home_public_dw.js'],
                }
            }
        },

        clean: ['content/build/css', 'content/build/js'],

        compass: {
            dist : {
                options: {
                    config: 'content/config.rb',
                }
            },
            dev : {
                options: {
                    config: 'content/config_dev.rb',
                }
            }
        },
        concurrent: {
            options: {
                logConcurrentOutput: true
            },
            dev: {
                tasks: ['watch:compass_dev']
            },
            jade: {
              tasks: ['watch:jade']
            },
        },
        sass: {
            options:{
                includePaths: ['content/components/compass-mixins/lib'],
                imagePath: '../../imgs',
                outputStyle: 'nested',
                sourceMap: true,
                indentedSyntax: true,
                sourceComments: true,
            },
            dist:{
                files: [{
                    expand: true,
                    cwd: "content/styles/",
                    src: ['**/*.sass', '**/*.scss', '!**/_*.scss'],
                    dest: "content/styles/css",
                    ext: ".css",
                }],
                options: {
                    livereload: true
                }
            }
        },
        watch: {
            compass:{
                files: ['content/**'],
                tasks: ['compass:dev'],
            },

            compass_dev: {
                files: ['content/**'],
                tasks: ['sass:dist'],
                options:{
                    livereload: true
                }
            },
            jade: {
              files: ['templates-jade/**'],
              tasks: ['jade']
            }
        },
        requirejs:{
            compile: {
                options:{
                    optimize: 'uglify2',
                    baseUrl: 'content/src/js',
                    dir: 'content/build/js',
                    preserveLicenseComments: false,
                    "uglify2":{
                        'mange': false,
                        'compress': true,
                    },
                    paths:{
                        'jquery':'../../components/jquery/dist/jquery',
                        'angular':'../../components/angular/angular',
                        'angularAMD':'../../components/angularAMD/angularAMD',
                        'bootstrap': '../../components/bootstrap-sass-official/assets/javascripts/bootstrap.min',
                        'home_app': '../../angular/home/app',
                        'home_controllers': '../../angular/home/controllers',
                        'home_services': '../../angular/home/services',
                        'home_directives': '../../angular/home/directives',
                    },
                    shim: {
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
                    },

                modules: [
                        {
                            name: 'home_public_dw',
                        }
                    ]
                }
            }
        },
        jade: {
            html: {
              src:['templates-jade/**/*.jade'],
              dest: "templates",
              options:{
                basePath: 'templates-jade',
                client: false,
                pretty: true,
              }
            }

        },
    });

grunt.loadNpmTasks('grunt-contrib-requirejs');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-clean');
grunt.loadNpmTasks('grunt-concurrent');
grunt.loadNpmTasks('grunt-sass');
grunt.loadNpmTasks('grunt-jade');

grunt.registerTask( 'production', ['clean', 'compass:dist', 'requirejs', 'uglify'])
grunt.registerTask( 'dev', ['concurrent:dev'])
grunt.registerTask( 'dev-jade', ['concurrent:jade'])

};

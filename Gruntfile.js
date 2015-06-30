module.exports = function (grunt) {
    var matches = grunt.file.expand("./content/src/js/*.js");
    var requirejsOptions = {};
    if (matches.length > 0) {
        for (var x = 0; x < matches.length; x++) {
            var namefile = matches[x].replace('./content/src/js/', '');
            namefile = namefile.replace('.js','');
            requirejsOptions['task' + x] = {
                "compile":{
                    "options": {
                        //'findNestedDependencies': true, 
                        "baseUrl": "./",
                        //"appDir": 'content/src/js/', 
                        //"dir": 'content/build/js',
                        "mainConfigFile": 'content/src/config.js',
                        //"wrap": true,
                        //"name": "content/src/js/" + namefile,
                        "out": "content/build/js/" + namefile + ".min.js",
                        //"optimize": "uglify2",
                        //"uglify2": {
                        //    "mangle": false
                        //},
                        //"generateSourceMaps": false,
                        //"preserveLicenseComments": false,
                        //"done": function(done, output) {
                        //    done();
                        //}
                    }    
                }
                
            };
        }
    }
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
        requirejs:requirejsOptions,
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

grunt.loadNpmTasks('grunt-requirejs');
//grunt.loadNpmTasks('grunt-contrib-requirejs');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-clean');
grunt.loadNpmTasks('grunt-concurrent');
grunt.loadNpmTasks('grunt-sass');
grunt.loadNpmTasks('grunt-jade');

grunt.registerTask( 'production', ['clean', 'compass:dist', 'requirejs'])
grunt.registerTask( 'dev', ['concurrent:dev'])
grunt.registerTask( 'dev-jade', ['concurrent:jade'])
grunt.registerTask( 'default', ['requirejs'])

};

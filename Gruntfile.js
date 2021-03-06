module.exports = function (grunt) {
    var matches = grunt.file.expand("./content/src/js/*.js");
    var requirejsOptions = {};
    if (matches.length > 0) {
        for (var x = 0; x < matches.length; x++) {
            var namefile = matches[x].replace('./content/src/js/', '');
            namefile = namefile.replace('.js','');
            requirejsOptions['task' + x ] = {
                    "options": {
                        'appDir': 'content/src/js',
                        'dir': 'content/build/js',
                        'mainConfigFile': 'content/src/commons/' + namefile + '.js',
                        'optimize': 'uglify2',
                        uglify2: {
                            options:{
                                banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Digital workers. Build Time: <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */',
                                mangle: false,
                                compress: true
                            },
                        },
                        'normalizeDirDefines': 'skip',
                        'skipDirOptimize': true,
                        'modules': [{
                            'name': namefile,
                            }
                        ]
                    },
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
                    'content/build/js/require.min.js': ['content/components/requirejs/require.js'],
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
              tasks: ['jade:html']
            }
        },
        requirejs: requirejsOptions,
        jade: {
            html: {
              src:['templates-jade/**/*.jade'],
              dest: "templates",
              options:{
                basePath: 'templates-jade',
                client: false,
                pretty: true,
              }
            },
            prod:{
                  src:['templates-jade/**/*.jade'],
                  dest: "templates",
                  options:{
                    basePath: 'templates-jade',
                    client: false,
                    pretty: false,
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

grunt.registerTask( 'production', ['clean', 'compass:dist', 'requirejs','jade:prod','uglify'])
grunt.registerTask( 'dev', ['concurrent:dev'])
grunt.registerTask( 'dev-jade', ['concurrent:jade'])

};

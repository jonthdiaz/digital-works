module.exports = function  (grunt) {
    grunt.initConfig({
        pkd: grunt.file.readJSON('package.json'),
        meta:{
            project: 'digital-workers',
            version: '0.1',
            banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Tutorya <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */'
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
                    config: 'content/config_dev/rb',
                }
            }
        },
        concurrent: {
            options: {
                logConcurrentOutput: true
            },
            dev: {
                tasks: ['watch:compass_dev']
            }
        },
        sass: {
            options:{
                includePaths: ['content/components/compass-mixins/lib'],
                outputStyle: 'compressed',
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
            }
        }
    });  

grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-clean');
grunt.loadNpmTasks('grunt-concurrent');
grunt.loadNpmTasks('grunt-sass');

grunt.registerTask( 'production', ['clean', 'compass:dist'])
grunt.registerTask( 'dev', ['concurrent:dev'])

};
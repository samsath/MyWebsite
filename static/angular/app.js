'use strict';

angular.module('personal',['ngSanitize','ngRoute','ui.router','ngAnimate','personal.controllers'])

    .config(['$httpProvider','$interpolateProvider', function($httpProvider, $interpolateProvider){
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    }])

    .run(['$http','$route','$rootScope','$state', function($http, $route, $rootScope, $state){
        $rootScope.$on("$stateChangeError", console.log.bind(console));
        $rootScope.tomenu = function(){
            $state.go('home');
        };
        $rootScope.goBack = function() {
            window.history.back();
        };
    }])

    .config(function($stateProvider, $urlRouterProvider, $locationProvider){

        $urlRouterProvider.otherwise("/");

        $stateProvider
            .state("home",{
                views:{
                    'controls':{
                        templateUrl:'/static/templates/home.control.html',
                        controller:'HomeLeftCtrl'
                    },
                    'main':{
                        templateUrl:'/static/templates/home.list.html',
                        controller:'HomeCtrl'
                    }
                },
                url:"/"
            })
            .state("project",{
                url:"/project/:name",
                views:{
                    'controls':{
                        templateUrl:'/static/templates/project.control.html',
                        controller:'ProjectCtrCtrl'
                    },
                    'main':{
                        templateUrl:'/static/templates/project.list.html',
                        controller:'ProjectCtrl'
                    }
                }
            })
    });

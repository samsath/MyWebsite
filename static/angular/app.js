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

        $locationProvider.html5Mode(true);
        $urlRouterProvider.otherwise("/");

        $stateProvider
            .state("home",{
                url:"/",
                templateUrl:'/static/templates/home.html',
                controller:'HomeCtrl'
            })
            .state("project",{
                url:"/project/:name",
                templateUrl:'/static/templates/project.html',
                controller:'ProjectCtrl'
            })
    });

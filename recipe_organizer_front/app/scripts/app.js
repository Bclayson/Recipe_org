'use strict';

/**
 * @ngdoc overview
 * @name angularProjectApp
 * @description
 * # angularProjectApp
 *
 * Main module of the application.
 */
angular
    .module('angularProjectApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'restangular'
    ])
    .config(function ($routeProvider, RestangularProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .when('/about', {
                templateUrl: 'views/about.html',
                controller: 'AboutCtrl'
            })
            .when('/recipes/:recipeId', {
                templateUrl: 'views/recipe_details.html',
                controller: 'RecipeDetailsCtrl'
            })
            .when('/add-recipe', {
                templateUrl:'views/add_recipe.html',
                controller: 'AddRecipeCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
        RestangularProvider.setBaseUrl('http://localhost:8002');
    });

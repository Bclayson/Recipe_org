'use strict';

/**
 * @ngdoc function
 * @name angularProjectApp.controller:RecipeDetailsCtrl
 * @description
 * # RecipeDetailsCtrl
 * Controller of the angularProjectApp
 */
angular.module('angularProjectApp')
    .controller('RecipeDetailsCtrl', function ($scope, $routeParams, Restangular, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        });

        $scope.ingredientName = $routeParams.ingredientName;

        Restangular.one('recipes', $scope.ingredientName).customGET().then(function (data) {
            $scope.ingredients = data;
        });

        $scope.deleteRecipe = function () {
            var response = confirm("Are you sure you want to delete this recipe?");
            if (response == true) {
                Restangular.one('recipes', $scope.recipeId).customDELETE().then(function () {
                    $location.path('/recipes');
                }, function () {
                    $scope.status = "The recipe couldn't be deleted";
                });
            }
        };
    });

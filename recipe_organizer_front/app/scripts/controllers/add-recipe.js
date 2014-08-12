'use strict';

/**
 * @ngdoc function
 * @name recipeOrganizerFrontApp.controller:AddRecipeCtrl
 * @description
 * # AddRecipeCtrl
 * Controller of the recipeOrganizerFrontApp
 */
angular.module('angularProjectApp')
    .controller('AddRecipeCtrl', function ($scope, Restangular) {
        $scope.recipe = {};
        $scope.saveNewRecipe = function () {

            Restangular.all('add-recipe').customPOST($scope.recipe).then(function () {
                $scope.status = alert("The recipe was successfully created!");
                $scope.recipe = {}

            }, function () {
                $scope.status = "The recipe couldn't be saved";
            });
        };
    });

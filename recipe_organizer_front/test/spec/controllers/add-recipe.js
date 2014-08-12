'use strict';

describe('Controller: AddRecipeCtrl', function () {

  // load the controller's module
  beforeEach(module('angularProjectApp'));

  var AddRecipeCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    AddRecipeCtrl = $controller('AddRecipeCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});

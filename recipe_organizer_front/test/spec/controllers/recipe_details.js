'use strict';

describe('Controller: RecipeDetailsCtrl', function () {

  // load the controller's module
  beforeEach(module('angularProjectApp'));

  var RecipeDetailsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    RecipeDetailsCtrl = $controller('RecipeDetailsCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});

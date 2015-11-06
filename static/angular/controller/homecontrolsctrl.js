angular.module('personal.controllers').controller('HomeLeftCtrl', ['$scope',  function($scope) {
    $scope.details = false;
    $scope.clearDetails = function(){
        console.log('home');
    }
}]);
angular.module('personal.controllers').controller('HomeCtrl', ['$scope', 'WorkSrv', function($scope, WorkSrv){
    $scope.details = false;

    $scope.projects = [];

    WorkSrv.getall().then(function(res){
        console.log(res);
        $scope.projects = res;
    });


}]);

angular.module('personal.controllers').controller('HomeCtrl', ['$scope', 'WorkSrv', function($scope, WorkSrv){
    $scope.details = false;
    $scope.detailstop = false;
    $scope.detailsbg = false;

    $scope.projects = [];

    WorkSrv.getall().then(function(res){
        console.log(res);
        $scope.projects = res;
    });

    $scope.selectPro = function(item){
        $scope.detailstop = true;
        $scope.detailsbg = true;
        $scope.details = $scope.projects[item];
    };

    $scope.clearDetails = function(){
        $scope.details = false;
        $scope.detailstop = false;
        $scope.detailsbg = false;
    };

    $('.mainsection').css('background-color','#ffffff');


}]);

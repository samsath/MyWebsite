/**
 * Created by sam on 05/11/15.
 */

angular.module('personal.controllers').controller('ProjectCtrCtrl', ['$scope', '$state','$stateParams','WorkSrv', function($scope ,$state,$stateParams,WorkSrv){

    WorkSrv.slug($stateParams.name).then(function(res) {
        $scope.left = res.objects[0];
    });
    $scope.clearDetails = function(){
        $state.go('home');
    }
}]);
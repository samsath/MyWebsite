angular.module('personal.controllers').controller('ProjectCtrl', ['$scope', '$state','$stateParams','WorkSrv', function($scope ,$state,$stateParams,WorkSrv){

    function invertColor(hexTripletColor) {
        var color = hexTripletColor;
        color = color.substring(1);           // remove #
        color = parseInt(color, 16);          // convert to integer
        color = 0xFFFFFF ^ color;             // invert three bytes
        color = color.toString(16);           // convert to hex
        color = ("000000" + color).slice(-6); // pad with leading zeros
        color = "#" + color;                  // prepend #
        return color;
    }

    WorkSrv.slug($stateParams.name).then(function(res){
        $scope.work = res.objects[0];
        $('.mainsection').css('background-color',$scope.work.background).css('color',invertColor($scope.work.background));

    })
}]);
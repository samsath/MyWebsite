angular.module('personal.services').service('FileSrv',['$http', function($http){
    var files = function(data){
        angular.extend(this, data);
    };

    var url ='/api/v1/files';
    var format = '?format=json';

    files.getall = function(){
        return $http.get(url + format).then(function(res){
            return new files(res.data);
        });
    };

    files.getProject = function(id){
        return $http.get(url +'/'+ id +'/'+ format).then(function(res){
            return new files(res.data);
        });
    };

    return files;

}]);

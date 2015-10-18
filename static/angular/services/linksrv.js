angular.module('personal.services').service('LinkSrv',['$http', function($http){
    var links = function(data){
        angular.extend(this, data);
    };

    var url ='/api/v1/links';
    var format = '?format=json';

    links.getall = function(){
        return $http.get(url + format).then(function(res){
            return new links(res.data);
        });
    };

    links.getProject = function(id){
        return $http.get(url +'/'+ id +'/'+ format).then(function(res){
            return new links(res.data);
        });
    };

    return links;

}]);

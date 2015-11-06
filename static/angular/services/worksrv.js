angular.module('personal.services').service('WorkSrv',['$http', function($http){
    var feed = function(data){
        angular.extend(this, data);
    };

    var url ='/api/v1/work';
    var format = '?format=json';

    feed.getall = function(){
        return $http.get(url + format).then(function(res){
            return new feed(res.data.objects);
        });
    };

    feed.getProject = function(id){
        return $http.get(url +'/'+ id +'/'+ format).then(function(res){
            return new feed(res.data);
        });
    };

    feed.slug = function(id){
        return $http.get(url + '/?slug=' + id + '&format=json').then(function(res){
            return new feed(res.data);
        });
    };

    return feed;

}]);

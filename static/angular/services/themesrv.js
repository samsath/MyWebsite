angular.module('personal.services').service('ThemeSrv',['$http', function($http){
    var themes = function(data){
        angular.extend(this, data);
    };

    var url ='/api/v1/themes';
    var format = '?format=json';

    themes.getall = function(){
        return $http.get(url + format).then(function(res){
            return new themes(res.data);
        });
    };

    themes.getProject = function(id){
        return $http.get(url +'/'+ id +'/'+ format).then(function(res){
            return new themes(res.data);
        });
    };

    return themes;

}]);

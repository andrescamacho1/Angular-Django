var app=angular.module("app",['ngResource']);

app.controller('controlador', function($scope,listado){

	$scope.lista=listado.get();

});

app.factory('listado', function($resource){
	return $resource("http://127.0.0.1:8000/Materia/", {},{get:{method:'GET',isArray:true}});
})
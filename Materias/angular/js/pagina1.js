var app=angular.module("app",['ngResource']);

app.controller("controlador", function($scope,listado){

	$scope.lista=listado.get();

	$scope.contador= function(posicion){
		var dato=$scope.idCedula;
		var s=0;

		for (var i = 0; i< $scope.lista.length; i++) {

			if (angular.equals(dato,$scope.lista[i].cedula )) {
				alert($scope.lista[i].cedula);
				window.location.href='pagina2.html';
			}else{
				s=2;
			}
		}
		return s;
	};

	

	$scope.agregar=function(){
		$scope.lista.push({cedula:$scope.idCedula});
		$scope.idCedula="";
	
	};

});


app.factory("listado",function($resource){
    //$http es un servicio htttp , hace lo mismo que 
    return $resource("http://127.0.0.1:8000/Alumno", {}, {get:{method:"GET",isArray:true}});
    //return $resource("http://127.0.0.1:8000/Materia/?format=json", {}, {get:{method:"GET",isArray:false}});    


});
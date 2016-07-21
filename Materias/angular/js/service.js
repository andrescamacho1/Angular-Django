var app=angular.module("app",['']);
function Login() {

   var logged=false;

   this.login=function(user,password) {
      if ((user==="a") && (password==="b")) {
         logged=true;
      }

     return logged;
   }
   
   this.isLogged=function() {
     return logged;
   }


}

app.service("login",Login);
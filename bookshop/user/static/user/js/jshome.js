$(document).ready(function(){
    $(".div-log").hide();
    $(".div-reg").hide();
    $(".log-in").click(function (){
        $(".div-log").slideToggle();
        $(".div-reg").hide();
        });

    $("#sign-up").click(function (){
        $(".div-reg").slideToggle();
        $(".div-log").hide();
    });
});
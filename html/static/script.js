$(function(){$("nav .menu").hover(function(){$(this).find("a").css("z-index",2);$(this).find("ul").show();$(this).parents("header").css("z-index",999);},function(){$(this).find("a").css("z-index",0);$(this).find("ul").hide();$(this).parents("header").css("z-index",1);});$("header>h1>a").click(function(){$(this).attr("href","javascript:;");$("html,body").animate({scrollTop:0},500);});$(".at").click(function(){$box=$(this).attr("data-box");$top=$($box).offset().top;$("html,body").animate({scrollTop:$top-100},1000,function(){$(".nav").slideDown(300);});return false;});});
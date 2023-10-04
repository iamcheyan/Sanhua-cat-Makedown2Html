$(function(){
	// $(window).scroll(function(){
		// $s = $(document).scrollTop();
		// $(".nav").addClass("fixed").show().css("top", $s);
		
		// $bookTop = $(".box.book").offset().top;
		// $projectTop = $(".box.project").offset().top;
		// $cheTop = $(".che").offset().top;
		
		// if ($s > $bookTop){
			// $(".box.book").animate({
				// paddingTop : 220
			// });
			// $(".nav").addClass("fixed").show().css("top", $bookTop + 50);
		// } if ($s > $projectTop || $s > ($projectTop - 800)){
			// $(".box.project").animate({
				// paddingTop : 220
			// });
			// $(".nav").addClass("fixed").show().css("top", $projectTop + 30);
		// } if ($s < 280){
			// $("header.fixed").hide();
		// };
	// });
	
	$("nav .menu").hover(function(){
		$(this).find("a").css("z-index",2);
		$(this).find("ul").show();
		$(this).parents("header").css("z-index",999);
	},function(){
		$(this).find("a").css("z-index",0);
		$(this).find("ul").hide();
		$(this).parents("header").css("z-index",1);
	});
	$("header>h1>a").click(function(){
		$(this).attr("href","javascript:;");
		$("html,body").animate({
			scrollTop: 0
		},500);
	});
	$(".at").click(function(){		
		$box = $(this).attr("data-box");	
		$top = $($box).offset().top;
		$("html,body").animate({
			scrollTop: $top -100
		},1000,function(){
			$(".nav").slideDown(300);
		});
		return false;
	});
	
});


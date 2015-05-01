function submit_word(s){
	
	// 渲染关系图
	postJson("/get_vec", {"word": s}, function(data){
  	  	render({ center: s,  word: data} )
    })  

 	// 获取百度百科的简介
    $("#baike_name").html(s)
    $.ajax({
	      url: "/baike", 
	      type: "post", 
	      data: JSON.stringify( {"word": s} ), 
	      contentType:"application/json",
	      success:function(data){
	        if (data != 'None'){
	          $("#baike").html(data)
	        }else{
	          $("#baike").html("百科中缺少介绍")
	        }

	        $("#baike_container").show()
	      }
   	})

    // 画出该词条最近的热点趋势图
    postJson("/get_heats", {"word": s}, function(data){
		draw_heat(s, data)
    })
}

$(function(){
	postJson("/get_top_word", {}, function(data){
		$.each(data, function(i, item){
			$("#top_word").append("<a href='#' class='top-word'>" + item.word + "</a>")
		})

		$("a.top-word").click(function(){
			submit_word($(this).html())
		})
	})
	$("#submit").click(function(){
	    submit_word($("#word").val())
  	})

  	$("a[rel*=leanModal]").leanModal({top:200})
})
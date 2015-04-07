$(function(){
	function submit_word(s){
		postJson("/get_vec", {"word": s}, function(data){
	      render({ center: s,  word: data} )
	    })  
	}
	postJson("/get_top_word", {}, function(data){
		$.each(data, function(i, item){
			$("#top_word").append("<a href='#' class='top-word'>" + item + "</a>")
		})

		$("a.top-word").click(function(){
			submit_word($(this).html())
		})
	})
	$("#submit").click(function(){
	    submit_word($("#word").val())
  	})
})
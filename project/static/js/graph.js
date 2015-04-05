$(function(){ // on dom ready
        function render(data){
          $("#graph").cytoscape({
                layout: {name: "concentric"} ,
                style: cytoscape.stylesheet()
                    .selector('node')
                      .css({
                          'background-color': 'red',
                          'content': 'data(id)',
                          'width': 'data(weight)',
                          'height': 'data(weight)', 
                          'text-valign': 'center', 
                          'text-halign': 'center'
                      })
                    .selector("edge")
                      .css({
                          'width': "data(weight)"
                      })
                    .selector()
                      .css({
                      })
          })
          
          var cy = $("#graph").cytoscape("get")

          cy.add({
              group: "nodes",
              data: { id: data.center, weight: 100},
          })

          $.each(data.word, function(i, item){
                cy.add([ { group: "nodes", data: { id: i,  weight: item*80 + 20 } }, 
                            { group: "edges", data: { id: "e"+i, source: data.center,  target: i, weight: item*5} }
                ])
          })

          cy.nodes().on("click", function(){    
               cy.center(this)
               newword = this.id()
               postJson("/get_vec", {"word": newword}, function(data){
                  render({ center: newword,  word: data} )
               })  
          });
      }
      
      $("#submit").click(function(){
          postJson("/get_vec", {"word": $("#word").val()}, function(data){
            render({ center: $("#word").val(),  word: data} )
          })  
      })
      
      render({center: "lmx", word: {"wyc": 1.0, "basketball": 0.2, "cs": 0.5 }})
}); // on dom ready
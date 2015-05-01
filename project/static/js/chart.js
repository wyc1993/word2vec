function draw_heat(name, data){
    y_value = []
    x_cate = []
    $.each(data, function(i, item){
        x_cate.push(i);
        y_value.push(item);
    })

	$('#chart_container').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: '过去一年热度值变化'
        },
        xAxis: {
            title: {
                text: "时间"
            },
            categories: x_cate
        },
        yAxis: {
            title: {
                text: '热度值'
            }
        },
        series: [{
            data: y_value
        }]
    });
}

function draw_hotword(data, div, m){
    x_cate = []
    y_value = []
    $.each(data, function(i, item){
        x_cate.push(item.word)
        y_value.push(item.heat)
    })

    console.log(x_cate)
    console.log(y_value)

    $(div).highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: m + '个月前的热度排行'
        },
        xAxis: {
            categories: x_cate
        },
        yAxis: {
            title: {
                text: "热度值"
            }
        },
        series: [ {
            name: '热度值',
            data: y_value
        }]
    });
}
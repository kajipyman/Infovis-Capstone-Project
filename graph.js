// 参考にした実装： https://bl.ocks.org/d3noob/119a138ef9bd1d8f0a8d57ea72355252
// set the dimensions and margins of the graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 700 - margin.left - margin.right,
    height = 140 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%Y%m%d%H");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the area
var area = d3.area()
    .x(function(d) { return x(d.date); })
    .y0(height)
    .y1(function(d) { return y(d.score); });

// define the line
var valueline = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.score); });

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select(".header_all").append("svg")
    .attr("class", "graph_svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

// get the data
d3.csv("./storage/transition.csv").then(function (data) {
    var trans;
    data.forEach(function (val){
        if(val["name"] === decodeURI(arg["kw"])){
            delete val["name"];
            trans = val;
        }
    });
    var objs_list = [];
    Object.keys(trans).forEach(function(key) {
        objs_list.push({"date": parseTime(key), "score": +this[key]})
    }, trans);

    // scale the range of the data
    x.domain(d3.extent(objs_list, function(d) { return d.date; }));
    y.domain([0, d3.max(objs_list, function(d) { return d.score; })]);

    // add the area
    svg.append("path")
        .data([objs_list])
        .attr("class", "area")
        .attr("d", area);

    // add the valueline path.
    svg.append("path")
        .data([objs_list])
        .attr("class", "line")
        .attr("d", valueline);

    // ドラッグ選択用の短冊
    var rect = svg.append("g")
        .selectAll("rect")
        .data(objs_list)
        .enter()
        .append("rect")
        .attr("class", "svg_rect")
        .attr("id", function(d, i){ return "rect_" + i; })
        .attr("x", function(d, i){
            return x(d.date);
        })
        .attr("y", 0)
        .attr("width", function (d, i) {
            return i === objs_list.length - 1 ? 0 : x(objs_list[1].date) - x(objs_list[0].date)
        })
        .attr("height", height)
        .attr("fill", "steelblue")
        .style("opacity", 0);

    // ドラッグ選択の実装
    var drag_start_id = null;
    var drag_small_id = null;
    var drag_large_id = null;
    var drag_now_id = null;
    var selected_ids = [];
    var time_scale = [];
    rect.on("mouseover", function (d, i) {
        let flag = false;
        for (let j = 0; j < selected_ids.length; j++){
            if(selected_ids[j] === i){
                flag = true;
                break;
            }
        }
        if(!flag){ d3.select("#rect_" + i).style("opacity", 0.2); }
            d3.select("#point_" + i).style("opacity", 1);
        })
        .on("mouseout", function (d, i) {
            let flag = false;
            for (let j = 0; j < selected_ids.length; j++){
                if(selected_ids[j] === i){
                    flag = true;
                    break;
                }
            }
            if(!flag){ d3.select("#rect_" + i).style("opacity", 0); }
            d3.select("#point_" + i).style("opacity", 0);
        });

    rect.call(d3.drag()
        .on("start", function(d, i){
            selected_ids = [i];
            drag_start_id = drag_now_id = i;
            d3.select("body").style("cursor", "col-resize");
        })
        .on("drag", select_fill)
        .on("end", function (d, i){
            d3.select("body").style("cursor", "auto");
            select_fill(d, i);
            time_scale = selected_ids.length === 0
                ? []
                : [objs_list[selected_ids[0]].date, objs_list[selected_ids[selected_ids.length - 1] + 1].date]
            if(time_scale.length !== 0){
                d3.selectAll(".article")
                    .each(function (d, i) {
                        let arti = d3.select("#" + this.id);
                        let pub_date = utcPerser(arti.select(".article_info_date").text().slice(0, -4));
                        if(time_scale[0] > pub_date || pub_date > time_scale[1]){
                            arti.style("opacity", 0.3)
                        }
                    })
            }
        }))
        .on("click", function (d, i) {
            selected_ids = [];
            time_scale = [];
            rect.attr("fill", "steelblue");
            d3.selectAll(".article").style("opacity", 1)
        });

    function select_fill(d, i) {
        if (objs_list[0].date.getTime() > x.invert(d3.event.x).getTime()){
            drag_now_id = 0;
        }else if(x.invert(d3.event.x).getTime() > objs_list[objs_list.length - 1].date.getTime()){
            drag_now_id = objs_list.length - 2;
        }else{
            for(let j = 0; j < objs_list.length - 1; j++){
                if (objs_list[j].date.getTime() < x.invert(d3.event.x).getTime() && x.invert(d3.event.x).getTime() < objs_list[j + 1].date.getTime()){
                    drag_now_id = j;
                    break;
                }
            }
        }
        selected_ids = [];
        drag_small_id = Math.min(drag_start_id, drag_now_id);
        drag_large_id = Math.max(drag_start_id, drag_now_id);
        for(let j = 0; j < objs_list.length; j++){
            if(drag_small_id <= j && j <= drag_large_id){
                selected_ids.push(j);
                d3.select("#rect_" + j).style("opacity", 0.2)
            }else {
                d3.select("#rect_" + j).style("opacity", 0)
            }
        }
    }

    var utcPerser = d3.utcParse("%Y-%m-%d %H:%M:%S");

    // add the X Axis
    var today = null;
    var x_axis = svg.append("g")
        .attr("class", "x_axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x)
            .tickFormat(function(d){
                let zero_fill_minute = String(d.getUTCMinutes()).length === 1 ? "0" + d.getUTCMinutes() : d.getUTCMinutes();
                if(today !== d.getUTCDate()){
                    today = d.getUTCDate();
                    return (d.getUTCMonth() + 1) + "/" + d.getUTCDate() + " " + d.getUTCHours() + ":" + zero_fill_minute;
                }else{
                    return d.getUTCHours() + ":" + zero_fill_minute;
                }
            }));
    x_axis.selectAll("text").attr("fill", "#444444");
    x_axis.selectAll(".domain").attr("stroke", "#e0e0e0");

    // add the Y Axis
    var y_axis = svg.append("g")
        .attr("class", "y_axis")
        .call(d3.axisLeft(y)
            .ticks(3)
            .tickSizeInner(-width)
            .tickSizeOuter(3)
            .tickPadding(7))
        .attr("color", "#e0e0e0")
        .attr("stroke-width", "1px")
        .attr("opacity", 0)
        .selectAll("text").attr("fill", "#444444");

    svg.on("mouseover", function () {
            d3.select(".y_axis").attr("opacity", 1)
        })
        .on("mouseout", function () {
            d3.select(".y_axis").attr("opacity", 0)
        });

    svg.append("text")
        .attr("x", 230)
        .attr("y", -20)
        .attr("dy", "0.71em")
        .attr("fill", "#444444")
        .text("Topicality Degree of the Keyword");

});

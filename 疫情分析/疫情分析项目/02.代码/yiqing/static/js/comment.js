function fajax(id, url) {
    var chart = echarts.init(id, 'white', {renderer: 'canvas'});
    return $.ajax({
        type: "GET",
        url: url,
        dataType: 'json',
        success: function (result) {
            chart.setOption(result);
        }
    })
}

function fdataGrid(id, col, path) {
    $(id).datagrid({
        url: path,
        method: "get",
        columns: col,
        fitColumns: true,
        nowrap: true,//数据长度超出列宽时将会自动截取。
    });
}

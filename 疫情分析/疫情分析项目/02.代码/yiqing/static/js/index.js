// $('#dg1').datagrid({
//            url: 'datagrid_data.json',
//            columns: [[
//                {field: 'code', title: 'Code', width: 100},
//                {field: 'name', title: 'Name', width: 100},
//                {field: 'price', title: 'Price', width: 100,}
//            ]]
//        });

style=function(value, row, index) {
    return 'vertical-align:middle;';
}
columns1 = [[
    {field: 'name', title: '地区', width: 180,align:'center',style},
    {field: 'nowConfirm', title: '现有确诊', width: 180,align:'center',style},
    {field: 'confirm', title: '累计确诊', width: 180,align:'center',style},
    {field: 'suspect', title: '疑似病例', width: 180,align:'center',style},
    {field: 'dead', title: '死亡病例', width: 180,align:'center',style},
    {field: 'heal', title: '治愈人数', width: 180,align:'center',style},
    {field: 'deadRate', title: '死亡率/%', width: 180,align:'center',style},
    {field: 'importedCase', title: '境外输入', width: 180,align:'center',style},
]]

columns2 = [[
    {field: 'name', title: '地区', width: 130,align:'center',style},
    {field: 'nowConfirm', title: '现有确诊', width: 130,align:'center',style},
    {field: 'confirm', title: '累计确诊', width: 130,align:'center',style},
    {field: 'suspect', title: '疑似病例', width: 130,align:'center',style},
    {field: 'dead', title: '死亡病例', width: 130,align:'center',style},
    {field: 'heal', title: '治愈人数', width: 130,align:'center',style},
    {field: 'importedCase', title: '境外输入', width: 130,align:'center',style},
    {field: 'healRate', title: '治愈率/%', width: 130,align:'center',style},
    {field: 'deadRate', title: '死亡率/%', width: 130,align:'center',style},
]]

columns3 = [[
    {field: 'name', title: '地区', width: 100,align:'center',style},  
    {field: 'nowConfirm', title: '现有确诊', width: 100,align:'center',style}, 
    {field: 'confirm', title: '累计确诊', width: 100,align:'center',style},
    {field: 'suspect', title: '疑似病例', width: 100,align:'center',style},
    {field: 'dead', title: '死亡病例', width: 100,align:'center',style},
    {field: 'heal', title: '治愈人数', width: 100,align:'center',style},
    {field: 'continent', title: '大洲', width: 100,align:'center',style},
    {field: 'isUpdated', title: '是否更新', width: 100,align:'center',style}
]]

columns4 = [[
    {field: 'name', title: '地区', width: 100,align:'center',style}, 
    {field: 'confirm', title: '累计病例', width: 100,align:'center',style},
    {field: 'suspect', title: '疑似病例', width: 100,align:'center',style},
    {field: 'dead', title: '死亡病例', width: 100,align:'center',style},
    {field: 'heal', title: '治愈人数', width: 100,align:'center',style},
    {field: 'date', title: '更新日期', width: 100,align:'center',style},
    {field: 'nameMap', title: '地区名', width: 100,align:'center',style},
    {field: 'isUpdated', title: '是否更新', width: 100,align:'center',style}
]]

fdataGrid('#dg1', columns1, '../static/json/中国各省市总体疫情信息.txt')

fdataGrid('#dg2', columns2, '../static/json/广东.txt')

fdataGrid('#dg3', columns3, '../static/json/世界总体疫情信息.txt')

fdataGrid('#dg4', columns4, '../static/json/美国.txt')

$('#Main_').css({padding: 0})

$('html body').css({backgroundColor: '#f4f4f4'})

$('.layui-header .layui-nav-item').removeClass('layui-this').eq(0).addClass('layui-this')

panel = $('.panel.datagrid')

$('#all-show').click(function () {
    panel.show()
})
$('.layui-nav.layui-nav-tree .layui-nav-child')
    .find('dd').click(function (event) {
    console.log(222)
    panel.hide()
    panel.eq(0).show()
    event.stopPropagation();    //  阻止事件冒泡
}).next().click(function (event) {
    panel.hide()
    panel.eq(1).show()
    event.stopPropagation();    //  阻止事件冒泡
}).next().click(function (event) {
    panel.hide()
    panel.eq(2).show()
    event.stopPropagation();    //  阻止事件冒泡
}).next().click(function (event) {
    panel.hide()
    panel.eq(3).show()
    event.stopPropagation();    //  阻止事件冒泡
})
import re
from lxml import etree

req_text = '''HTTP/1.1 200 OK
Server: nginx
Date: Mon, 11 Mar 2019 05:47:50 GMT
Content-Type: text/html;charset=GB2312
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
XYWY_HEADER: admin01.node.kddi.op.xywy.com
Content-Length: 7102

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>分诊后台管理系统</title>
<link href="css/css.css" rel="stylesheet" type="text/css" />
<style type="text/css">
<!--
.lanbeifont{font:"宋体"; font-size:12px; padding-left:18px;}
-->
</style>
<script language="javascript" src="http://fzadmin.z.xywy.com/js/jquery-1.7.2.min.js"></script>
<script language="javascript" src="http://fzadmin.z.xywy.com/js/global.js"></script>
<link href="http://fzadmin.z.xywy.com/js/date/skin/WdatePicker.css"/>
<script language="javascript" src="http://fzadmin.z.xywy.com/js/date/WdatePicker.js"></script>

</head>

<body><script language="javascript" src="http://fzadmin.z.xywy.com/js/jquery-1.6.js"></script>
<style type="text/css">
.grade_1{}
.grade_2{color:#0f0}
.grade_3{color:#f00}
.button{width:100px;height:30px;border:1px solid green;float:left;line-height:30px;text-align:center;cursor:pointer;color:black;}
.current{background-color:#007B48;color:white;}
.choose-team{margin-left:1%}
.explain{height:30px;line-height:30px;text-align:center;}
</style>
<script>
    function check_time()
    {
        var startdate = $("#startdate").val(),
            enddate = $("#enddate").val(),
            team = $(".button.current").attr("data-attr");
        if(startdate || enddate){
            if(!startdate)
            {
                alert("请选择搜索开始时间");
                return false;
            }
            
            if(!enddate)
            {
                alert("请选择搜索结束时间");
                return false;
            }
            var start_arr = startdate.replace(/-/g,''),
                end_arr =enddate.replace(/-/g,'');

            if(parseInt(end_arr)>=parseInt(start_arr))
            {}
            else
            {
                alert("搜索开始时间大于结束时间");
                return false;
            }
        }

        window.location.href="statistics.php?type=plus_state_source_statistics&startdate="+startdate+"&enddate="+enddate+"&team="+team;
        return false;
    }
    
    $(function(){
        $(".button").click(function(){
            var team = $(this).attr("data-attr"),
                startdate = $("#startdate").val(),
                enddate = $("#enddate").val();
            window.location.href="statistics.php?type=plus_state_source_statistics&startdate="+startdate+"&enddate="+enddate+"&team="+team;
        })  
    })
</script>
<table width="98%" border="0" align="center" cellspacing="0" cellpadding="0" style="padding-bottom:10px; ">
   <tr>
  <td>&nbsp;</td>
  </tr>
  <tr>
    <td align="center" bgcolor="#F2F2F2"><a style="font-size:14px;color:#F00;">订单来源/状态统计表</a></td>
  </tr>
</table>
<form action="statistics.php" method="GET" onsubmit="return check_time();">
<table width="98%"  border="0" align="center" cellpadding="0" style="margin-bottom:10px; " cellspacing="1" bgcolor="#E3E6EB">
    <tr>
        <td bgcolor="#FFFFFF" style="padding-left:10px;">
            统计日期: 
            <input id="startdate" name="startdate" type="text" value="2019-03-10" class="Wdate" onClick="WdatePicker({minDate:'2018-03-11',maxDate:'2019-03-10'})" readonly /> - 
            <input id="enddate" name="enddate" type="text" value="2019-03-10" class="Wdate" onClick="WdatePicker({minDate:'#F{$dp.$D(\'startdate\')}',maxDate:'2019-03-10'})" readonly />
        </td>
        <td colspan="2" height="35" bgcolor="#FFFFFF" style="padding-left:10px;">
            <input type="hidden" name="type" value="plus_state_source_statistics" />
            <input type="submit" name="submit" value="搜 索" />
        </td>
    </tr>
</table>
</form>
<div class="choose-team">
<div class="button type_0 current" data-attr="0">全部</div>
<div class="button type_1_2 " data-attr="1">一二期</div>
<!--<div class="button type_3 " data-attr="3">三期</div>-->
<div class="explain">该数据默认展示前一天的30天之内的数据，搜索限制时间是一年</div>
</div>

<table width="98%" border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="#89B270">
    <tr>
        <td width="" align="center" bgcolor="8DDA40" rowspan='2'>日期</td>
        <td width="" align="center" bgcolor="8DDA40" rowspan='2'>有效订单数</td>
        <td width="" align="center" bgcolor="8DDA40" colspan='10'>来源</td>
        <td width="" align="center" bgcolor="8DDA40" colspan='11'>审核状态</td>
        <td width="" align="center" bgcolor="8DDA40" rowspan='2'>无效订单</td>
    </tr>
    <tr>
        <td width="" align="center" bgcolor="8DDA40" >pc</td>
        <td width="" align="center" bgcolor="8DDA40" >app</td>
        <td width="" align="center" bgcolor="8DDA40" >3g</td>
        <td width="" align="center" bgcolor="8DDA40" >微信</td>
        <td width="" align="center" bgcolor="8DDA40" >呼叫中心</td>
        <td width="" align="center" bgcolor="8DDA40" >呼叫中心改约</td>
        <td width="" align="center" bgcolor="8DDA40" >超级APP</td>
        <td width="" align="center" bgcolor="8DDA40" >云健康</td>
        <td width="" align="center" bgcolor="8DDA40" >问医生</td>
        <td width="" align="center" bgcolor="8DDA40" >其它</td>
        <td width="" align="center" bgcolor="8DDA40" >待审核</td>
        <td width="" align="center" bgcolor="8DDA40" >审核前取消</td>
        <td width="" align="center" bgcolor="8DDA40" >审核后取消</td>
        <td width="" align="center" bgcolor="8DDA40" >审核通过</td>
        <td width="" align="center" bgcolor="8DDA40" >审核不通过</td>
        <td width="" align="center" bgcolor="8DDA40" >成功就诊</td>
        <td width="" align="center" bgcolor="8DDA40" >爽约</td>
        <td width="" align="center" bgcolor="8DDA40" >取消就诊</td>
        <td width="" align="center" bgcolor="8DDA40" >审核通过率</td>
        <td width="" align="center" bgcolor="8DDA40" >领取加号数</td>
        <td width="" align="center" bgcolor="8DDA40" >领取加号率</td>
    </tr>
            <tr>
        <td width="" align="center" bgcolor="FFFFFF" >2019-03-10</td>
        <td width="" align="center" bgcolor="FFFFFF" >71</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >26</td>
        <td width="" align="center" bgcolor="FFFFFF" >13</td>
        <td width="" align="center" bgcolor="FFFFFF" >1</td>
        <td width="" align="center" bgcolor="FFFFFF" >1</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >15</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >3</td>
        <td width="" align="center" bgcolor="FFFFFF" >12</td>
        <td width="" align="center" bgcolor="FFFFFF" >32</td>
        <td width="" align="center" bgcolor="FFFFFF" >4</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >32</td>
        <td width="" align="center" bgcolor="FFFFFF" >3</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >91.43%</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
        <td width="" align="center" bgcolor="FFFFFF" >0%</td>
        <td width="" align="center" bgcolor="FFFFFF" >0</td>
    </tr>
        <!--<tr>
        <td colspan="20" align="center" bgcolor="FFFFFF"></td>
    </tr>-->
    </table>



</body>
</html>
'''

elements = etree.HTML(req_text)
q_all = elements.xpath('/html/body/table[2]/tr[3]/td[2]/text()')[0]
q_pc = elements.xpath('/html/body/table[2]/tr[3]/td[3]/text()')[0]
q_app = elements.xpath('/html/body/table[2]/tr[3]/td[4]/text()')[0]
q_3g = elements.xpath('/html/body/table[2]/tr[3]/td[5]/text()')[0]
q_wx = elements.xpath('/html/body/table[2]/tr[3]/td[6]/text()')[0]
q_hujiao = elements.xpath('/html/body/table[2]/tr[3]/td[7]/text()')[0]
q_hujiao_gy = elements.xpath('/html/body/table[2]/tr[3]/td[8]/text()')[0]
q_xywyapp = elements.xpath('/html/body/table[2]/tr[3]/td[9]/text()')[0]
q_askapp = elements.xpath('/html/body/table[2]/tr[3]/td[11]/text()')[0]
q_others = elements.xpath('/html/body/table[2]/tr[3]/td[12]/text()')[0]

print(q_all)
print(q_pc)
print(q_app)
print(q_3g)
print(q_wx)
print(q_hujiao)
print(q_hujiao_gy)
print(q_xywyapp)
print(q_askapp)
print(q_others)
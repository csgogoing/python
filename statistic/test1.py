import re

a = '''HTTP/1.1 200 OK
Server: nginx
Date: Thu, 07 Mar 2019 09:38:41 GMT
Content-Type: text/html; charset=gb2312
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
XYWY_HEADER: admin01.node.kddi.op.xywy.com
Content-Length: 27420

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>患者电话咨询订单列表</title>
<link href="http://dhys.z.xywy.com/css/css.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="http://dhys.z.xywy.com/js/jquery-1.6.js"></script>
<script type="text/javascript" src="http://dhys.z.xywy.com/js/common.js"></script>
<link href="/js/My97DatePicker/skin/WdatePicker.css"/>
<script language="javascript" src="/js/My97DatePicker/WdatePicker.js"></script>
<script>
var adminurl = "http://dhys.z.xywy.com";
</script>

<!--退款弹出框JS_start-->
<script>
        var order_id;
        $(function(){
            function letDivCenter(divName){
    　　          var top = ($(window).height() - $(divName).height())/2;
    　　          var left = ($(window).width() - $(divName).width())/2;
    　　          var scrollTop = $(document).scrollTop();
    　　          var scrollLeft = $(document).scrollLeft();
    　　          $(divName).css( { position : 'absolute', 'top' : top + scrollTop, left : left + scrollLeft } ).show();
            } 
            $('.refund').click(function(){
                order_id = $(this).attr('order_id');
                letDivCenter('.refund-box');
            })
            $('.refund-cal').click(function(){
                $('.refund-box').hide();
                $('.refund-content').val('')
            })
            $('.refund-tru').click(function(){
                var refund_content = $('.refund-content').val();
                console.log(refund_content)
                if(!refund_content){
                    alert('请输入退款原因！');
                    return ;
                }
                
                //ajax
                $.ajax({
                    url:"/order.php?type=ajax_order_refund",
                    type:'post',
                    data: {
                          order_id:order_id,
                          remark:refund_content
                    },
                    dataType:'json',
                    success:function(json){
                        if(json.state == '10000'){//调取成功
                            $('.refund-content').val('')
                            $('.refund-box').hide();
                            letDivCenter('.refund-suss')
                            setTimeout(function(){$('.refund-suss').hide();},3000);
                            window.location.reload();
                        }
                        else{
                            alert(json.msg);
                        }
                    }

                });
        
                
            })
        })
    </script>
<!--退款js_end-->
<script>
    function outdata(){
        var url = window.location.href;
        if(url.indexOf("condition") > 0 && url.indexOf("outdata") == -1){
            var tmp = url.match(/condition=(\d){1}/),
                or_url="http://dhys.z.xywy.com/out_data.php?type=out_phone_order&condition="+tmp[1]+"&outdata=1";
                window.location.href=or_url;
        }else{
            var state=$("select[name=state]").val(),
                call_start=$("input[name=call_start]").val(),
                call_end=$("input[name=call_end]").val(),
                operator_id=$("select[name=operator_id]").val(),
                expert_name=$("input[name=expert_name]").val(),
                created_at_start=$("input[name=created_at_start]").val(),
                created_at_end=$("input[name=created_at_end]").val(),
                done_at_start=$("input[name=done_at_start]").val(),
                done_at_end=$("input[name=done_at_end]").val(),
                trade_type=$("select[name=trade_type]").val(),
                is_balance=$("select[name=is_balance]").val(),
                order_type=$("select[name=order_type]").val(),
                balance_start=$("input[name=balance_start]").val(),
                balance_end=$("input[name=balance_end]").val(),
                order_num=$("input[name=order_num]").val(),
                source=$("select[name=source]").val(),
                platform_source_pay=$("select[name=platform_source_pay]").val(),
                url="http://dhys.z.xywy.com/out_data.php?type=out_phone_order&state="+state+"&call_start="+call_start+"&call_end="+call_end+"&operator_id="+operator_id+"&expert_name="+expert_name+"&created_at_start="+created_at_start+"&created_at_end="+created_at_end+"&done_at_start="+done_at_start+"&done_at_end="+done_at_end+"&trade_type="+trade_type+"&is_balance="+is_balance+"&order_type="+order_type+"&balance_start="+balance_start+"&balance_end="+balance_end+"&order_num="+order_num+"&source="+source+"&platform_source_pay="+platform_source_pay+"&outdata=1&search=1";
            window.location.href=url;
        }
    }

    function change_hidden(){
        //var hidden_test = $('#hidden_test').val;//
        var hidden_test_val = $("input[type='checkbox']:checked").val();

        if(hidden_test_val == 'on'){
            $('#hidden_test_check').attr("checked");
            $('#hidden_test').val(1);
        }else{
            $('#hidden_test').val(0);//
            $('#hidden_test_check').removeAttr("checked");
        }

    }

    var show = new Array(); //限制展示条数

    function show_change_before_order(order_id,pid,flag,ch){
        if(!order_id){
            return false;
        }

        var tr_xb = 'tr_'+order_id;  //本条数据为改约的最后一条数据，其前有多个父关联订单
        var pr_xb = 'c_'+order_id;  //其本身前有多个父关联订单

        if(show[tr_xb] == undefined ){//原-子

        }else{
            return false;
        }
        var post_url = 'order.php?type=change_before_order_list';
        var html_str = '';
        $.ajax({
            url:post_url,
            type:'post',
            data:'order_id='+order_id,
            dataType:'json',
            success:function(json){
                if(json.status == '1'){//调取成功
                    var arr = json.data ;
                    //显示关联订单
                    loop_arr_to_show_order(arr,order_id,pid,flag,ch);

                }
                else{
                    //调取失败
                }
            }

        });
    }


    function loop_arr_to_show_order(arr,order_id,pid,flag,ch){
        if(!arr) {
            return false;
        }

        var html_str = '';
        var html_str2 = '';


        $(arr).each(function(k,v){
            // $(v).each(function(kk,vv){
                $(v).each(function(kkk,vvv){
                    var key_arr = new Array();
                    key_arr = vvv;

                    var tr_xb = 'tr_'+order_id;
                    var pr_xb = 'c_'+order_id;

                    if(show[tr_xb] == undefined){
                        if(flag == 1 && $("#c_"+key_arr.id).length <=0 ){
                            html_str = get_html(key_arr,0);
                            $("#tr_"+order_id).after(html_str);
                            show[tr_xb] = 'true'; //1

                        }else{
                            html_str = get_html(key_arr,0);
                            $("#c_"+order_id).after(html_str);
                            show[tr_xb] = 'true'; //1
                        }

                    }else{
                        if($("#c_"+key_arr.id).length <=0  ){
                            html_str = get_html(key_arr,0);
                            $("#c_"+order_id).after(html_str);
                            show[pr_xb] = 'true';
                        }

                    }
                    html_str = '';

                });

            });
        //})
    }

    function get_html(arr,ch_num){
        var vvv = new Array();
        html_str = '';

        vvv = arr;

        if(ch_num == 1){
            html_str += '<TR oid = "'+vvv.id+'" id="ch_'+vvv.id+'" >';
        }else{
            html_str += '<TR oid = "'+vvv.id+'" id="c_'+vvv.id+'" >';
        }

        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.state == 1){
            html_str += '<input type="checkbox" value="'+vvv.id+'" name="selectid[]">';
        }

        html_str += '</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.id+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.order_num+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.expert_name+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.hosname+''+vvv.depname+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.fee+'</TD>';

        html_str += '<TD bgcolor="00CCFF">'+vvv.realname+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.created_at+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.state_cn+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.confirm_start+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.order_done_at+'</TD>';
        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.source == '3gzf'){
            html_str += '3G支付宝';
        }else if(vvv.source == 'yyfztj'){
            html_str += '预约分诊推荐';
        }else{
            html_str += vvv.source;
        }
        html_str += '</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.platform_source_pay+'</TD>';
        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.pay_state_cn == '未支付'){
            html_str += '<font color="red">'+vvv.pay_state_cn+'</font>';
        }else if(vvv.pay_state_cn == '已支付'){
            html_str += '<font color="green">'+vvv.pay_state_cn+'</font>';
        }else if(vvv.pay_state_cn == '已退款'){
            html_str += vvv.pay_state_cn;
        }else if(vvv.pay_state_cn == '已变更'){
            html_str += vvv.pay_state_cn;
        }
        html_str += '</TD>';

        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.trade_type == 1){
            html_str += '支付宝';
        }else if(vvv.trade_type == 2){
            html_str += '银联云闪付';
        }else if(vvv.trade_type == 3){
            html_str += '中国银联';
        }else if(vvv.trade_type == 4){
            html_str += '微信支付';
        }else if(vvv.trade_type == 5){
            html_str += '线下支付';
        }else if(vvv.trade_type == 6){
            html_str += '<font color="red">VIP卡支付</font>';
        }
        html_str += '</TD>';

        html_str += '<TD bgcolor="00CCFF">'+vvv.trade_no+'</TD>';
        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.is_balance == 2){
            html_str += '成功';
        }else if(vvv.is_balance == 3){
            html_str += '失败';
        }
        html_str += '</TD>';

        html_str += '<TD bgcolor="00CCFF">';
        if(vvv.balance_time){
            html_str += vvv.balance_time;
        }
        html_str += '</TD>';


        html_str += '<TD bgcolor="00CCFF">'+vvv.operation_remark+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.operation_operated_at+'</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.operation_operator+'</TD>';
        html_str += '<TD bgcolor="00CCFF">';
        //if(vvv.is_locking == 0){
            //if(vvv.state == 16){
                html_str += '<a href="order.php?type=change_before_order_detail&id='+vvv.id+'" target="_blank">查看</a>';
            /* }else{
                html_str += '<a href="order.php?type=order_detail&id='+vvv.id+'" >审核</a>';
            } */

        /* }else{
            html_str += '<span style="color:#999;">审核</span>';
        } */

        if(vvv.related_order != 0){
            if(ch_num == 1){
                html_str += '&nbsp;&nbsp;<a href="javascript:void(0)" style="cursor:pointer" onclick="show_change_before_order('+vvv.id+','+vvv.related_order+',0,1)" >改前订单</a>';

            }else{
                html_str += '&nbsp;&nbsp;<a href="javascript:void(0)" style="cursor:pointer" onclick="show_change_before_order('+vvv.id+','+vvv.related_order+',0,0)" >改前订单</a>';

            }
            //html_str +=   '&nbsp;&nbsp;<a href="javascript:void(0)" style="cursor:pointer" onclick="show_change_before_order('+vvv.id+','+vvv.related_order+',0)" >改前订单</a>';
        }
        html_str += '</TD>';
        html_str += '<TD bgcolor="00CCFF">'+vvv.lock_owner+'</TD>';
        html_str += '<input type="hidden" id="hi_"'+vvv.id+' value="true"> ';
        html_str += '</TR>';
        return html_str;
    }


</script>
</head>
<body>
<!--退款弹框start-->
    <style>
    /**{margin: 0;padding: 0}*/
        .refund-box{
            display: none;
            position: absolute;
            width: 438px;
            height: 224px;
            border: 1px solid #eee;
            background: #fff;
            z-index: 10000;
        }
        .refund-box-top{
            height: 45px;
            text-align: center;
            line-height: 45px;
            font-size: 16px;
            background-color: #fafafa;
            border-bottom: 1px solid #eee;
        }
        .refund-content{
            display: block;
            width: 388px;
            height: 68px;
            padding: 5px;
            margin: 20px auto 0;
            resize: none;
            outline: none;
            border: 1px solid #eee;
        }
        .refund-btn-area{
            text-align: center;

        }
        .refund-btn{
            display: inline-block;
            width: 118px;
            height: 38px;
            margin: 10px;
            border: 1px solid #86cd48;
            font-size: 16px;
            text-align: center;
            line-height: 38px;
            border-radius: 3px;
            cursor: pointer;
        }
        .refund-cal{
            color: #86cd48;
        }
        .refund-tru{
            color: #fff;
            background: #86cd48;
        }
        .refund-suss{
            display: none;
            position: absolute;
            width: 150px;
            height: 80px;
            border: 1px solid #eee;
            text-align: center;
            line-height: 80px;
            font-size: 18px;
            background-color: #86cd48;
            z-index: 100001;
        }
    </style>
    <div class="refund-box">
        <p class="refund-box-top">退款申请</p>
        <textarea class="refund-content" placeholder="请输入退款原因，最多填写100个字。（必填）" maxlength="100" required="required"></textarea>
        <div class="refund-btn-area" "><span class="refund-btn refund-cal">取消</span>
        <span class="refund-btn refund-tru">确定</span></div>
    </div>
    <p class="refund-suss">提交成功!</p>
<!--退款弹框end-->
<table width="98%" border="0" align="center" cellspacing="0" cellpadding="0" style="padding-bottom:10px; ">
   <tr>
  <td>&nbsp;</td>
  </tr>
  <tr>
    <td width="50%" align="center" bgcolor="#F2F2F2"><a style="font-size:14px;color:#F00;">电话咨询订单列表</a></td>
  </tr>
</table>

<form action="order.php?type=order_list" method="get">
<table width="98%" bgcolor="#E3E6EB" border="0" align="center" cellpadding="0" cellspacing="1">
    <input name = "type" value= "order_list" type = "hidden"></input>
    <input name ="hidden_test" id="hidden_test" value= "1" type = "hidden"/>
     <tr>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            订单状态：
            <select name="state">
                <option value="0">全部</option>
                                <option value="1" >未支付</option>
                                <option value="2" >支付处理中</option>
                                <option value="3" >待确定时间</option>
                                <option value="4" >待通话</option>
                                <option value="5" >通话完成</option>
                                <option value="6" >订单取消</option>
                                <option value="7" >已退款</option>
                                <option value="8" >订单完成</option>
                                <option value="9" >订单失效</option>
                                <option value="16" >订单变更</option>
                                <option value="17" >待填写信息</option>
                                <option value="18" >退款待审核</option>
                                <option value="19" >退款被驳回</option>
                            </select>
            支付状态：
            <select name="pay_state">
                <option value="0">全部</option>
                                <option value="1" >未支付</option>
                                <option value="2" >已支付</option>
                                <option value="3" >已退款</option>
                                <option value="4" >已变更</option>
                                <option value="5" >已打回</option>
                            </select>
        </td>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            通话时间：
            <input name="call_start" value="" type="text" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />至<input name="call_end" type="text" value="" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />
        </td>
        <td height="35" width="20%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            咨询的专家：<input type="text" name="expert_name" size="8" value="" />
         </td>
         <td height="35" width="20%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            占用人：
            <select name="operator_id">
                <option value="0">全部</option>
                                <option value="13" >门总</option>
                                <option value="72" >江源溪</option>
                                <option value="80" >张文悦</option>
                                <option value="82" >管富国</option>
                                <option value="107" >caimingchao</option>
                                <option value="122" >郝苑君</option>
                                <option value="124" >温丽利</option>
                                <option value="141" >商盼盼</option>
                                <option value="180" >付艳秋</option>
                                <option value="187" >李秀文</option>
                                <option value="189" >张红梅</option>
                                <option value="190" >姚远</option>
                                <option value="194" >戴慧</option>
                                <option value="197" >杜军</option>
                                <option value="199" >王倩倩</option>
                                <option value="200" >刘伟</option>
                                <option value="207" >张萌</option>
                                <option value="209" >刘盼盼</option>
                                <option value="210" >赵钰博</option>
                                <option value="212" >赵明明</option>
                                <option value="213" >植宇</option>
                                <option value="214" >闫金东</option>
                                <option value="215" >苏楠楠</option>
                                <option value="217" >刘娜</option>
                                <option value="219" >刘娜</option>
                                <option value="220" >杜春雪</option>
                                <option value="221" >郝晓丽</option>
                                <option value="225" >周慧敏</option>
                                <option value="227" >zhouxuejian</option>
                                <option value="229" >王佳丽</option>
                            </select>
         </td>
    </tr>

    <tr>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            提交时间: <input name="created_at_start" value="2015-03-03" type="text" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />至<input name="created_at_end" type="text" value="2015-03-03" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />
        </td>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
             <a href="order.php?type=order_list&condition=2" style="color:#f00;">最近待确定时间订单</a>
            <!-- 需要在10分钟内建立通话：
            <select name="ten_mins">
                <option value="0">全部</option>
                <option value="1" >是</option>
                <option value="2" >否</option>
            </select> -->
        </td>

        <td colspan="2" height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
             订单完成时间：<input name="done_at_start" value="" type="text" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />至<input name="done_at_end" type="text" value="" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />
        </td>
    </tr>
    <input type="hidden" name="search" value="1"/>
     <tr>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">支付方式：
            <select name = "trade_type">
                <option value="0">请选择</option>
                <option value="1" >支付宝</option>
                <option value="2" >银联云闪付</option>
                <option value="3" >中国银联</option>
                <option value="4" >微信支付</option>
                <option value="5" >线下支付</option>
                <option value="6" >VIP卡支付</option>
                <option value="7" >企业支付</option>
                <option value="8" >闻康支付</option>


            </select>
            &nbsp;
            对账：
            <select name = "is_balance">
                <option value="0">请选择</option>
                <option value="1" >未对账</option>
                <option value="2" >对账成功</option>
                <option value="3" >对账失败</option>
            </select>
        </td>
        <td bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            <select name = "order_type">
                <option value="0">请选择</option>
                <option value="0" selected>不限</option>
                <option value="1" >正常订单</option>
                <option value="2" >描述无关且无支付意向</option>
                <option value="3" >无法联系到患者</option>
                <option value="4" >重复订单</option>
                <option value="5" >测试订单</option>
                <option value="10" >其它原因</option>
            </select>
        </td>

        <td colspan="2" width="40%" height="35" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
        对账时间：
        <input name="balance_start" value="" type="text" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />至<input name="balance_end" type="text" value="" onClick="WdatePicker({maxDate:'%y-%M-#{%d}'})" size="10" readonly />
        </td>
    </tr>
    <tr>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
                订单号：<input type="text" name="order_num" value="" />
                订单：<select name='is_dhysfz'>
                            <option>全部</option>
                            <option  value='1'>普通订单</option>
                            <option  value='2'>复诊订单</option>
                        </select>
        </td>
        <td height="35" width="30%" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
          <a href="order.php?type=order_list&condition=1" style="color:#6F6FFF;">最近待通话订单</a>
            订单来源：
          <select name="source">
            <option value="0">请选择</option>
            <option value="1" >pc</option>
            <option value="2" >3g</option>
            <option value="3" >app</option>
            <option value="4" >3g支付宝</option>
             <option value="5" >预约分诊推荐</option>
             <option value="6" >三星</option>
             <option value="7" >互联网医院</option>
             <option value="8" >问医生APP</option>
             <option value="9" >寻医问药APP</option>
             <option value="10" >new寻医问药APP</option>
             <option value="11" >寻医问药APP综合</option>
             <option value="12" >微信公众号</option>
             <option value="13" >医拉患</option>
             <option value="14" >百度熊掌号</option>
             <option value="15" >淘新闻</option>
              <option value="16" >vivo全局搜</option>
              <option value="17" >今日头条</option>
              <option value="18" >搜狗</option>
          </select>
          &nbsp;&nbsp;
        </td>
        <td width="40%" colspan="2" bgcolor="#FFFFFF" style="text-align:left; padding-left:10px;">
            支付来源：
              <select name="platform_source_pay">
                <option value="0">请选择</option>
                <option value="1" >pc</option>
                <option value="2" selected>wap</option>
                <option value="3" >app</option>
                <option value="4" >微信公众号</option>
                <option value="5" >线下支付</option>
              </select>
              &nbsp;
              隐藏测试订单 <input type="checkbox"  id="hidden_test_check" name="hidden_test_check" checked="checked" onclick="change_hidden()" />
            <input type="submit"   value=" 搜  索  " name="submit" style="height: 45px; width: 145px; font-size: 18px; cursor:pointer;" />
        </td>
    </tr>
</table>

</form>
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr height="20" bgcolor="#F2F2F2" >
    <td align="center"></td>
    <td align="left" ></td>
  </tr>
</table>


 <form id="formselect" name="formselect" method="post" action="/order.php?type=fail_order" onsubmit="return doall(this,'selectid[]',1);">
<table width="98%" border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="#89B270">
    <tr>
        <td width="1%" align="center" bgcolor="8DDA40">选择</td>
        <td width="3%" align="center" bgcolor="8DDA40">ID</td>
        <td width="5%" align="center" bgcolor="8DDA40">订单号</td>
        <td width="2%" align="center" bgcolor="8DDA40">咨询专家</td>
        <td width="6%" align="center" bgcolor="8DDA40">医院科室</td>
        <td width="3%" align="center" bgcolor="8DDA40">服务费用</td>
        <td width="2%" align="center" bgcolor="8DDA40">患者姓名</td>
        <td width="7%" align="center" bgcolor="8DDA40">订单提交时间</td>
        <td width="4%" align="center" bgcolor="8DDA40">订单状态</td>
        <td width="7%" align="center" bgcolor="8DDA40">通话时间</td>
        <td width="7%" align="center" bgcolor="8DDA40">订单完成时间</td>
        <td width="2%" align="center" bgcolor="8DDA40">订单来源</td>
        <td width="2%" align="center" bgcolor="8DDA40">支付来源</td>
        <td width="2%" align="center" bgcolor="8DDA40">支付状态</td>
        <td width="2%" align="center" bgcolor="8DDA40">支付方式</td>
        <td width="7%" align="center" bgcolor="8DDA40">流水号</td>
        <td width="3%" align="center" bgcolor="8DDA40">对账</td>
        <td width="7%" align="center" bgcolor="8DDA40">对账时间</td>
        <td width="7%" align="center" bgcolor="8DDA40">最新备注</td>
        <td width="7%" align="center" bgcolor="8DDA40">备注时间</td>
        <td width="2%" align="center" bgcolor="8DDA40">备注人</td>
        <td width="4%" align="center" bgcolor="8DDA40">操作</td>
        <td width="2%" align="center" bgcolor="8DDA40">占用人</td>
    </tr>

       <tr bgcolor="ffffff">
        <td colspan=10 style="text-align:center;">暂无数据 </td>
    </tr>
   </table>
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td align="center">
        <input type="checkbox" name="selectall" onclick="selall(this.checked,'selectid[]');" id="selectall">&nbsp; 全选&nbsp;
        <input id="act" type="radio" name="act" value="fail">失效
        <input type="submit" value="处理" name="submitfail">
    </td>
  </tr>
</table>
</form>
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>&nbsp;</td>
  </tr>
</table>

<table width="98%" border="0"  cellpadding="0" cellspacing="0" align="center">
  <tr height="20" bgcolor="#F2F2F2" >
    <td align="center"></td>
    <td align="left"></td>
  </tr>
</table>
<!-- 要处理的订单 S -->
<div class="" style="float:right;font-size:12px;width:300px;border:1px solid #b8caf6;margin-right:10px;">
  <div style="padding:10px;background-color: #B8CAF6;color: #4D4D4D;"><strong>10分钟内需要建立通话会议订单</strong></div>
  <ul id="wait_meeting_list" style="list-style:none;">
        <li style="margin-left:-30px;padding:5px 0;">Z14103112881&nbsp;&nbsp;2014-12-02 20:30:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=3623" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15010950490&nbsp;&nbsp;2015-01-09 17:15:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=4349" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15020628590&nbsp;&nbsp;2015-04-16 15:26:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=5411" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15030276297&nbsp;&nbsp;2015-03-09 14:16:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=5635" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15041615525&nbsp;&nbsp;2015-04-30 11:29:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=6801" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15041675686&nbsp;&nbsp;2015-04-16 16:17:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=6811" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15050456750&nbsp;&nbsp;2015-06-04 11:27:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=7031" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15051382137&nbsp;&nbsp;2015-05-15 16:37:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=7122" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15052521554&nbsp;&nbsp;2015-06-05 11:20:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=7298" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;">Z15060372739&nbsp;&nbsp;2015-06-05 15:36:00&nbsp;&nbsp;<a href="order.php?type=order_detail&id=7436" target="_blank">审核</a></li>
        <li style="margin-left:-30px;padding:5px 0;text-align:center;"><a href="order.php?type=order_list&state=4&ten_mins=1&search=1">查看全部</a>&nbsp;&nbsp;</li>
  </ul>
</div>
<!-- 要处理的订单 E -->
</body>
</html>
'''
total_num = re.findall(r'总计: (.*)条', a)
pay_num = re.findall(r'已付款订单量：(\d*) &nbsp', a)
pay_amount = re.findall(r'已付款总金额：(\d+\.\d+)', a)

print(total_num)
print(pay_num)
print(pay_amount)
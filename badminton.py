# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

## URL
AVAILABLE_COURT = 'http://web.szosc.cn/index.php/wxplace/place/index/salevenue/%E8%8B%8F%E5%B7%9E%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E4%BD%93%E8%82%B2%E4%B8%AD%E5%BF%83/fieldtype/%E7%BE%BD%E6%AF%9B%E7%90%83A%E5%8C%BA/cgxx/%E4%BD%93%E8%82%B2%E5%9C%BA%E5%81%A5%E8%BA%AB%E4%B8%AD%E5%BF%83'
CREATE_ORDER = 'http://web.szosc.cn/index.php/wxplace/place/pay'
SUBMIT_ORDER = 'http://web.szosc.cn/index.php/yinlian/index/pay'

## Cookies
PHPSESSID = 'ugaroeb0umt7ufa7513eelija6'

## Headers
UA = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'

## Order infos
DATE = '2019-05-15'  ## Every Tuesday
PRICE = '55.00'
FIELTYPE = '羽毛球A区'
LIMIT = '1.000'
HOMENAME = '苏州奥林匹克体育中心'

## Personal infos
BOOKHOLDER = '叶子木'
MOBILE = '15170123456'
OPENID = 'osfFy0tch3WmLnoNJpUNIlJSyVQ0' ## Personal Key
UNIONID = 'o3eng1FtJFC0ozvsZpuCX0Ls0TE0' ## Personal Key

def getAvailableCourt():
    response = requests.get(AVAILABLE_COURT,
                        headers = {'User-Agent': UA},
                        cookies = {'PHPSESSID' : PHPSESSID})
    print response.content
    ## Parse tables, but too complex...

def createOrder(field):
    response = requests.post(CREATE_ORDER,
                        headers = {'User-Agent': UA},
                        cookies = {'PHPSESSID' : PHPSESSID},
                        data = {'price' : PRICE,
                                'field' : field,
                                'fieldtype' : FIELTYPE,
                                'openid' : OPENID,
                                'unionid' : UNIONID,
                                'homename' : HOMENAME,
                                'limit' : LIMIT})
    soup = BeautifulSoup(response.content, "html.parser")
    print '======= Create order successfully... ======='
    print '======= OrderInfos ======='
    orderInfos = soup.find_all(attrs={"type" : "hidden"})
    outtradeno = ''
    bookinfo = ''
    fieldtype = ''
    ordtotal_fee = ''
    fieldnum = ''
    starttime = ''
    paid = ''
    for item in orderInfos:
        name = item['name']
        value = item['value']
        print name + " : " + value
        if name == "outtradeno":
            outtradeno = value
        elif name == "bookinfo":
            bookinfo = value
        elif name == "fieldtype":
            fieldtype = value
        elif name == "ordtotal_fee":
            ordtotal_fee = value
        elif name == "fieldnum":
            fieldnum = value
        elif name == "starttime":
            starttime = value
        elif name == "paid":
            paid = value
    if outtradeno == '':
        print '======= This court had been booked... ======='
    else:
        print '======= Start submit order... ======='
        submitOrder(outtradeno, ordtotal_fee, fieldtype, fieldnum, starttime, paid, bookinfo)

def submitOrder(tradeno, ordtotal_fee, fieldtype, fieldnum, starttime, paid, bookinfo):
    response = requests.post(SUBMIT_ORDER,
                        headers = {'User-Agent': UA},
                        cookies = {'PHPSESSID' : PHPSESSID},
                        data = {'bookholder' : BOOKHOLDER,
                                'mobile' : MOBILE,
                                'outtradeno' : tradeno,
                                'ordtotal_fee' : ordtotal_fee,
                                'homename' : HOMENAME,
                                'fieldtype' : fieldtype,
                                'fieldnum' : fieldnum,
                                'starttime' : starttime,
                                'bookinfo' : bookinfo,
                                'paid' : paid,
                                'wxopenid' : OPENID,
                                'unionid' : UNIONID,
                                'limit' : LIMIT})
    if response.content.find('确认支付') > 0:
        print '======= Submit successfully! please pay on you phone ======='
    else:
        print '======= Submit Failed! try other courts?======='

def main():
    # getAvailableCourt()
    field5_1 = '19:00-20:00|' + DATE + ' 19:00:00|5|55'
    field5_2 = '20:00-21:00|' + DATE + ' 20:00:00|5|55'

    field6_1 = '19:00-20:00|' + DATE + ' 19:00:00|6|55'
    field6_2 = '20:00-21:00|' + DATE + ' 20:00:00|6|55'

    # createOrder(field5_1)
    # createOrder(field5_2)
    # createOrder(field6_1)
    createOrder(field6_2)

main()


# ==================== Create order request =========================
# Request URL: http://web.szosc.cn/index.php/wxplace/place/pay
# Request Method: POST
# Status Code: 200 OK
# Remote Address: 218.4.252.149:80
# Referrer Policy: no-referrer-when-downgrade
# Cache-Control: private
# Connection: Keep-Alive
# Content-Type: text/html; charset=utf-8
# Date: Tue, 07 May 2019 04:02:16 GMT
# Expires: Thu, 19 Nov 1981 08:52:00 GMT
# Keep-Alive: timeout=5, max=100
# Pragma: no-cache
# Server: Apache/2.4.23 (Win32) OpenSSL/1.0.2j PHP/5.4.45
# Transfer-Encoding: chunked
# X-Powered-By: ThinkPHP

## Request headers
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,la;q=0.5,ja;q=0.4
# Cache-Control: max-age=0
# Connection: keep-alive
# Content-Length: 302
# Content-Type: application/x-www-form-urlencoded
# Cookie: PHPSESSID=ugaroeb0umt7ufa7513eelija6
# Host: web.szosc.cn
# Origin: http://web.szosc.cn
# Referer: http://web.szosc.cn/index.php/wxplace/place/index/salevenue/%E8%8B%8F%E5%B7%9E%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E4%BD%93%E8%82%B2%E4%B8%AD%E5%BF%83/fieldtype/%E7%BE%BD%E6%AF%9B%E7%90%83A%E5%8C%BA/cgxx/%E4%BD%93%E8%82%B2%E5%9C%BA%E5%81%A5%E8%BA%AB%E4%B8%AD%E5%BF%83
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36

## Form
# price: 30.00
# fieldtype: 羽毛球A区
# homename: 苏州奥林匹克体育中心
# field: 17:00-18:00|2019-05-07 17:00:00|2|30
# openid: osfFy0tch3WmLnoNJpUNIlJSyVQ0
# unionid: o3eng1FtJFC0ozvsZpuCX0Ls0TE0
# limit: 1.0000


## ====================== Submit order request ======================
# Request URL: http://web.szosc.cn/index.php/yinlian/index/pay
# Request Method: POST
# Status Code: 200 OK
# Remote Address: 218.4.252.149:80
# Referrer Policy: no-referrer-when-downgrade
# Cache-Control: private
# Connection: Keep-Alive
# Content-Length: 5508
# Content-Type: text/html; charset=utf-8
# Date: Tue, 07 May 2019 06:39:32 GMT
# Expires: Thu, 19 Nov 1981 08:52:00 GMT
# Keep-Alive: timeout=5, max=100
# Pragma: no-cache
# Server: Apache/2.4.23 (Win32) OpenSSL/1.0.2j PHP/5.4.45
# X-Powered-By: ThinkPHP
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,la;q=0.5,ja;q=0.4
# Cache-Control: max-age=0
# Connection: keep-alive
# Content-Length: 488
# Content-Type: application/x-www-form-urlencoded
# Cookie: PHPSESSID=ugaroeb0umt7ufa7513eelija6
# Host: web.szosc.cn
# Origin: http://web.szosc.cn
# Referer: http://web.szosc.cn/index.php/wxplace/place/pay
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36

# Forms
# bookholder: 叶志彬
# mobile: 15170777774
# idno:
# outtradeno: 4076SP9E222019050711148
# ordtotal_fee: 55.00
# homename: 苏州奥林匹克体育中心
# fieldtype: 羽毛球A区
# wxopenid: osfFy0tch3WmLnoNJpUNIlJSyVQ0
# unionid: o3eng1FtJFC0ozvsZpuCX0Ls0TE0
# fieldnum: 16号
# starttime: 2019-05-11 18:00:00,
# bookinfo: 18:00-19:00|2019-05-11 18:00:00|16|55
# uid:
# paid: 55.00
# limit: 1.0000



## =========== Create order html plain text =============
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>场地预定</title>
# 	<meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
#     <script type="text/javascript" src="/Public/static/jquery-2.0.3.min.js"></script>
#     <script type="text/javascript" src="/Public/Wxplace/js/jquery.mousewheel.js"></script>
# 	<link href="/Public/static/theme.min.css" rel="stylesheet">
# <style>
#  #settype{
#     width:100%;
#   }
#   .userdiv{
# 	width:100%;
#   }
#   .user2{
# 	margin:0 auto;
# 	width:98%;
#     margin-top:0px;
#   }
#   #btnn{
#     margin-top: 20px;
#   }
#   .chooseman{
#
#   }
#   .addman{
#   margin-top:-19px;
#   background-color:#fff;
#   cursor: pointer;
#   color:#46a3ff;
#   line-height:40px;
#   height:40px;
#   width:100%;
#   text-align:center;
#   font-size:20px;
#   border-top:1px solid #e0e0e0;
#   }
#   .choose{
#  width:80px;height:30px;background-color:#2290F9; color:#fff;text-align:center;line-height:30px;
#  border-radius:0.5em;font-size:12px;
#   }
#   .nochoose{
#  width:80px;height:30px;background-color:#e0e0e0; color:#fff;text-align:center;line-height:30px;
#  border-radius:0.5em;font-size:12px;
#   }
# </style>
# </head>
# <body style="background-color:#fff">
#
# <div id="settype">
# <!--订单信息-->
# <form action="/index.php/yinlian/index/pay" method="post">
# <div class="order">
# 	<table style="width:100%">
# 		<tr style="background-color:#f0f0f0;font-size:16px;height:40px;"><td colspan="3">订场信息：</td></tr>
# 		<tr style="border-bottom:1px solid #e0e0e0;height:30px;">
# 			<td style="width:60px;color:#46a3ff" align="right">场&nbsp;&nbsp;&nbsp;&nbsp;馆：</td>
# 			<td colspan="2">苏州奥林匹克体育中心</td>
# 		</tr>
# 		<tr style="border-bottom:1px solid #e0e0e0;height:30px;">
# 			<td style="width:60px;color:#46a3ff" align="right">项&nbsp;&nbsp;&nbsp;&nbsp;目：</td>
# 			<td colspan="2">羽毛球A区</td>
# 		</tr>
# 		<tr>
# 			<td style="width:60px;color:#46a3ff" align="right">场&nbsp;&nbsp;&nbsp;&nbsp;地：</td>
# 			<td colspan="2">
# 				16号场&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2019-05-11&nbsp;18:00-19:00			</td>
# 		</tr>
# 				<tr style="border-top:1px solid #e0e0e0;height:30px;">
# 			<td style="width:60px;color:#46a3ff" align="right">价&nbsp;&nbsp;&nbsp;&nbsp;格：</td>
# 			<td colspan="2" style="color:#fd5a28">&yen;55.00</td>
# 		</tr>
# 		<tr style="border-top:1px solid #e0e0e0;height:30px;">
# 			<td style="width:60px;color:#46a3ff" align="right">提&nbsp;&nbsp;&nbsp;&nbsp;示：</td>
# 			<td colspan="2" style="width:60px;color:red;" align="left">入场前72个小时内不可退票</td>
# 		</tr>
# 		<tr style="background-color:#f0f0f0;font-size:16px;height:40px;"><td colspan="3">用户信息：</td></tr>
# 		<tr style="border-bottom:1px solid #e0e0e0">
# 			<td align="right" style="width:60px;color:#46a3ff">订场人：</td>
# 			<td><input type="text" name="bookholder" placeholder="2-4汉字" style="height:20px;width:150px;border:0px;background-color:#fff" value="" /></td>
# 			<td align="right"><div class="showman" style="width:80px;height:30px;background-color:#2290F9; color:#fff;text-align:center;line-height:30px;  border-radius:0.5em;font-size:12px;">修改</div></td>
# 		</tr>
# 		<tr>
# 			<td></td>
# 			<td> <span name="error2"></span></td>
# 		</tr>
# 		<tr style="border-bottom:1px solid #e0e0e0">
# 			<td align="right" style="color:#46a3ff">手机号：</td>
# 			<td><input type="text" name="mobile" placeholder="11位手机号" style="height:20px;width:150px;border:0px;background-color:#fff" value="" /></td>
# 			<td></td>
# 		</tr/>
# 	    <tr>
# 			<td></td>
# 			<td> <span name="error1"></span></td>
# 		</tr>
# 		<tr style="border-bottom:1px solid #e0e0e0">
# 			<td align="right" style="color:#46a3ff">身份证：</td>
# 			<td><input type="text" name="idno" placeholder="可以为空" style="height:20px;width:150px;border:0px;background-color:#fff" value="" />
# 			</td>
# 			<td></td>
# 		</tr>
# 	    <tr>
# 			<td></td>
# 			<td> <span name="error3"></span></td>
# 		</tr>
# 		<!--tr style="border-bottom:1px solid #e0e0e0;height:30px;">
# 			<td style="width:60px;color:#46a3ff" align="right">支&nbsp;&nbsp;&nbsp;&nbsp;付：</td>
# 			<td colspan="2">
# 				<select name="pays" style="width:100%;height:30px;background-color:#2290f9;color:#fff"/>
# 					<option value="微信支付">微信支付</option>
# 					<option value="会员卡">会员卡</option>
# 				</select>
# 			</td>
# 		</tr-->
#
# 		<tr style="border-bottom:1px solid #e0e0e0;height:30px;" class="aa">
# 			<td rowspan="2" style="width:60px;color:#46a3ff" align="right">支&nbsp;&nbsp;&nbsp;&nbsp;付：</td>
# 			<td><img src="/Uploads/Picture/images/weixinpay.jpg" width="40px" height="40px"/>微信支付</td>
# 			<td align="right"><div class="choose" value="微信">已选</div></td>
# 		</tr>
# 		<!--tr style="border-bottom:1px solid #e0e0e0;height:30px;" class="aa">
# 			<td style="height:40px"><img src="/Uploads/Picture/images/会员卡支付.png" width="25px" height="25px" style="margin-left:7px;margin-right:6px;"/>会员卡支付</td>
# 			<td align="right"><div class="nochoose" value="会员卡">启用</div></td>
# 		</tr-->
#
#
# 		<tr style="display:none" class="huiyuanka">
# 			<td></td>
# 			<td colspan='2'>
#
#
# 			</td>
# 		</tr>
# 	</table>
# </div>
# <div style="width:100%">
#   <input type="hidden" name="outtradeno" value="4076SP610E2019050709585" />
#   <input type="hidden" name="ordtotal_fee" value="55.00" />
#   <input type="hidden" name="homename" value="苏州奥林匹克体育中心" />
#   <input type="hidden" name="fieldtype" value="羽毛球A区" />
#   <input type="hidden" name="wxopenid" value="osfFy0tch3WmLnoNJpUNIlJSyVQ0" />
#   <input type="hidden" name="unionid" value="o3eng1FtJFC0ozvsZpuCX0Ls0TE0" />
#   <input type="hidden" name="fieldnum" value="16号" />
#   <input type="hidden" name="starttime" value="2019-05-11 18:00:00," />
#   <input type="hidden" name="bookinfo" value="18:00-19:00|2019-05-11 18:00:00|16|55"/>
#   <input type="hidden" name="uid" value=""/>
#   <input type="hidden" name="paid" value="55.00" />
#   <input type="hidden" name="limit" value="1.000"/>
#
#   <button type="submit" style="width:98%; height:40px;background-color:#2290F9; border:0px #2290F9 solid; cursor: pointer;  color:white; font-size:12px;margin-left:1%; border-radius:0.5em;"  id="btnn">确认订单</button>
# </div>
# </form>
# </div>
# <script type="text/javascript">
# $('#btnn').click(function(){
# var tel = $('input[name=mobile]').val();
# var reg = /^0?1[2|3|4|5|6|7|8|9][0-9]\d{8}$/;
# if(!reg.test(tel)){
#   $('span[name=error1]').css({"color":"red"});
#   $('span[name=error1]').text('手机号为空或格式不对');
#   return false;
# }
#  var name = $.trim($('input[name=bookholder]').val());
#  var regname = /^[\u4e00-\u9fa5]{2,4}$/;
#  if(!regname.test(name)){
#     $('span[name=error2]').css({"color":"red"});
#     $('span[name=error2]').text('姓名为2到4个汉字');
#     return false;
#   }
# if($('input[name=bookholder]').val()==''){
#   $('span[name=error2]').css({"color":"red"});
#   $('span[name=error2]').text('姓名不能为空');
#   return false;
# }
# /*if($('input[name=IdNo]').val()==''){
#   $('span[name=error3]').css({"color":"red"});
#   $('span[name=error3]').text('证件号不能为空');
#   return false;
# }*/
# var regID = /(^\d{15}$)|(^\d{17}(\d|X)$)|(^\d{10}\*\*\*\*\d{3}(\d|X)$)|(^\d{10}\*\*\*\*\d$)/;
# if($('input[name=idno]').val()==''){
#   return true;
# }
# else if(!regID.test($('input[name=idno]').val())){
#   $('span[name=error3]').css({"color":"red"});
#   $('span[name=error3]').text('证件号格式不对');
#    return false;
# }
# else{
# 	return true;
# }
# });
# //对齐样式设置
# $('#settype input[type=text]').css({"vertical-align":"middle","margin-top":"12px"});
# $('#settype select').css({"vertical-align":"middle","margin-top":"12px"});
# $('#settype input[type=radio]').css({"vertical-align":"middle","margin-top":"0px"});
#
# var width = $(window).width();
# var height = width*0.13;
# $("#butt1").css({"height":width*0.13});
# $(".userdiv").css({"margin-top":width*0.24});
#
# $('.showman').click(function(){
# 	$('input[name=mobile]').val('');
# 	$('input[name=mobile]').removeAttr('readOnly');
# 	$('input[name=bookholder]').val('');
# 	$('input[name=bookholder]').removeAttr('readOnly');
# 	$('input[name=idno]').val('');
# 	$('input[name=idno]').removeAttr('readOnly');
# });
#
# $('select[name=pays]').change(function(){
# 	var checkpay = $('select[name=pays] :selected').val();
# 	if(checkpay == '微信支付'){
# 		$('.huiyuanka').hide();
# 		 $('form').eq(0).attr("action","/index.php/yinlian/index/pay");
# 	}
# 	else if(checkpay == '会员卡'){
# 		$('.huiyuanka').show();
# 		$('form').eq(0).attr("action","/index.php/wxplace/place/huiyuanka");
# 	}
# });
#
# $('.aa div').click(function(){
# 	var checkpay = $(this).attr('value');
# 	if(checkpay == '微信'){
# 		$('.huiyuanka').hide();
# 		 $('form').eq(0).attr("action","/index.php/yinlian/index/pay");
# 	}
# 	else if(checkpay == '会员卡'){
# 		$('.huiyuanka').show();
# 		$('form').eq(0).attr("action","/index.php/wxplace/place/huiyuanka");
# 	}
#   $(".choose").text('启用');
#   $(".choose").removeClass("choose").addClass("nochoose");
#   $(this).addClass("choose").removeClass("nochoose");
#   $(this).text('已选');
# });
# </script>
# </body>
# </html>

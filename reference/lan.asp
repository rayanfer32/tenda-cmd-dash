<!DOCTYPE html>
<html> 
<head>
<meta charset="utf-8" />
<title>LAN | DHCP Client List</title>
<link rel="stylesheet" type="text/css" href="css/screen.css">
</head>

<body onLoad="init();">
<form name="frmSetup" id="frmSetup" method="POST" action="/goform/DhcpListClient">
    <input type="hidden" name="staticIpAddress" value="">
	<fieldset>
		<h2 class="legend">Static Assignment</h2>
		<table class="content2" id="table1">
			<tr>
				<td width="100" align="right" class="item1">IP Address</td>
				<td class="controls" nowrap colspan="2">
					<span id="netip_prefix"></span>
					<input id="IP" class="text input-medium" size="3" maxlength="3">
				</td>
			</tr>
			<tr>
				<td align="right" class="item1">MAC Address</td>
				<td class="controls">
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this, 1)">:
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this, 2)">:
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this, 3)">:
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this, 4)">:
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this, 5)">:
					<input type="text" id="MAC" class="text input-mic-mini" size="2" maxlength="2" onKeyUp="toNextMac(document.frmSetup, this)">
				</td>
				<td align=right>
					<input type="button" class="btn btn-small"  value="Add" id="ADD" onClick="add_static(IP,combinMAC2(MAC));">
				</td>
			</tr>
		 </table>
	
    <div id="staticlist" style="position:relative;visibility:visible;"></div>
	</fieldset>
	<fieldset>
		<h2 class="legend">DHCP Client List</h2>
		<table class="content1">
			<tr>
				<td align="right">
					<input type="button" class="btn btn-small" value="Refresh" id="Refresh"  onclick='refresh("lan_dhcp_clients.asp")'>
				</td>
			</tr>
		</table>
		<div id="dhcplist" style="position:relative;visibility:visible;"></div>
	</fieldset>
    <br>
    <div class="btn-group">
		<input type="button" class="btn" value="OK" onClick="preSubmit(document.frmSetup)" />
		<input type="button" class="btn last" value="Cancel" onClick="init(document.frmSetup)" />
	</div>
</form>
<script src="lang/b28n.js" type="text/javascript"></script>
<script>
//handle translate
(function() {
	B.setTextDomain(["base", "advanced"]);
	B.translate();
})();
</script>
<script type="text/javascript" src="js/gozila.js"></script>
<script>
var def_DHS = "192.168.0.100",//DHCP服务设置 IP池开始地址：最后一个字节
	def_DHE = "192.168.0.150",//DHCP服务设置 IP池结束地址：最后一个字节
	def_LEASE = "86400",//add by roy
	dhcpList=new Array('lg;192.168.0.105;90:00:4E:91:54:5D;0;74865','M2003J15SC-RedmiNote;192.168.0.100;2A:52:73:F1:FE:53;0;75011','ADRIAN;192.168.0.101;32:BC:8F:40:C8:B8;0;75411','rayanpc;192.168.0.103;14:18:77:B2:69:F4;0;75904','POCOM2Pro-POCOM2Pro;192.168.0.104;E0:1F:88:23:C4:92;0;80178','osmc;192.168.0.109;B8:27:EB:DF:C9:F8;0;84577',';192.168.0.102;40:B0:76:71:F0:30;0;84915'),//客户端列表 格式：'主机名;IP地址;MAC地址;静态(0:close;1:open);租约时间(秒数)',''、、、、、、、、、
	StaticList = new Array(),//静态列表//'ip;mac',、、、
	ipmaceninit = "",//????//'00000000',???
	def_LANIP = "192.168.0.1";//LAN口设置的IP地址
addCfg("DHS",1,def_DHS);
addCfg("DHE",3,def_DHE);
addCfg("LANIP",0,def_LANIP);
ctime=0;

var LANIP = getCfg("LANIP"),
	netip = LANIP.replace(/\.\d{1,3}$/,"."),
	dhs = getCfg("DHS").match(/\d{1,3}$/),
	dhe = getCfg("DHE").match(/\d{1,3}$/);

function showList() {
	var m='<table class="table">'
	m += '<thead><tr>';
	m += '<th nowrap>'+_("Host Name")+'</th>';
	m += '<th nowrap>'+_("IP Address")+'</th>';
	m += '<th nowrap>'+_("MAC Address")+'</th>';
	m += '<th nowrap>'+_("Lease Time")+'</th>';
	m += '</tr></thead>';
	m += '<tbody>';
	for (i=0;i<dhcpList.length;i++) {
		//;10.10.10.100;00:0C:43:30:52:66;0;3427243784d
		var s=dhcpList[i].split(";");
		//if (s.length!=4) break;
		//if (s.length!=5) break;//roy modified
		
		m+='<tr class=controls align=center>';
		if( s[0] == "") {
			m += '<td>'+"&nbsp;"+'</td>';
		} else {
			m += '<td>'+s[0]+'</td>';
		}
		m += '<td>'+s[1]+'</td>';
		m += '<td>'+s[2]+'</td>';
		m += '<td>'+timeStr(s[4]-ctime)+'</td>';//roy mdified
		m += '</tr>';
	}
	m += '</tbody></table>';
	document.getElementById("dhcplist").innerHTML = m;
}

function showStaticList() {
	var m='<table class="table" id="staticTab">';
	m+='<thead><tr>';
	m+='<th nowrap>' + _("NO.") + '</th>';
	m+='<th nowrap>' + _("IP Address") + '</th>';
	m+='<th nowrap>' + _("MAC Address") + '</th>';
	m+='<th nowrap>' + _("Delete") + '</th>';
	m+='</tr></thead>';
	m += '<tbody>';
	for (i=0;i<StaticList.length;i++) {
		//hostname;ip;mac;flag;lease
		var s=StaticList[i].split(";");
		//if (s.length!=2) break;
		if (s.length <4) break;//roy modified //modify by stanley
				
		m+='<tr class=controls align=center>';
		m+='<td>'+(i+1)+'</td>';
		m+='<td>'+s[1]+'</td>';
		m+='<td>'+s[2]+ '</td>';	
		m+='<td><input type=button class="btn btn-mini" value="' + _("Delete") + '" onclick="OnDel(this,' + i +  ')"></td>';
		m+='</tr>';
	}
	m += '</tbody></table>';
	document.getElementById("staticlist").innerHTML = m;
}

function OnDel(obj,dex){
	document.getElementById("staticTab").deleteRow(dex+1);
	var i=0;
	var box;
	for(i=dex;i<StaticList.length;i++){
		StaticList[i] = StaticList[(i+1)];
		if(i != StaticList.length -1){
			//box = document.getElementById("en"+(i+2));
			//box.id = "en"+(i+1);
		}
	}
	StaticList.length--;
	showStaticList();
}

function init(){
	for(i=0; i<6; i++) {
		document.frmSetup.elements['MAC'][i].value = "";
	}
	document.getElementById("netip_prefix").innerHTML = netip;
	document.frmSetup.elements['IP'].value = '';
	showList();
	showStaticList();
}

function preSubmit(f) {
	var s,
		loc = "/goform/DhcpListClient?GO=lan_dhcp_clients.asp",
		ipmacen = "",
		ipmac_enable = 1,
		ipmac_disable = 2;

	for (var i=0;i<StaticList.length;i++) {
		s=StaticList[i].split(";");
		ipmacen += "1";
		StaticList[i] = (s[0]+";"+s[1]+";"+s[2]+";"+ipmac_enable+";"+s[4]);
		loc += "&list" + (i + 1) + "=" + StaticList[i];
	}

	loc += "&IpMacEN=" + ipmacen;
	loc += "&LISTLEN=" + StaticList.length;
	window.location = loc; 
}
function add_static(ip, mac) {
	var all,
		f = document.frmSetup,
		hostname = "",//add by roy
		flag = "1";//static lease,add by roy
		
	ip.value = clearInvalidIpstr(ip.value);
	f.staticIpAddress.value = netip+ip.value;
	//add by stanley
	if(StaticList.length >15){
		alert(_("Up to 16 Address Reservations are supported!"));
		return ;
	}
	//add end
	if (!verifyIP2(f.staticIpAddress,_("IP address"))) return ;
	if (!macsCheck(mac,_("MAC address"))) return ;
	if(!ckMacReserve(mac))return ;
	all = StaticList.toString() + LANIP + ';';
	
	if (all.indexOf(netip+ip.value+';') >=0) {
		alert(_("Please don't add the LAN IP address or the IP address that already exists in the address Reservation table!"));
		return;
	}
	
	for (var k=0;k<StaticList.length;k++) {
		if (StaticList[k].toString().indexOf(mac) >=0) {
			if (!confirm(_("Please don't add MAC address that already exists in the address Reservation table!"))){
				return ;
			}
			rmEntry(StaticList, k);
		}
	}
	StaticList[StaticList.length]=(hostname+';'+netip+ip.value+';'+mac+';'+flag+';'+def_LEASE);//modified by roy
	showStaticList();
	
	//reset this iframe height by call parent iframe function
	window.parent.reinitIframe();
}

</script>
</body>
</html>
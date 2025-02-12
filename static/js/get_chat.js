var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "/get_msgs/" + PAGE_NUM, false); // false for synchronous request
let resp = xmlHttp.responseText;
alert(resp);

ol = document.getElementById("chat_msgs_ol");

for (let i=0; i < resp.length; i++) {
    msg_pkt = resp[i];
    new_li = createElement("li");
    new_li.innerHTML = msg_pkt[0] + ":<br />" + msg_pkt[1]
    ol.appendChild(new_li);
}

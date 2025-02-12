var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "/get_msgs/" + PAGE_NUM, false); // false for synchronous request
xmlHttp.send(null);
let resp = xmlHttp.responseText;
resp = JSON.parse(resp);

ol = document.getElementById("chat_msgs_ol");

console.log(resp);
console.log(resp.length);
for (let i=0; i < resp.length; i++) {
    msg_pkt = resp[i];
    new_li = document.createElement("li");
    new_li.classList.add("list-item");
    new_li.innerHTML = msg_pkt[0] + ":<br />" + msg_pkt[1]
    ol.appendChild(new_li);
}

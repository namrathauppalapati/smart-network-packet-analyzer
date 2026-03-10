let protocolCount = {
TCP:0,
UDP:0,
ICMP:0,
OTHER:0
}

let ctx = document.getElementById("protocolChart").getContext("2d")

let chart = new Chart(ctx,{
type:"pie",
data:{
labels:["TCP","UDP","ICMP","OTHER"],
datasets:[{
data:[0,0,0,0]
}]
}
})


async function loadPackets(){

let res = await fetch("/packets")

let data = await res.json()

let table = document.getElementById("packetTable")

table.innerHTML = `
<tr>
<th>Source IP</th>
<th>Destination IP</th>
<th>Protocol</th>
<th>Length</th>
</tr>
`

protocolCount = {TCP:0,UDP:0,ICMP:0,OTHER:0}

data.forEach(p => {

let row = table.insertRow()

row.insertCell(0).innerText = p.src
row.insertCell(1).innerText = p.dst
row.insertCell(2).innerText = p.protocol
row.insertCell(3).innerText = p.length

if(protocolCount[p.protocol] != undefined)
protocolCount[p.protocol]++
})

chart.data.datasets[0].data = [
protocolCount.TCP,
protocolCount.UDP,
protocolCount.ICMP,
protocolCount.OTHER
]

chart.update()

}

setInterval(loadPackets,2000)

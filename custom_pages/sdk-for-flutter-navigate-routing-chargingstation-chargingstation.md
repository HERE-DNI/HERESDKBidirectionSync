---
title: "ChargingStation constructor"
slug: "sdk-for-flutter-navigate-routing-chargingstation-chargingstation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation.html -->


<div>
<h1>ChargingStation constructor</h1></div>

ChargingStation(<ol class="parameter-list single-line"> <li>String? id, </li>
<li>String? name, </li>
<li><a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>? connectorAttributes</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>id</code> Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.</li>
<li><code>name</code> Human readable name of this charging station. It can be null when there is no
name associated with the station.</li>
<li><code>connectorAttributes</code> Details of the connector suggested to be used.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStation(this.id, this.name, this.connectorAttributes)
    : brand = null, chargePointOperator = null, matchingEMobilityServiceProviders = [];</code></pre>

 



</div>
`
}</HTMLBlock>

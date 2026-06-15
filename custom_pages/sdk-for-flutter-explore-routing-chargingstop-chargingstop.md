---
title: "ChargingStop constructor"
slug: "sdk-for-flutter-explore-routing-chargingstop-chargingstop"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStop.html -->


<div>
<h1>ChargingStop constructor</h1></div>

ChargingStop(<ol class="parameter-list"> <li>double powerInKilowatts, </li>
<li>double currentInAmperes, </li>
<li>double voltageInVolts, </li>
<li><a href="sdk-for-flutter-explore-routing-chargingsupplytype">ChargingSupplyType</a>? supplyType, </li>
<li>Duration? minDuration, </li>
<li>Duration? maxDuration, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>powerInKilowatts</code> The value of rated power of the connector (in kW).</li>
<li><code>currentInAmperes</code> The value of rated current of the connector (in A).</li>
<li><code>voltageInVolts</code> The value of rated voltage of the connector (in V).</li>
<li><code>supplyType</code> Supply type of the suggested connector.</li>
<li><code>minDuration</code> The minimum duration the user expects to charge at the station,
including <a href="sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</li>
<li><code>maxDuration</code> The maximum duration the user plans to charge at the station,
including <a href="sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStop(this.powerInKilowatts, this.currentInAmperes, this.voltageInVolts, this.supplyType, this.minDuration, this.maxDuration);</code></pre>

 



</div>
`
}</HTMLBlock>

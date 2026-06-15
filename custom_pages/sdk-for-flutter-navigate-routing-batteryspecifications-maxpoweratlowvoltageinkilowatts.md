---
title: "maxPowerAtLowVoltageInKilowatts property"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-maxpoweratlowvoltageinkilowatts"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maxPowerAtLowVoltageInKilowatts.html -->


<div>
<h1>maxPowerAtLowVoltageInKilowatts property</h1></div>

        
        double?
        maxPowerAtLowVoltageInKilowatts
<div class="features">getter/setter pair</div>


<p>The maximum power in kilowatts at which a vehicle can charge under given these conditions:</p>
<ul>
<li>The charging station connector's maximum supply voltage is less than 800 V.</li>
<li><a href="sdk-for-flutter-navigate-routing-batteryspecifications-maxchargingvoltageinvolts">BatterySpecifications.maxChargingVoltageInVolts</a> is greater than or equal to 800 V.
The provided value must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? maxPowerAtLowVoltageInKilowatts;</code></pre>

 



</div>
`
}</HTMLBlock>

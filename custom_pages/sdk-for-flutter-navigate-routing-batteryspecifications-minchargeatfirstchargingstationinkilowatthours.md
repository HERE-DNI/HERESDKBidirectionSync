---
title: "minChargeAtFirstChargingStationInKilowattHours property"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatfirstchargingstationinkilowatthours"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- minChargeAtFirstChargingStationInKilowattHours.html -->


<div>
<h1>minChargeAtFirstChargingStationInKilowattHours property</h1></div>

        
        double?
        minChargeAtFirstChargingStationInKilowattHours
<div class="features">getter/setter pair</div>


<p>Minimum charge when arriving at first charging station in kWh.
This overrides <a href="/sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station.
If not specified, <a href="/sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used
for all charging stations, including the first one.
Defaults to <code>null</code>.
When initialized, it must be non-negative and less than the value of
<a href="/sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>,
otherwise the <a href="/sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? minChargeAtFirstChargingStationInKilowattHours;</code></pre>

 



</div>
`
}</HTMLBlock>

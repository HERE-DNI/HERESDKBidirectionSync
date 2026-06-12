---
title: "initialChargeInKilowattHours property"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-initialchargeinkilowatthours"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- initialChargeInKilowattHours.html -->


<div>
<h1>initialChargeInKilowattHours property</h1></div>

        
        double
        initialChargeInKilowattHours
<div class="features">getter/setter pair</div>


<p>Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
<a href="/sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>,
otherwise the <a href="/sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="/sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double initialChargeInKilowattHours;</code></pre>

 



</div>
`
}</HTMLBlock>

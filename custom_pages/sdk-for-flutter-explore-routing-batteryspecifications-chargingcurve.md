---
title: "chargingCurve property"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-chargingcurve"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- chargingCurve.html -->


<div>
<h1>chargingCurve property</h1></div>

        
        Map&lt;double, double&gt;
chargingCurve
<div class="features">getter/setter pair</div>


<p>Function curve describing the maximum battery charging rate (in kW) at a given charge
level (in kWh).
Map keys represent charge levels that are non-negative floating point values
in units of (kWh).
Map values represent charging rate values that are positive floating point values
in units of (kW).
Given charge levels must cover the entire range of
[0, <a href="/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>],
otherwise the <a href="/sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned <a href="/sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;double, double&gt; chargingCurve;</code></pre>

 



</div>
`
}</HTMLBlock>

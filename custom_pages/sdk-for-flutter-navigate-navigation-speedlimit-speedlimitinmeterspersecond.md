---
title: "speedLimitInMetersPerSecond property"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- speedLimitInMetersPerSecond.html -->


<div>
<h1>speedLimitInMetersPerSecond property</h1></div>

        
        double?
        speedLimitInMetersPerSecond
<div class="features">getter/setter pair</div>


<p>Regular speed limit if available. In case of unbounded speed limit, the value is zero.</p>
<p><strong>Note:</strong>
When following a route, then this value will depend on the selected transport mode.
For other speed limits, like weather-dependent speed limits only the value as shown
on the local road sign is provided. It may not be applicable to all transport modes.
For tracking mode (without following a route), the VehicleProfile is ignored and only
the speed limit from the local road sign is provided or the regular speed limit
for a particular type of road or area like regular inner-city speed limits.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? speedLimitInMetersPerSecond;</code></pre>

 



</div>
`
}</HTMLBlock>

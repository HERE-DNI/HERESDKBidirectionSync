---
title: "advisorySpeedLimitInMetersPerSecond property"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-advisoryspeedlimitinmeterspersecond"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- advisorySpeedLimitInMetersPerSecond.html -->


<div>
<h1>advisorySpeedLimitInMetersPerSecond property</h1></div>

        
        double?
        advisorySpeedLimitInMetersPerSecond
<div class="features">getter/setter pair</div>


<p>A recommended speed limit that may not be indicated on the local road signs,
but that serves to warn a driver that the road conditions may indicate a lower speed.
Typically, the road condition is a curved road or a ramp but it may be due to a narrow road,
narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a
different road than the one for which it applies (this can happen with ramps). In this case,
the advisory speed is indicated for the road for which it is intended, even if the sign is
further than 50 meters from the particular road.</p>
<ul>
<li>Advisory speed signs due to construction are not included.</li>
<li>A speed value is published for advisory signs.</li>
</ul>
<p>A possible usage example can be to show an icon on the device's screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? advisorySpeedLimitInMetersPerSecond;</code></pre>

 



</div>
`
}</HTMLBlock>

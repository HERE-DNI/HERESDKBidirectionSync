---
title: "transitRadiusInMeters property"
slug: "sdk-for-flutter-navigate-routing-waypoint-transitradiusinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- transitRadiusInMeters.html -->


<div>
<h1>transitRadiusInMeters property</h1></div>

        
        int
        transitRadiusInMeters
<div class="features">getter/setter pair</div>


<p>The maximum allowed distance from the waypoint that the calculated
route may pass through. For example, to drive past a city without necessarily going
into the city center, you can specify the coordinates of the center and a transit
radius of 5000m. The default transit radius is zero.
If the route should pass the waypoint as close as possible, the default value
should be kept. Note that the waypoint will be map-matched to a road.
Non-zero values allow a greater tolerance.
Note that <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> option is ignored if the user sets this option with a value
greater than zero.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int transitRadiusInMeters;</code></pre>

 



</div>
`
}</HTMLBlock>

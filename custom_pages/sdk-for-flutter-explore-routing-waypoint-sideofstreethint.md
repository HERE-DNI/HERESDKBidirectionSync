---
title: "sideOfStreetHint property"
slug: "sdk-for-flutter-explore-routing-waypoint-sideofstreethint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sideOfStreetHint.html -->


<div>
<h1>sideOfStreetHint property</h1></div>

<a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?
        sideOfStreetHint
<div class="features">getter/setter pair</div>


<p>Optional coordinates to indicate which side of the street should be used to reach the waypoint.
For example, if the location is to the left of the street, the router will prefer using that side
in case the street has dividers.
Note that this option is ignored if the user sets <a href="/sdk-for-flutter-explore-routing-waypoint-transitradiusinmeters">Waypoint.transitRadiusInMeters</a> option with a
value greater than zero.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCoordinates? sideOfStreetHint;</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "Waypoint.withDefaults constructor"
slug: "sdk-for-flutter-explore-routing-waypoint-waypoint-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Waypoint.withDefaults.html -->


<div>
<h1>Waypoint.withDefaults constructor</h1></div>

Waypoint.withDefaults(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> coordinates</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>coordinates</code> The waypoint's geographic coordinates.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Waypoint.withDefaults(this.coordinates)
    : type = WaypointType.stopover, transitRadiusInMeters = 0, headingInDegrees = null, sideOfStreetHint = null, displayLocation = null, minCourseDistanceInMeters = null, nameHint = null, matchSideOfStreet = null, duration = const Duration(seconds: 0), segmentHint = null, onRoadThresholdInMeters = null, chargingStop = null, currentWeightChangeInKilograms = null;</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "MapMatchedLocation constructor"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-mapmatchedlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatchedLocation.html -->


<div>
<h1>MapMatchedLocation constructor</h1></div>

MapMatchedLocation(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li>double? bearingInDegrees</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>coordinates</code> The geographic coordinates of the map-matched location.</li>
<li><code>bearingInDegrees</code> The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
for east it's equal to 90, and so on.
If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
range [0, 360).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMatchedLocation(this.coordinates, this.bearingInDegrees)
    : segmentReference = SegmentReference.withDefaults(), segmentOffsetInCentimeters = 0, confidence = 0.0, isDrivingInTheWrongWay = false, horizontalAccuracyInMeters = null, speedInMetersPerSecond = null, timestamp = null;</code></pre>

 



</div>
`
}</HTMLBlock>

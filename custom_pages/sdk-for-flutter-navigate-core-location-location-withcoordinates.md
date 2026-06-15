---
title: "Location.withCoordinates constructor"
slug: "sdk-for-flutter-navigate-core-location-location-withcoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Location.withCoordinates.html -->


<div>
<h1>Location.withCoordinates constructor</h1></div>

Location.withCoordinates(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates</li>
</ol>)
    

<p>Creates a new Location instance from the provided GeoCoordinates value.
timestamp is initialized with <code>January 1, 1970, 00:00:00 GMT</code> value.
The rest of the fields will be initialized to null.</p>
<ul>
<li><code>coordinates</code> The geographic coordinates of the location.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Location.withCoordinates(this.coordinates)
    : bearingInDegrees = null, speedInMetersPerSecond = null, time = null, horizontalAccuracyInMeters = null, verticalAccuracyInMeters = null, bearingAccuracyInDegrees = null, speedAccuracyInMetersPerSecond = null, timestampSinceBoot = null, locationTechnology = null, source = null, gnssTime = null, pitchInDegrees = null;</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "GeoCoordinatesUpdate.withAltitude constructor"
slug: "sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-withaltitude"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinatesUpdate.withAltitude.html -->


<div>
<h1>GeoCoordinatesUpdate.withAltitude constructor</h1></div>

GeoCoordinatesUpdate.withAltitude(<ol class="parameter-list single-line"> <li>double? latitude, </li>
<li>double? longitude, </li>
<li>double? altitude</li>
</ol>)
    

<p>Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
and alt values.</p>
<p>Corrects values of latitude and longitude if they exceed the ranges.</p>
<ul>
<li>
<p><code>latitude</code> Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it's clamped to that range.
NaN value is converted to <code>null</code>.</p>
</li>
<li>
<p><code>longitude</code> Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it's replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to <code>null</code>.</p>
</li>
<li>
<p><code>altitude</code> Altitude in meters. NaN value is converted to <code>null</code>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoCoordinatesUpdate.withAltitude(double? latitude, double? longitude, double? altitude) =&gt; $prototype.withAltitude(latitude, longitude, altitude);</code></pre>

 



</div>
`
}</HTMLBlock>

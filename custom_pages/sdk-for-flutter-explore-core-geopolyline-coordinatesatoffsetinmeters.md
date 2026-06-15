---
title: "coordinatesAtOffsetInMeters method"
slug: "sdk-for-flutter-explore-core-geopolyline-coordinatesatoffsetinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- coordinatesAtOffsetInMeters.html -->


<div>
<h1>coordinatesAtOffsetInMeters method</h1></div>

<a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>
coordinatesAtOffsetInMeters(<ol class="parameter-list single-line"> <li>double offsetInMeters, </li>
<li><a href="sdk-for-flutter-explore-core-geopolylinedirection">GeoPolylineDirection</a> direction</li>
</ol>)

      

    

<p>Returns the coordinates at the given distance along the polyline.</p>
<p>When the polyline is
traversed from the beginning, the distance is calculated from the start of the
polyline; while a direction from the end indicates a distance from the last vertex.</p>
<p>The offset is expected to be non-negative and smaller than the length of the polyline.
When the offset is negative, the function returns the starting end point of the polyline,
i.e. the first vertex in positive direction and the last vertex in the negative direction.
Similarly, when the offset is larger than the length of the polyline, then the function
returns the opposite end point of the polyline.</p>
<p>The distance between two consecutive vertices is calculated using the
<a href="sdk-for-flutter-explore-core-geocoordinates-distanceto">GeoCoordinates.distanceTo</a> function. Therefore, it computes the distance (in meters) along
the great circle between the two vertices. Similarly, the full length of the polyline is the
sum of the distances between its vertices. The interpolation coordinates between two vertices
is calculated using the <a href="sdk-for-flutter-explore-core-geocoordinates-interpolate">GeoCoordinates.interpolate</a> function.</p>
<p>Note: the result may different from the analogue result from other matching components since
they may adapt the result to the length of the underlying object described by the polyline.</p>
<ul>
<li>
<p><code>offsetInMeters</code> The distance along the polyline in meters</p>
</li>
<li>
<p><code>direction</code> The direction in which the polyline is traversed.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>. The coordinates of the point at the given distance</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCoordinates coordinatesAtOffsetInMeters(double offsetInMeters, GeoPolylineDirection direction) =&gt; $prototype.coordinatesAtOffsetInMeters(this, offsetInMeters, direction);</code></pre>

 



</div>
`
}</HTMLBlock>

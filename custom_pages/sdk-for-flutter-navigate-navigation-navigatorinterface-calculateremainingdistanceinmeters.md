---
title: "calculateRemainingDistanceInMeters abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateRemainingDistanceInMeters.html -->


<div>
<h1>calculateRemainingDistanceInMeters abstract method</h1></div>

int?
calculateRemainingDistanceInMeters(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates</li>
</ol>)

      

    

<p>This method calculates the distance between the current position and given coordinates.</p>
<p>The coordinates must be on the polyline.</p>
<ul>
<li><code>coordinates</code> The geographic coordinates of the location.</li>
</ul>
<p>Returns <code>int?</code>. distance in meters or null if given coordinates are not on route or given
coordinates were already traversed.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? calculateRemainingDistanceInMeters(GeoCoordinates coordinates);</code></pre>

 



</div>
`
}</HTMLBlock>

---
title: "viewToGeoCoordinates abstract method"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- viewToGeoCoordinates.html -->


<div>
<h1>viewToGeoCoordinates abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?
viewToGeoCoordinates(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a> viewCoordinates</li>
</ol>)

      

    

<p>Converts view coordinates (in pixels) to geographical coordinates.</p>
<p>An optional altitude component of the resulting geographical coordinate is not set.</p>
<p>If the view coordinates specify a point above a horizon, then the result
is geographical coordinates of the point on a horizon below the specified
view coordinates.</p>
<p>The fog effect is ignored for the calculation, meaning that for the view point
within the area covered by the fog, the result is geographical coordinates
that would be displayed at the specified point if the fog effect was
not applied.</p>
<p>If the render surface is not attached, it will return <code>null</code>.</p>
<ul>
<li><code>viewCoordinates</code> Point inside the view to convert.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates?</a>. The geographical coordinates under specified view point or <code>null</code> if there is no render surface attached.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCoordinates? viewToGeoCoordinates(Point2D viewCoordinates);</code></pre>

 



</div>
`
}</HTMLBlock>

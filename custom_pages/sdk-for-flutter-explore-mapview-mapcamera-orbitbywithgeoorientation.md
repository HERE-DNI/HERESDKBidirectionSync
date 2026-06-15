---
title: "orbitByWithGeoOrientation abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-orbitbywithgeoorientation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- orbitByWithGeoOrientation.html -->


<div>
<h1>orbitByWithGeoOrientation abstract method</h1></div>

void
orbitByWithGeoOrientation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> delta, </li>
<li><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a> origin</li>
</ol>)

      

    

<p>Orbits the camera around a specified view point by increasing tilt and bearing by specified
delta values.</p>
<ul>
<li>
<p><code>delta</code> Camera orientation change, containing tilt and bearing angle deltas.</p>
</li>
<li>
<p><code>origin</code> Pixel point in view coordinates around which orbiting occurs.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void orbitByWithGeoOrientation(GeoOrientationUpdate delta, Point2D origin);</code></pre>

 



</div>
`
}</HTMLBlock>

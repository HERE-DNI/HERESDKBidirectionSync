---
title: "lookAtPointWithMeasure abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithMeasure.html -->


<div>
<h1>lookAtPointWithMeasure abstract method</h1></div>

void
lookAtPointWithMeasure(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> target, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> zoom</li>
</ol>)

      

    

<p>Makes the camera look at the geodetic target with the given zoom.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> Geodetic coordinates at which the camera will point.</p>
</li>
<li>
<p><code>zoom</code> The zoom level which can be provided as distance to the target point, scale or
zoom level.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtPointWithMeasure(GeoCoordinates target, MapMeasure zoom);</code></pre>

 



</div>
`
}</HTMLBlock>

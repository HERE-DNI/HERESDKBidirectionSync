---
title: "lookAtPoint abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-lookatpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoint.html -->


<div>
<h1>lookAtPoint abstract method</h1></div>

void
lookAtPoint(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> target</li>
</ol>)

      

    

<p>Makes the camera look at a new geodetic target, while
preserving the current orientation and distance to the target.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>target</code> Geodetic coordinates at which the camera will point.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtPoint(GeoCoordinates target);</code></pre>

 



</div>
`
}</HTMLBlock>

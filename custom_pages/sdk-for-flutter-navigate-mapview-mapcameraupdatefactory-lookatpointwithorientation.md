---
title: "lookAtPointWithOrientation static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpointwithorientation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithOrientation.html -->


<div>
<h1>lookAtPointWithOrientation static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtPointWithOrientation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target, </li>
<li><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation</li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the given target with the given
orientation preserving the current map measure (zoom level/distance/scale)
Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPointWithOrientation(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation) =&gt; $prototype.lookAtPointWithOrientation(target, orientation);</code></pre>

 



</div>
`
}</HTMLBlock>

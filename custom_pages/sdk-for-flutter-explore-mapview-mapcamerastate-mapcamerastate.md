---
title: "MapCameraState constructor"
slug: "sdk-for-flutter-explore-mapview-mapcamerastate-mapcamerastate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraState.html -->


<div>
<h1>MapCameraState constructor</h1></div>

MapCameraState(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> targetCoordinates, </li>
<li><a href="/sdk-for-flutter-explore-core-geoorientation-class">GeoOrientation</a> orientationAtTarget, </li>
<li>double distanceToTargetInMeters, </li>
<li>double zoomLevel, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>targetCoordinates</code> Camera's 'LookAt' target position in geodetic space.</li>
</ul>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>orientationAtTarget</code> Camera's orientation at target point.</li>
<li><code>distanceToTargetInMeters</code> Distance from the camera to the target point in meters.</li>
<li><code>zoomLevel</code> Zoom level corresponding to the current distance to target.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapCameraState(this.targetCoordinates, this.orientationAtTarget, this.distanceToTargetInMeters, this.zoomLevel);</code></pre>

 



</div>
`
}</HTMLBlock>

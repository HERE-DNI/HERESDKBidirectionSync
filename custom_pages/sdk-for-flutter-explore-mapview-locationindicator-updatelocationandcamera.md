---
title: "updateLocationAndCamera abstract method"
slug: "sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationAndCamera.html -->


<div>
<h1>updateLocationAndCamera abstract method</h1></div>

void
updateLocationAndCamera(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-location-class">Location</a> location, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a> cameraUpdate</li>
</ol>)

      

    

<p>Updates the indicator to a new location and applies a camera update at the same time.</p>
<p>Does nothing if the indicator instance is not enabled.
If accuracy visualized is set to <code>true</code> the field <a href="sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a>
determines the size of the accuracy indicator halo.</p>
<p>The altitude of the location is ignored.</p>
<ul>
<li>
<p><code>location</code> The updated location of the user.</p>
</li>
<li>
<p><code>cameraUpdate</code> The update to apply to the camera.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void updateLocationAndCamera(Location location, MapCameraUpdate cameraUpdate);</code></pre>

 



</div>
`
}</HTMLBlock>

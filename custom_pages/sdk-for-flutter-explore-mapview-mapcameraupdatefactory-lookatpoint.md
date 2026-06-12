---
title: "lookAtPoint static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoint.html -->


<div>
<h1>lookAtPoint static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtPoint(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target</li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the given target,
preserving the current orientation at look-at target and map measure.</p>
<p>Any target sub-element value that is not finite will be excluded from the update.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>target</code> The look-at target position in geodetic coordinates, altitude is ignored,
the target is considered to be located on the ground.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPoint(GeoCoordinatesUpdate target) =&gt; $prototype.lookAtPoint(target);</code></pre>

 



</div>
`
}</HTMLBlock>

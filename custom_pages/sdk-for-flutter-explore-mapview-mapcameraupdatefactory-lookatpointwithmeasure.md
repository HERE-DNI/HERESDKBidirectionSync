---
title: "lookAtPointWithMeasure static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithMeasure.html -->


<div>
<h1>lookAtPointWithMeasure static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtPointWithMeasure(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> measure</li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the given target with the given
map measure preserving the current orientation at look-at target.</p>
<p>Any target sub-element value that is not finite will be excluded from the update.
If the map measure is not valid, the current map camera distance to the target point is preserved.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>measure</code> The desired map measure.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPointWithMeasure(GeoCoordinatesUpdate target, MapMeasure measure) =&gt; $prototype.lookAtPointWithMeasure(target, measure);</code></pre>

 



</div>
`
}</HTMLBlock>

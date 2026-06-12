---
title: "lookAtArea static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtArea.html -->


<div>
<h1>lookAtArea static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtArea(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a> target</li>
</ol>)

      

    

<p>Creates an update to look at the given geo-box,
preserving current orientation and zooming at the center of viewport.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>target</code> Geodetic box that should be visible inside the viewport rectangle.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtArea(GeoBox target) =&gt; $prototype.lookAtArea(target);</code></pre>

 



</div>
`
}</HTMLBlock>

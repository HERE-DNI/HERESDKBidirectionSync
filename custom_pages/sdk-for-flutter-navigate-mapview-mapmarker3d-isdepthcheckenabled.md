---
title: "isDepthCheckEnabled property"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-isdepthcheckenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isDepthCheckEnabled.html -->


<div>
<h1>isDepthCheckEnabled property</h1></div>
<section id="getter">

bool
isDepthCheckEnabled


<p>Determines whether the depth of the 3D marker's vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p>
<p>By default depth check is set to <code>false</code>.</p>
<p>Use the altitude of the <a href="/sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a> to position the 3D marker sufficiently high above the
surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
3D model unexpectedly shine through.
Returns <code>true</code> if depth check is enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isDepthCheckEnabled;</code></pre>

</section>
<section id="setter">

void
isDepthCheckEnabled=(bool value)


<p>Determines whether the depth of the 3D marker's vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p>
<p>By default depth check is set to <code>false</code>.</p>
<p>Use the altitude of the <a href="/sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a> to position the 3D marker sufficiently high above the
surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
3D model unexpectedly shine through.
Set whether the depth of the 3D marker's vertices is considered during rendering.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isDepthCheckEnabled(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

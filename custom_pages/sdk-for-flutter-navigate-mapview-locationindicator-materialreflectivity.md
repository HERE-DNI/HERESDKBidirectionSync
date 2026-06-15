---
title: "materialReflectivity property"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-materialreflectivity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- materialReflectivity.html -->


<div>
<h1>materialReflectivity property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-mapview-materialreflectivity-class">MaterialReflectivity</a>?
materialReflectivity


<p>The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p>
<p>Default value is <code>null</code>.
Retrieves the material reflectivity applied to all markers of location indicator.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MaterialReflectivity? get materialReflectivity;</code></pre>

</section>
<section id="setter">

void
materialReflectivity=(<a href="sdk-for-flutter-navigate-mapview-materialreflectivity-class">MaterialReflectivity</a>? value)


<p>The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p>
<p>Default value is <code>null</code>.
Sets the material reflectivity properties for all markers of location indicator including its halo.
This value affects also any custom markers set with <code>setMarker3dModel</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set materialReflectivity(MaterialReflectivity? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

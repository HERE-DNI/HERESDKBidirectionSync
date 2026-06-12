---
title: "MaterialReflectivity class"
slug: "sdk-for-flutter-explore-mapview-materialreflectivity-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaterialReflectivity-class.html -->


<div>
<h1>MaterialReflectivity class</h1></div>

<p>Material reflectivity properties are used to enable per‑pixel lighting for supported map objects
(e.g.</p>
<p><code>LocationIndicator</code> markers and their halo).</p>
<h2 id="lighting-off-vs-on">Lighting OFF vs ON</h2>
<p>By default (when no MaterialReflectivity is assigned) objects are rendered "unlit" (emissive):
their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a
<code>MaterialReflectivity</code> instance to an object that supports it (e.g. <code>LocationIndicator.materialReflectivity</code>)
automatically enables lighting for this object and all its internal components. Clearing (setting the property to
<code>null</code>) disables lighting again and restores the unlit appearance.</p>
<h2 id="factors">Factors</h2>
<p>Both factors are expected to be within [0.0, 1.0]. Values outside this range are allowed but may
produce exaggerated results or be clamped by future implementations. Typical useful ranges:</p>
<ul>
<li>ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)</li>
<li>diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-materialreflectivity">MaterialReflectivity</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-ambientfactor">ambientFactor</a></li><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-diffusefactor">diffuseFactor</a></li><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-materialreflectivity-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

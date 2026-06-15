---
title: "MapMatcher class abstract"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatcher-class.html -->


<div>
<h1>MapMatcher class abstract</h1></div>

<p>This class provides map-matching functionality.</p>
<p>It determines whether a location can be
matched to a nearby road network and provides additional OCM map data for that location.</p>
<p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
behaviors. Related APIs may change in future releases without a deprecation process.</p>
<p>A <code>MapMatcher</code> maintains an internal state across location updates.
This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy
of the provided location.</p>
<p>A <code>MapMatcher</code> requires OCM tile data, either through caching, prefetching, or installed <code>Region</code> data.
If the necessary tiles are not found, an online request is initiated. Note that in such cases,
the download is triggered silently in the background, and <code>null</code> is returned
immediately.</p>
<p>The <code>MapMatcher</code> supports two layer configurations for retrieving segment geometry data:</p>
<ul>
<li>
<p><strong>Rendering layer (<code>LayerConfiguration.Feature.RENDERING</code>)</strong>: Enabled by default.
If your application uses map rendering or <code>MapView</code> components, using this layer is recommended.</p>
</li>
<li>
<p><strong>eHorizon layer (<code>LayerConfiguration.Feature.EHORIZON</code>)</strong>: Not enabled by default.
It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data.
Use the eHorizon layer when:</p>
<ul>
<li>No <code>MapView</code> is used in your application.</li>
<li>Only the eHorizon layer is used in your application.
In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.</li>
</ul>
</li>
</ul>
<p><strong>Important</strong>: If <code>useRenderingLayers</code> is set to <code>false</code> without properly enabling the eHorizon layer,
it may produce incorrect results. Layer configuration is especially important when prefetching or installing
region data. Missing data will be downloaded online automatically as needed.</p>
<p>If your hardware supports pitch and high precision altitude information and you want to use them in the <code>MapMatcher</code>
to improve map-matching, then enable the <code>LayerConfiguration.Feature.ADAS</code> layer:</p>
<ol>
<li>Turn on the <code>ADAS</code> layer via <code>LayerConfiguration.enabledFeatures</code> (it will increase data consumption).</li>
<li>If available, set <code>location.pitchInDegrees</code>, <code>location.coordinates.altitude</code> and <code>location.verticalAccuracyInMeters</code>.</li>
<li>In case of issues, please contact your HERE representative.</li>
</ol>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher">MapMatcher</a></li><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withengine">MapMatcher.withEngine</a></li><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withlayers">MapMatcher.withLayers</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-match">match</a></li><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

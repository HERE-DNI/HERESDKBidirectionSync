---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-mapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapMatcher.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/MapMatcher"></a>
<a title="MapMatcher  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        MapMatcher  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMatcher</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapMatcherC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMatcher"></a>
<a class="token" href="#/s:7heresdk10MapMatcherC">MapMatcher</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides map-matching functionality. It determines whether a location can be
matched to a nearby road network and provides additional OCM map data for that location.</p>
<p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
behaviors. Related APIs may change in future releases without a deprecation process.</p>
<p>A <code>MapMatcher</code> maintains an internal state across location updates.
This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy
of the provided location.</p>
<p>A <code>MapMatcher</code> requires OCM tile data, either through caching, prefetching, or installed <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code> data.
If the necessary tiles are not found, an online request is initiated. Note that in such cases,
the download is triggered silently in the background, and <code>nil</code> is returned
immediately.</p>
<p>The <code>MapMatcher</code> supports two layer configurations for retrieving segment geometry data:</p>
<ul>
<li><p><strong>Rendering layer (<code>LayerConfiguration.Feature.RENDERING</code>)</strong>: Enabled by default.
If your application uses map rendering or <code><a href="sdk-for-ios-navigate-api-reference-classes-mapview">MapView</a></code> components, using this layer is recommended.</p></li>
<li><p><strong>eHorizon layer (<code>LayerConfiguration.Feature.EHORIZON</code>)</strong>: Not enabled by default.
It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data.
Use the eHorizon layer when:</p>
<ul>
<li>No <code><a href="sdk-for-ios-navigate-api-reference-classes-mapview">MapView</a></code> is used in your application.</li>
<li>Only the eHorizon layer is used in your application.
In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.</li>
</ul></li>
</ul>
<p><strong>Important</strong>: If <code>useRenderingLayers</code> is set to <code>false</code> without properly enabling the eHorizon layer,
it may produce incorrect results. Layer configuration is especially important when prefetching or installing
region data. Missing data will be downloaded online automatically as needed.</p>
<p>If your hardware supports pitch and high precision altitude information and you want to use them in the <code>MapMatcher</code>
to improve map-matching, then enable the <code>LayerConfiguration.Feature.ADAS</code> layer:</p>
<ol>
<li>Turn on the <code>ADAS</code> layer via <code><a href="Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code> (it will increase data consumption).</li>
<li>If available, set <code>location.pitchInDegrees</code>, <code>location.coordinates.altitude</code> and <code>location.verticalAccuracyInMeters</code>.</li>
<li>In case of issues, please contact your HERE representative.</li>
</ol>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMatcher</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMatcher</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMatcher</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MatchedLocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MatchedLocation"></a>
<a class="token" href="#/s:7heresdk15MatchedLocationV">MatchedLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The result of matching the original location to the available map.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-matchedlocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MatchedLocation</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

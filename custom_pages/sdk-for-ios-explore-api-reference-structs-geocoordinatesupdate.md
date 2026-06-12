---
title: "GeoCoordinatesUpdate"
slug: "sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCoordinatesUpdate"></a>
<a title="GeoCoordinatesUpdate Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-core">Core</a>

        GeoCoordinatesUpdate Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GeoCoordinatesUpdate</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoCoordinatesUpdate</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents geographical coordinates in 3D space.
Unlike <code><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></code>, its members can be undefined, allowing for APIs
that update only the specified parts of geo coordinates.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV8latitudeSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/latitude"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV8latitudeSdSgvp">latitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional latitude in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV9longitudeSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/longitude"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV9longitudeSdSgvp">longitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional longitude in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV8altitudeSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/altitude"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV8altitudeSdSgvp">altitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional altitude in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV8latitude9longitudeACSdSg_AFtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(latitude:longitude:)"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV8latitude9longitudeACSdSg_AFtcfc">init(latitude:<wbr/>longitude:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCoordinatesUpdate from the provided latitude and
longitude values.
Corrects values of latitude and longitude if they exceed the ranges.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?,</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>latitude</em>
</code>
</td>
<td>
<div>
<p>Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it’s clamped to that range.
NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>longitude</em>
</code>
</td>
<td>
<div>
<p>Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it’s replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV8latitude9longitude8altitudeACSdSg_A2Gtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(latitude:longitude:altitude:)"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV8latitude9longitude8altitudeACSdSg_A2Gtcfc">init(latitude:<wbr/>longitude:<wbr/>altitude:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
and alt values.
Corrects values of latitude and longitude if they exceed the ranges.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?,</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?,</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>latitude</em>
</code>
</td>
<td>
<div>
<p>Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it’s clamped to that range.
NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>longitude</em>
</code>
</td>
<td>
<div>
<p>Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it’s replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>altitude</em>
</code>
</td>
<td>
<div>
<p>Altitude in meters. NaN value is converted to <code>nil</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateVyAcA0bC0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateVyAcA0bC0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCoordinatesUpdate from GeoCoordinates</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>GeoCoordinates to construct GeoCoordinatesUpdate.</p>
</div>
</td>
</tr>
</tbody>
</table>
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

`
} </HTMLBlock>

---
title: "sdk-for-ios-explore-api-reference-structs-locationdetails"
slug: "sdk-for-ios-explore-api-reference-structs-locationdetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationDetails"></a>
<a title="LocationDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains geographical info about location</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV23coordinatesInterpolatedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinatesInterpolated"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV23coordinatesInterpolatedSbvp">coordinatesInterpolated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if has house number with coordinates interpolated from the address range.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinatesInterpolated</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV12accessPointsSayAA14GeoCoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/accessPoints"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV12accessPointsSayAA14GeoCoordinatesVGvp">accessPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The access points to the place, such as the points on a road or in a parking lot.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">accessPoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV11boundingBoxAA03GeoE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV11boundingBoxAA03GeoE0VSgvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the map bounding box containing the place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationDetailsV11coordinates0D12Interpolated12accessPoints11boundingBoxAcA14GeoCoordinatesV_SbSayAIGAA0jI0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:coordinatesInterpolated:accessPoints:boundingBox:)"></a>
<a class="token" href="#/s:7heresdk15LocationDetailsV11coordinates0D12Interpolated12accessPoints11boundingBoxAcA14GeoCoordinatesV_SbSayAIGAA0jI0VSgtcfc">init(coordinates:<wbr/>coordinatesInterpolated:<wbr/>accessPoints:<wbr/>boundingBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">coordinatesInterpolated</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">accessPoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

`
}</HTMLBlock>

---
title: "LocationDetails Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-locationdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LocationDetails.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationDetails"></a>
<a title="LocationDetails Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct LocationDetails : Hashable</code></pre>
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
<pre><code>public var coordinates: GeoCoordinates</code></pre>
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
<pre><code>public var coordinatesInterpolated: Bool</code></pre>
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
<pre><code>public var accessPoints: [GeoCoordinates]</code></pre>
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
<pre><code>public var boundingBox: GeoBox?</code></pre>
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
<pre><code>public init(coordinates: GeoCoordinates, coordinatesInterpolated: Bool = false, accessPoints: [GeoCoordinates] = [], boundingBox: GeoBox? = nil)</code></pre>
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



</div>
`
}</HTMLBlock>

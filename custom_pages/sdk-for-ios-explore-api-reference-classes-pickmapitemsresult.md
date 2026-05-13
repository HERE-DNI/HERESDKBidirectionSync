---
title: "PickMapItemsResult Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-pickmapitemsresult"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PickMapItemsResult.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PickMapItemsResult"></a>
<a title="PickMapItemsResult Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PickMapItemsResult Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PickMapItemsResult</code></pre>
<pre><code>extension PickMapItemsResult: NativeBase</code></pre>
<pre><code>extension PickMapItemsResult: Hashable</code></pre>
</div>
</div>
<p>Carries results from the picking of map items on the map scene.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC16clusteredMarkersSayAA0C13MarkerClusterC8GroupingVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/clusteredMarkers"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC16clusteredMarkersSayAA0C13MarkerClusterC8GroupingVGvp">clusteredMarkers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of marker groups (represented by a single cluster marker)
or individual markers belonging to a cluster at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var clusteredMarkers: [MapMarkerCluster.Grouping] { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC7markersSayAA0C6MarkerCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/markers"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC7markersSayAA0C6MarkerCGvp">markers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of markers at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var markers: [MapMarker] { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC9markers3dSayAA0C8Marker3DCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/markers3d"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC9markers3dSayAA0C8Marker3DCGvp">markers3d</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of 3d markers at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var markers3d: [MapMarker3D] { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC9polylinesSayAA0C8PolylineCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polylines"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC9polylinesSayAA0C8PolylineCGvp">polylines</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of polylines at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var polylines: [MapPolyline] { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC8polygonsSayAA0C7PolygonCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polygons"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC8polygonsSayAA0C7PolygonCGvp">polygons</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of polygons at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var polygons: [MapPolygon] { get }</code></pre>
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

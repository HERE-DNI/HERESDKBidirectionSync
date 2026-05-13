---
title: "Maps / PickMapItemsResult"
slug: "sdk-for-ios-explore-api-reference-classes-pickmapitemsresult"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PickMapItemsResult"></a>
<a title="PickMapItemsResult Class Reference"></a>

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
<h1>PickMapItemsResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PickMapItemsResult</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapItemsResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapItemsResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">clusteredMarkers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarkercluster">MapMarkerCluster</a></span><span class="o">.</span><span class="kt">Grouping</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker">MapMarker</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">markers3d</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3d">MapMarker3D</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">polylines</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mappolyline">MapPolyline</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">polygons</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mappolygon">MapPolygon</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

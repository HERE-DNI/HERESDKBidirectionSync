---
title: "MapMarkerCluster"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarkercluster"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarkerCluster"></a>
<a title="MapMarkerCluster Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        MapMarkerCluster Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMarkerCluster</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarkerCluster</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerCluster</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerCluster</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
them in a small area.</p>
<p>The markers that are close to each other are replaced by a single cluster marker. Cluster groups
are generated based on geographical distance between objects, not based on screen space collision.
Hence it is possible, that cluster markers can overlap.</p>
<p>The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
map, add it to the scene using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF">MapScene.addMapMarkerCluster(...)</a></code>. The display of a cluster is only
guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p>
<p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC10imageStyleA2C05ImageF0V_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(imageStyle:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10imageStyleA2C05ImageF0V_tcfc">init(imageStyle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of a map marker cluster which is represented as an image.</p>
<p>Any modification to object passed as <code>imageStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">imageStyle</span><span class="p">:</span> <span class="kt">MapMarkerCluster</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-imagestyle">ImageStyle</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>imageStyle</em>
</code>
</td>
<td>
<div>
<p>The visual representation for the cluster.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC10imageStyle07counterF0A2C05ImageF0V_AC07CounterF0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(imageStyle:counterStyle:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10imageStyle07counterF0A2C05ImageF0V_AC07CounterF0Vtcfc">init(imageStyle:<wbr/>counterStyle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of a map marker cluster which is represented as an image along with a counter
showing how many markers are actually grouped under particular cluster icon.</p>
<p>Any modification to <code>imageStyle</code> or <code>counterStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">imageStyle</span><span class="p">:</span> <span class="kt">MapMarkerCluster</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-imagestyle">ImageStyle</a></span><span class="p">,</span> <span class="nv">counterStyle</span><span class="p">:</span> <span class="kt">MapMarkerCluster</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-counterstyle">CounterStyle</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>imageStyle</em>
</code>
</td>
<td>
<div>
<p>Describes the visual appearance of cluster icon.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>counterStyle</em>
</code>
</td>
<td>
<div>
<p>Describes the appearance of marker count label.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC7markersSayAA0bC0CGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/markers"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC7markersSayAA0bC0CGvp">markers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of map markers which currently belong to this cluster.
Modifying the list has no effect on the marker cluster.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC7opacitySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/opacity"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC7opacitySdvp">opacity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
The value is clamped in range [0.0, 1.0]. Default value is 1.0 which means marker cluster
is displayed with the default opacity of the image.</p>
<p>Marker clusters with opacity value set to 0.0 are still on map and are considered for picking.</p>
<p>Markers part of cluster will use their respective opacity when not displayed as a cluster icon.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">opacity</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC8GroupingV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Grouping"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC8GroupingV">Grouping</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a group of map markers belonging to a cluster.</p>
<p>It contains a list of map markers grouped on map view under single icon of marker cluster or
single map marker entry for markers being part of cluster but spread enough not to be grouped.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-grouping">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Grouping</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC10ImageStyleV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ImageStyle"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC10ImageStyleV">ImageStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class specifies the visual appearance of a cluster marker.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-imagestyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ImageStyle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CounterStyle"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV">CounterStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Styling options for a marker cluster which is represented by the marker count as a text.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-counterstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CounterStyle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC03addbC06markeryAA0bC0C_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarker(marker:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC03addbC06markeryAA0bC0C_tF">addMapMarker(marker:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map marker to this cluster. Adding a marker which is already part of the cluster or
which was already added to the map scene has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarker</span><span class="p">(</span><span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC03addB7Markers7markersySayAA0bC0CG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarkers(markers:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC03addB7Markers7markersySayAA0bC0CG_tF">addMapMarkers(markers:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a list of map markers to this cluster.</p>
<p>Markers which are already part of the cluster or
which were already added to the map scene will be ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarkers</span><span class="p">(</span><span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of markers.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC06removebC06markeryAA0bC0C_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarker(marker:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC06removebC06markeryAA0bC0C_tF">removeMapMarker(marker:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map marker from this cluster.</p>
<p>Removing a marker which is not part of this cluster has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarker</span><span class="p">(</span><span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC06removeB7Markers7markersySayAA0bC0CG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarkers(markers:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC06removeB7Markers7markersySayAA0bC0CG_tF">removeMapMarkers(markers:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a list of map markers from this cluster.</p>
<p>Removing markers which are not part of this cluster has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarkers</span><span class="p">(</span><span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of markers.</p>
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
<a name="/s:7heresdk16MapMarkerClusterC09removeAllB7MarkersyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapMarkers()"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC09removeAllB7MarkersyyF">removeAllMapMarkers()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all map markers from this cluster.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapMarkers</span><span class="p">()</span></code></pre>
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

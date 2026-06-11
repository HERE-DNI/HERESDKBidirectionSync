---
title: "IndoorRouteStyle"
slug: "sdk-for-ios-navigate-api-reference-classes-indoorroutestyle"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IndoorRouteStyle"></a>
<a title="IndoorRouteStyle Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        IndoorRouteStyle Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorRouteStyle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndoorRouteStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRouteStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRouteStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a style of the indoor route. Contains information about route colors and widths.
Optionally, this style allows to set <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> instances that can be used for
specific route elements.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC19indoorPolylineWidthSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorPolylineWidth"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC19indoorPolylineWidthSdvp">indoorPolylineWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The width in pixels. Default value is 15 pixels
The width in pixels of polylines for indoor route sections.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">indoorPolylineWidth</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC19indoorPolylineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorPolylineColor"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC19indoorPolylineColorSo7UIColorCvp">indoorPolylineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color value. The default color is #48DAD0.
The color of polylines for indoor route sections.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">indoorPolylineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC11startMarkerAA03MapF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startMarker"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC11startMarkerAA03MapF0CSgvp">startMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> instance representing the start of the route. By default, no map marker is provided.
The start map marker of the resulting route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC17destinationMarkerAA03MapF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/destinationMarker"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC17destinationMarkerAA03MapF0CSgvp">destinationMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> instance representing the destination of the route. By default, no map marker is provided
The destination map marker of the resulting route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">destinationMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC10walkMarkerAA03MapF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/walkMarker"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC10walkMarkerAA03MapF0CSgvp">walkMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> instance representing the walk point of the route. By default, no map marker is provided.
The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">walkMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC11driveMarkerAA03MapF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/driveMarker"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC11driveMarkerAA03MapF0CSgvp">driveMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> instance representing the drive point of the route. By default, no map marker is provided.
The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">driveMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC03getB9MarkerFor7feature6deltaZAA03MapF0CSgAA0B19LevelChangeFeaturesO_s5Int32VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getIndoorMarkerFor(feature:deltaZ:)"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC03getB9MarkerFor7feature6deltaZAA03MapF0CSgAA0B19LevelChangeFeaturesO_s5Int32VtF">getIndoorMarkerFor(feature:<wbr/>deltaZ:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> for a given indoor feature and
the number of levels to change. By default, no map markers are provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getIndoorMarkerFor</span><span class="p">(</span><span class="nv">feature</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span><span class="p">,</span> <span class="nv">deltaZ</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>feature</em>
</code>
</td>
<td>
<div>
<p>An indoor feature.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>deltaZ</em>
</code>
</td>
<td>
<div>
<p>A number of levels to change, positive for up, negative for down.
In the case of 0, the method returns an exit map marker.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The result <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code>, if it was set.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRouteStyleC03setB10MarkersFor7feature8upMarker04downJ004exitJ0yAA0B19LevelChangeFeaturesO_AA03MapJ0CSgA2MtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setIndoorMarkersFor(feature:upMarker:downMarker:exitMarker:)"></a>
<a class="token" href="#/s:7heresdk16IndoorRouteStyleC03setB10MarkersFor7feature8upMarker04downJ004exitJ0yAA0B19LevelChangeFeaturesO_AA03MapJ0CSgA2MtF">setIndoorMarkersFor(feature:<wbr/>upMarker:<wbr/>downMarker:<wbr/>exitMarker:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets map markers for the given indoor feature.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setIndoorMarkersFor</span><span class="p">(</span><span class="nv">feature</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span><span class="p">,</span> <span class="nv">upMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?,</span> <span class="nv">downMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?,</span> <span class="nv">exitMarker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>feature</em>
</code>
</td>
<td>
<div>
<p>An indoor feature.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>upMarker</em>
</code>
</td>
<td>
<div>
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> to go up.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>downMarker</em>
</code>
</td>
<td>
<div>
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> to go down.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>exitMarker</em>
</code>
</td>
<td>
<div>
<p>A <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code> to exit the indoor feature.</p>
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
}</HTMLBlock>

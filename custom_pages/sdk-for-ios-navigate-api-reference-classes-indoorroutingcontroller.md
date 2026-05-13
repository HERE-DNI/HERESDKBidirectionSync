---
title: "Routing / IndoorRoutingController"
slug: "sdk-for-ios-navigate-api-reference-classes-indoorroutingcontroller"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IndoorRoutingController"></a>
<a title="IndoorRoutingController Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IndoorRoutingController Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorRoutingController</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndoorRoutingController</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRoutingController</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRoutingController</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class controls the rendering of indoor routes on the map.
<br/>
Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23IndoorRoutingControllerC_7mapViewAcA8VenueMapC_AA0hF4Base_ptcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:mapView:)"></a>
<a class="token" href="#/s:7heresdk23IndoorRoutingControllerC_7mapViewAcA8VenueMapC_AA0hF4Base_ptcfc">init(_:<wbr/>mapView:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">venueMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemap">VenueMap</a></span><span class="p">,</span> <span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>venueMap</em>
</code>
</td>
<td>
<div>
<p>A venue map instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>A map scene where routes should be shown.</p>
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
<a name="/s:7heresdk23IndoorRoutingControllerC9showRoute5route5styleyAA0F0C_AA0bF5StyleCtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/showRoute(route:style:)"></a>
<a class="token" href="#/s:7heresdk23IndoorRoutingControllerC9showRoute5route5styleyAA0F0C_AA0bF5StyleCtF">showRoute(route:<wbr/>style:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Shows an indoor route on the map. The previously visible indoor route will be hidden.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">showRoute</span><span class="p">(</span><span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></span><span class="p">,</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-indoorroutestyle">IndoorRouteStyle</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>route</em>
</code>
</td>
<td>
<div>
<p>A route to show</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>A route style for the given route.</p>
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
<a name="/s:7heresdk23IndoorRoutingControllerC9hideRouteyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/hideRoute()"></a>
<a class="token" href="#/s:7heresdk23IndoorRoutingControllerC9hideRouteyyF">hideRoute()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hides an indoor route, visible on the map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">hideRoute</span><span class="p">()</span></code></pre>
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

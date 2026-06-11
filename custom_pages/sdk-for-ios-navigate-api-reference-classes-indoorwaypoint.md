---
title: "sdk-for-ios-navigate-api-reference-classes-indoorwaypoint"
slug: "sdk-for-ios-navigate-api-reference-classes-indoorwaypoint"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IndoorWaypoint"></a>
<a title="IndoorWaypoint Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        IndoorWaypoint Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorWaypoint</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndoorWaypoint</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorWaypoint</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorWaypoint</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents an indoor waypoint, used as input for indoor route calculation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorWaypointC11coordinates7venueId05levelF0AcA14GeoCoordinatesV_S2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:venueId:levelId:)"></a>
<a class="token" href="#/s:7heresdk14IndoorWaypointC11coordinates7venueId05levelF0AcA14GeoCoordinatesV_S2Stcfc">init(coordinates:<wbr/>venueId:<wbr/>levelId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an indoor waypoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">venueId</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">levelId</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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
<p>A waypoint’s geographic coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>venueId</em>
</code>
</td>
<td>
<div>
<p>An ID of the venue where the waypoint is located.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>levelId</em>
</code>
</td>
<td>
<div>
<p>An ID of the level where the waypoint is located</p>
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
<a name="/s:7heresdk14IndoorWaypointC11coordinatesAcA14GeoCoordinatesV_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:)"></a>
<a class="token" href="#/s:7heresdk14IndoorWaypointC11coordinatesAcA14GeoCoordinatesV_tcfc">init(coordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an outdoor waypoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span></code></pre>
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
<p>A waypoint’s geographic coordinates.</p>
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
<a name="/s:7heresdk14IndoorWaypointC11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk14IndoorWaypointC11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The waypoint’s geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorWaypointC7venueIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueId"></a>
<a class="token" href="#/s:7heresdk14IndoorWaypointC7venueIdSSSgvp">venueId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ID of the venue where the waypoint is located, if applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueId</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorWaypointC7levelIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levelId"></a>
<a class="token" href="#/s:7heresdk14IndoorWaypointC7levelIdSSSgvp">levelId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ID of the level where the waypoint is located, if applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">levelId</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

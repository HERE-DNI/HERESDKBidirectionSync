---
title: "PickMapContentResult"
slug: "sdk-for-ios-explore-classes-pickmapcontentresult"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PickMapContentResult"></a>
<a title="PickMapContentResult Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-maps">Maps</a>

        PickMapContentResult Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PickMapContentResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PickMapContentResult</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapContentResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapContentResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class that contains possible results from picking map content on the map scene.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC12pickedPlacesSayAA11PickedPlaceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pickedPlaces"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC12pickedPlacesSayAA11PickedPlaceVGvp">pickedPlaces</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of picked places containing the POIs at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pickedPlaces</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-structs-pickedplace">PickedPlace</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC16trafficIncidentsSayAC015TrafficIncidentE0CGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficIncidents"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC16trafficIncidentsSayAC015TrafficIncidentE0CGvp">trafficIncidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of traffic incidents at the location of picking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficIncidents</span><span class="p">:</span> <span class="p">[</span><span class="kt">PickMapContentResult</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-classes-pickmapcontentresult-trafficincidentresult">TrafficIncidentResult</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncidentResult"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C">TrafficIncidentResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Carries the result of picking a Carto traffic incident object.
Description of incident is currently not present in our map data, so
<code>description</code> always returns an empty string.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-classes-pickmapcontentresult-trafficincidentresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficIncidentResult</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-classes-pickmapcontentresult">PickMapContentResult</a></span><span class="o">.</span><span class="kt">TrafficIncidentResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-classes-pickmapcontentresult">PickMapContentResult</a></span><span class="o">.</span><span class="kt">TrafficIncidentResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
} </HTMLBlock>

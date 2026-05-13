---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-pickmapcontentresult-trafficincidentresult"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficIncidentResult.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncidentResult"></a>
<a title="TrafficIncidentResult Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-classes-pickmapcontentresult">PickMapContentResult</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        TrafficIncidentResult Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficIncidentResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficIncidentResult</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-protocols-trafficincidentbase">TrafficIncidentBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-pickmapcontentresult">PickMapContentResult</a></span><span class="o">.</span><span class="kt">TrafficIncidentResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-pickmapcontentresult">PickMapContentResult</a></span><span class="o">.</span><span class="kt">TrafficIncidentResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Carries the result of picking a Carto traffic incident object.
Description of incident is currently not present in our map data, so
<code>description</code> always returns an empty string.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C6impactAA0fG6ImpactOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/impact"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C6impactAA0fG6ImpactOvp">impact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The impact of the incident.
The value is <code><a href="../../Enums/TrafficIncidentImpact.html#/s:7heresdk21TrafficIncidentImpactO7unknownyA2CmF">TrafficIncidentImpact.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">impact</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-enums-trafficincidentimpact">TrafficIncidentImpact</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C4typeAA0fG4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C4typeAA0fG4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The category of the incident.
The value is <code><a href="../../Enums/TrafficIncidentType.html#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">TrafficIncidentType.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-enums-trafficincidenttype">TrafficIncidentType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11descriptionAA13LocalizedTextVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11descriptionAA13LocalizedTextVvp">description</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The human readable description of the incident, possibly with location information.
The description is currently not present in our map data. Therefore, when
accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
always an empty string is returned. This does not apply when using the <code><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trafficengine">TrafficEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">description</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-localizedtext">LocalizedText</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C9startTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startTime"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C9startTime10Foundation4DateVSgvp">startTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>nil</code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C7endTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endTime"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C7endTime10Foundation4DateVSgvp">endTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>nil</code> if it hasn’t been provided by the traffic incidents supplier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">endTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C10originalIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/originalId"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C10originalIdSSvp">originalId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique traffic event ID.
Can be referenced when checking for updated traffic information
for the specified event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">originalId</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the traffic incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-geocoordinates">GeoCoordinates</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

</div>
`
}</HTMLBlock>

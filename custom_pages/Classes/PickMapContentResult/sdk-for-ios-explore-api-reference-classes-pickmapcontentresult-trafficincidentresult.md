---
title: "TrafficIncidentResult Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-pickmapcontentresult-trafficincidentresult"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficIncidentResult.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncidentResult"></a>
<a title="TrafficIncidentResult Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Maps.html">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Classes/PickMapContentResult.html">PickMapContentResult</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        TrafficIncidentResult Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class TrafficIncidentResult : TrafficIncidentBase</code></pre>
<pre><code>extension PickMapContentResult.TrafficIncidentResult: NativeBase</code></pre>
<pre><code>extension PickMapContentResult.TrafficIncidentResult: Hashable</code></pre>
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
<pre><code>public var impact: TrafficIncidentImpact { get }</code></pre>
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
<pre><code>public var type: TrafficIncidentType { get }</code></pre>
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
always an empty string is returned. This does not apply when using the <code><a href="../../Classes/TrafficEngine.html">TrafficEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var description: LocalizedText { get }</code></pre>
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
<pre><code>public var startTime: Date? { get }</code></pre>
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
<pre><code>public var endTime: Date? { get }</code></pre>
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
<pre><code>public var originalId: String { get }</code></pre>
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
<pre><code>public var coordinates: GeoCoordinates { get }</code></pre>
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

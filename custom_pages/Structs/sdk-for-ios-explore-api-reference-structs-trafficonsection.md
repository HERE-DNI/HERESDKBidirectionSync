---
title: "TrafficOnSection Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-trafficonsection"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficOnSection.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficOnSection"></a>
<a title="TrafficOnSection Structure Reference"></a>
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
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficOnSection Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct TrafficOnSection : Hashable</code></pre>
</div>
</div>
<p>Traffic information on a section.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of coordinates representing the polyline of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var geometry: [GeoCoordinates]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV12trafficSpansSayAA0bC4SpanVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSpans"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV12trafficSpansSayAA0bC4SpanVGvp">trafficSpans</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of traffic spans.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var trafficSpans: [TrafficOnSpan]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficIncidents"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp">trafficIncidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of traffic incidents.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var trafficIncidents: [TrafficIncidentOnRoute]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/departurePlace"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp">departurePlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the departure place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var departurePlace: RoutePlace</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalPlace"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp">arrivalPlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the arrival place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var arrivalPlace: RoutePlace</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficOnSectionV8geometry12trafficSpans0F9Incidents14departurePlace07arrivalJ0ACSayAA14GeoCoordinatesVG_SayAA0bC4SpanVGSayAA0b8IncidentC5RouteCGAA0pJ0VAStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometry:trafficSpans:trafficIncidents:departurePlace:arrivalPlace:)"></a>
<a class="token" href="#/s:7heresdk16TrafficOnSectionV8geometry12trafficSpans0F9Incidents14departurePlace07arrivalJ0ACSayAA14GeoCoordinatesVG_SayAA0bC4SpanVGSayAA0b8IncidentC5RouteCGAA0pJ0VAStcfc">init(geometry:<wbr/>trafficSpans:<wbr/>trafficIncidents:<wbr/>departurePlace:<wbr/>arrivalPlace:<wbr/>)</a>
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
<pre><code>public init(geometry: [GeoCoordinates] = [], trafficSpans: [TrafficOnSpan] = [], trafficIncidents: [TrafficIncidentOnRoute] = [], departurePlace: RoutePlace, arrivalPlace: RoutePlace)</code></pre>
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

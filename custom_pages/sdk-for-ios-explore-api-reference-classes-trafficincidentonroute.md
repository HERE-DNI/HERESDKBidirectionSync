---
title: "TrafficIncidentOnRoute Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-trafficincidentonroute"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficIncidentOnRoute.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncidentOnRoute"></a>
<a title="TrafficIncidentOnRoute Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-traffic">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficIncidentOnRoute Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class TrafficIncidentOnRoute : TrafficIncidentBase</code></pre>
<pre><code>extension TrafficIncidentOnRoute: NativeBase</code></pre>
<pre><code>extension TrafficIncidentOnRoute: Hashable</code></pre>
</div>
</div>
<p>Traffic incidents on a route. Use <code><a href="../Classes/Section.html#/s:7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">Section.trafficIncidents</a></code> to get a list of incidents on a route section.
Use <code><a href="../Classes/Span.html#/s:7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp">Span.trafficIncidentIndexes</a></code> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans.
Also, an incident can take some place out of the built route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrafficIncidentOnRouteC6impactAA0bC6ImpactOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/impact"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC6impactAA0bC6ImpactOvp">impact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The impact of the incident.
The value is <code><a href="../Enums/TrafficIncidentImpact.html#/s:7heresdk21TrafficIncidentImpactO7unknownyA2CmF">TrafficIncidentImpact.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
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
<a name="/s:7heresdk22TrafficIncidentOnRouteC4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The category of the incident.
The value is <code><a href="../Enums/TrafficIncidentType.html#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">TrafficIncidentType.unknown</a></code> if it hasn’t been provided by the traffic incidents supplier.</p>
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
<a name="/s:7heresdk22TrafficIncidentOnRouteC11descriptionAA13LocalizedTextVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC11descriptionAA13LocalizedTextVvp">description</a>
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
always an empty string is returned. This does not apply when using the <code><a href="sdk-for-ios-explore-api-reference-..-classes-trafficengine">TrafficEngine</a></code>.</p>
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
<a name="/s:7heresdk22TrafficIncidentOnRouteC9startTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startTime"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC9startTime10Foundation4DateVSgvp">startTime</a>
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
<a name="/s:7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endTime"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp">endTime</a>
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
<a name="/s:7heresdk22TrafficIncidentOnRouteC2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique current identifier for a traffic incident.
The identifier can be changed by the backend due to some events, e.g. changing of
<code><a href="../Classes/TrafficIncidentOnRoute.html#/s:7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp">endTime</a></code>. This field will be empty for <code>OfflineRouting</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var id: String? { get }</code></pre>
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

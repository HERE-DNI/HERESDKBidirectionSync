---
title: "TrafficOptimizationMode Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-trafficoptimizationmode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficOptimizationMode.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficOptimizationMode"></a>
<a title="TrafficOptimizationMode Enumeration Reference"></a>
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
        TrafficOptimizationMode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum TrafficOptimizationMode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/timeDependent"></a>
<a class="token" href="#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">timeDependent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that
depends on the <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code> or <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code>. As a result, streets with heavy traffic
will be avoided whenever possible.
Note that this mode enables traffic-aware routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case timeDependent</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficOptimizationModeO20longTermClosuresOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/longTermClosuresOnly"></a>
<a class="token" href="#/s:7heresdk23TrafficOptimizationModeO20longTermClosuresOnlyyA2CmF">longTermClosuresOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Only long-term road closures are taken into account. Both <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code>
and <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code> are ignored, and the route will be shaped disregarding all
the available current and historical traffic information, except long-term road closures.
Note that this mode disables traffic-aware routing regardless of other settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case longTermClosuresOnly</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficOptimizationModeO8disabledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/disabled"></a>
<a class="token" href="#/s:7heresdk23TrafficOptimizationModeO8disabledyA2CmF">disabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic optimization is completely disabled, including long-term road closures. Both <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code>
and <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code> are ignored, and the route will be shaped disregarding all
the available current and historical traffic information. Note that seasonal closures are not excluded. To exclude seasonal closures,
use <code><a href="../Enums/RoadFeatures.html#/s:7heresdk12RoadFeaturesO15seasonalClosureyA2CmF">RoadFeatures.seasonalClosure</a></code>.
Note that this mode disables traffic-aware routing regardless of other settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case disabled</code></pre>
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

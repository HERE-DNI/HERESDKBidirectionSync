---
title: "TrafficOptimizationMode"
slug: "sdk-for-ios-navigate-api-reference-enums-trafficoptimizationmode"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficOptimizationMode"></a>
<a title="TrafficOptimizationMode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        TrafficOptimizationMode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficOptimizationMode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficOptimizationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">timeDependent</span></code></pre>
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
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">longTermClosuresOnly</span></code></pre>
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
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">disabled</span></code></pre>
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

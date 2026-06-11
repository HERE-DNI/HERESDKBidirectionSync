---
title: "sdk-for-ios-navigate-api-reference-structs-indoorrouteoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-indoorrouteoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/IndoorRouteOptions"></a>
<a title="IndoorRouteOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        IndoorRouteOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorRouteOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">IndoorRouteOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how an indoor route should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRouteOptionsV05routeD0AA0cD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk18IndoorRouteOptionsV05routeD0AA0cD0Vvp">routeOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the common route calculation options.</p>
<p><strong>Note:</strong> Currently, only <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> parameter is
utilized for indoor route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeoptions">RouteOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRouteOptionsV13transportModeAA014VenueTransportF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transportMode"></a>
<a class="token" href="#/s:7heresdk18IndoorRouteOptionsV13transportModeAA014VenueTransportF0Ovp">transportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The transport mode for route calculation.</p>
<p><strong>Note:</strong> Indoor route sections of the resulting route will always be
<code><a href="../Enums/VenueTransportMode.html#/s:7heresdk18VenueTransportModeO10pedestrianyA2CmF">VenueTransportMode.pedestrian</a></code> in the current implementation.
This option will affect only outdoor route sections.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRouteOptionsV015indoorAvoidanceD0AA0bfD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorAvoidanceOptions"></a>
<a class="token" href="#/s:7heresdk18IndoorRouteOptionsV015indoorAvoidanceD0AA0bfD0Vvp">indoorAvoidanceOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify restrictions for indoor route calculations. By default
no restrictions are applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">indoorAvoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRouteOptionsV22speedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk18IndoorRouteOptionsV22speedInMetersPerSecondSdvp">speedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the speed that will be used by the service as the speed
for <code><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></code> in meters per second.
It influences the duration of segments along the route.
The default speed is 1 meter per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRouteOptionsV05routeD013transportMode015indoorAvoidanceD022speedInMetersPerSecondAcA0cD0V_AA014VenueTransportG0OAA0biD0VSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:transportMode:indoorAvoidanceOptions:speedInMetersPerSecond:)"></a>
<a class="token" href="#/s:7heresdk18IndoorRouteOptionsV05routeD013transportMode015indoorAvoidanceD022speedInMetersPerSecondAcA0cD0V_AA014VenueTransportG0OAA0biD0VSdtcfc">init(routeOptions:<wbr/>transportMode:<wbr/>indoorAvoidanceOptions:<wbr/>speedInMetersPerSecond:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an object and assign default values for route options.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>routeOptions: Specifies the common route calculation options.</li>
</ul>
<p><strong>Note:</strong> Currently, only <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> parameter is
  utilized for indoor route calculation.</p>
<ul>
<li>transportMode: The transport mode for route calculation.</li>
</ul>
<p><strong>Note:</strong> Indoor route sections of the resulting route will always be
  <code><a href="../Enums/VenueTransportMode.html#/s:7heresdk18VenueTransportModeO10pedestrianyA2CmF">VenueTransportMode.pedestrian</a></code> in the current implementation.
  This option will affect only outdoor route sections.</p>
<ul>
<li>indoorAvoidanceOptions: Options to specify restrictions for indoor route calculations. By default
no restrictions are applied.</li>
<li>speedInMetersPerSecond: Specifies the speed that will be used by the service as the speed
for <code><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></code> in meters per second.
It influences the duration of segments along the route.
The default speed is 1 meter per second.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeoptions">RouteOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">(),</span> <span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></span><span class="o">.</span><span class="n">pedestrian</span><span class="p">,</span> <span class="nv">indoorAvoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a></span><span class="p">(),</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">)</span></code></pre>
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

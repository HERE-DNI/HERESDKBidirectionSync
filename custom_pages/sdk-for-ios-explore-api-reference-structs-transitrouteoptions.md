---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-transitrouteoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TransitRouteOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitRouteOptions"></a>
<a title="TransitRouteOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TransitRouteOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransitRouteOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitRouteOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a public transit route should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV13departureTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/departureTime"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV13departureTime10Foundation4DateVSgvp">departureTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional time when travel is expected to start.
If it is not specified, it is set to the current time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">departureTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV11arrivalTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalTime"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV11arrivalTime10Foundation4DateVSgvp">arrivalTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional time when travel is expected to end.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">arrivalTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV12alternativess5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/alternatives"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV12alternativess5Int32Vvp">alternatives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of alternative routes to return aside from the optimal route.
The provided value must be in the range [0, 6].
By default, it is 0 and only one route is calculated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">alternatives</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV7changess5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/changes"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV7changess5Int32VSgvp">changes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum number of changes or transfers allowed in a route.
When it is not set, unlimited number of changes is permitted.
The provided value must be in the range [0, 6].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">changes</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/modeFilter"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp">modeFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines inclusion or exclusion of transit modes for route calculation.
By default, the inclusion mode is used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">modeFilter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transitmodefilter">TransitModeFilter</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV5modesSayAA0B4ModeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/modes"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV5modesSayAA0B4ModeOGvp">modes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This list is used to determine which transit modes should be used for route calculation,
<code><a href="../Structs/TransitRouteOptions.html#/s:7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp">TransitRouteOptions.modeFilter</a></code> specifies whether this list is an inclusion or an exclusion.
For example, specifying subway and bus transit modes with the include filter, returns only subway
and bus transit modes, and with the exclude filter, returns all the transit modes except subway
and bus. When not set, all the supported transit modes are permitted.
By default, this list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">modes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transitmode">TransitMode</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV32pedestrianSpeedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pedestrianSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV32pedestrianSpeedInMetersPerSecondSdvp">pedestrianSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Walking speed in meters per second. Influences the duration of walking segments from origin to a station,
from a station to destination and in-between the stations (e.g. if transfer is needed).
The provided value must be in the range [0.5, 2.0].
The default value is 1.0 mps.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pedestrianSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV29pedestrianMaxDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pedestrianMaxDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV29pedestrianMaxDistanceInMeterss5Int32Vvp">pedestrianMaxDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
The provided value must be in the range [0, 6000].
The default value is 2000 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pedestrianMaxDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV04textD0AA0c4TextD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV04textD0AA0c4TextD0Vvp">textOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Customize textual content returned from the route calculation, such
as localization, format, and unit system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routetextoptions">RouteTextOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV13departureTime07arrivalF012alternatives7changes10modeFilter5modes32pedestrianSpeedInMetersPerSecond0m11MaxDistanceoP004textD0AC10Foundation4DateVSg_APs5Int32VARSgAA0b4ModeK0OSayAA0bY0OGSdArA0c4TextD0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(departureTime:arrivalTime:alternatives:changes:modeFilter:modes:pedestrianSpeedInMetersPerSecond:pedestrianMaxDistanceInMeters:textOptions:)"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV13departureTime07arrivalF012alternatives7changes10modeFilter5modes32pedestrianSpeedInMetersPerSecond0m11MaxDistanceoP004textD0AC10Foundation4DateVSg_APs5Int32VARSgAA0b4ModeK0OSayAA0bY0OGSdArA0c4TextD0Vtcfc">init(departureTime:<wbr/>arrivalTime:<wbr/>alternatives:<wbr/>changes:<wbr/>modeFilter:<wbr/>modes:<wbr/>pedestrianSpeedInMetersPerSecond:<wbr/>pedestrianMaxDistanceInMeters:<wbr/>textOptions:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">departureTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">arrivalTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">alternatives</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">changes</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">modeFilter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transitmodefilter">TransitModeFilter</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transitmodefilter">TransitModeFilter</a></span><span class="o">.</span><span class="n">include</span><span class="p">,</span> <span class="nv">modes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transitmode">TransitMode</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">pedestrianSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span> <span class="nv">pedestrianMaxDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">2000</span><span class="p">,</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routetextoptions">RouteTextOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routetextoptions">RouteTextOptions</a></span><span class="p">())</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TransitRouteOptionsV33fromDefaultParameterConfigurationACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromDefaultParameterConfiguration()"></a>
<a class="token" href="#/s:7heresdk19TransitRouteOptionsV33fromDefaultParameterConfigurationACyFZ">fromDefaultParameterConfiguration()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns TransitRouteOptions instance with default values used in SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromDefaultParameterConfiguration</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">TransitRouteOptions</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>An <code>TransitRouteOptions</code> instance with default values used in SDK.</p>
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

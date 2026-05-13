---
title: "Navigation / TrafficMergeWarningOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-trafficmergewarningoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficMergeWarningOptions"></a>
<a title="TrafficMergeWarningOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficMergeWarningOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficMergeWarningOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficMergeWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides traffic merge warning options. Set the options for filtering the traffic merge notifications.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficMergeWarningOptionsV11typesFilterSayAA0bC8RoadTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/typesFilter"></a>
<a class="token" href="#/s:7heresdk26TrafficMergeWarningOptionsV11typesFilterSayAA0bC8RoadTypeOGvp">typesFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The types of roads containing traffic which will trigger a warning when they merge with the current highway. If the list
is empty, the merging roads containing traffic are not filtered by type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">typesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trafficmergeroadtype">TrafficMergeRoadType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficMergeWarningOptionsV22enableTextNotificationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableTextNotification"></a>
<a class="token" href="#/s:7heresdk26TrafficMergeWarningOptionsV22enableTextNotificationSbvp">enableTextNotification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables the text notification emitted together with the traffic merge warner.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableTextNotification</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficMergeWarningOptionsV23warningDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warningDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk26TrafficMergeWarningOptionsV23warningDistanceInMeterss5Int32Vvp">warningDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The warning notification distance in meters applicable for traffic merge warning regardless of the timing profile.
Defaults to 1500 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">warningDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficMergeWarningOptionsV11typesFilter22enableTextNotification23warningDistanceInMetersACSayAA0bC8RoadTypeOG_Sbs5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(typesFilter:enableTextNotification:warningDistanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk26TrafficMergeWarningOptionsV11typesFilter22enableTextNotification23warningDistanceInMetersACSayAA0bC8RoadTypeOG_Sbs5Int32Vtcfc">init(typesFilter:<wbr/>enableTextNotification:<wbr/>warningDistanceInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">typesFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trafficmergeroadtype">TrafficMergeRoadType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">enableTextNotification</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">true</span><span class="p">,</span> <span class="nv">warningDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1500</span><span class="p">)</span></code></pre>
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

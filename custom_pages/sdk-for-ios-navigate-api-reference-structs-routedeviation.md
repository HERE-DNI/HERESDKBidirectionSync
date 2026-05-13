---
title: "Navigation / RouteDeviation"
slug: "sdk-for-ios-navigate-api-reference-structs-routedeviation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteDeviation"></a>
<a title="RouteDeviation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RouteDeviation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteDeviation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteDeviation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains all the relevant information on a deviation from the route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastLocationOnRoute"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp">lastLocationOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The last known location on the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastLocationOnRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV24lastTraveledSectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastTraveledSectionIndex"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV24lastTraveledSectionIndexs5Int32Vvp">lastTraveledSectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the index of the last traveled route section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV37traveledDistanceOnLastSectionInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/traveledDistanceOnLastSectionInMeters"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV37traveledDistanceOnLastSectionInMeterss5Int32Vvp">traveledDistanceOnLastSectionInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV15currentLocationAA09NavigableE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentLocation"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV15currentLocationAA09NavigableE0Vvp">currentLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV014lastLocationOnB00D20TraveledSectionIndex016traveledDistancef4LastH8InMeters07currentE0AcA09NavigableE0VSg_s5Int32VAlItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lastLocationOnRoute:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:currentLocation:)"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV014lastLocationOnB00D20TraveledSectionIndex016traveledDistancef4LastH8InMeters07currentE0AcA09NavigableE0VSg_s5Int32VAlItcfc">init(lastLocationOnRoute:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>currentLocation:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lastLocationOnRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">currentLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></span><span class="p">)</span></code></pre>
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

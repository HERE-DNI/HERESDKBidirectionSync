---
title: "AvoidBoundingBoxAreaOptions"
slug: "sdk-for-ios-explore-api-reference-structs-avoidboundingboxareaoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AvoidBoundingBoxAreaOptions"></a>
<a title="AvoidBoundingBoxAreaOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        AvoidBoundingBoxAreaOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AvoidBoundingBoxAreaOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidBoundingBoxAreaOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify rectangular shape which routes must not cross.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidBoundingBoxArea"></a>
<a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp">avoidBoundingBoxArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area of rectangular shape which routes must not cross. Strictly enforced.
<strong>Note:</strong>
Violations are reported as [sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD].
This avoidance option is not supported for <code><a href="sdk-for-ios-explore-api-reference-structs-isolineoptions">IsolineOptions</a></code>. If it is defined for isoline calculation then an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidBoundingBoxArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBoxExceptionAreas"></a>
<a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp">boundingBoxExceptionAreas</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Areas of rectangular shape to exclude from avoidance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBoxExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polygonExceptionAreas"></a>
<a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp">polygonExceptionAreas</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Areas of polygon shape to exclude from avoidance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">polygonExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/corridorExceptionAreas"></a>
<a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp">corridorExceptionAreas</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Areas of corridor shape to exclude from avoidance.
<strong>Note:</strong>
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an [sdk.routing.RoutingError.INVALID_PARAMETER] error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">corridorExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocorridor">GeoCorridor</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE008boundingD14ExceptionAreas07polygoniJ008corridoriJ0AcA03GeoD0V_SayAIGSayAA0M7PolygonVGSayAA0M8CorridorVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(avoidBoundingBoxArea:boundingBoxExceptionAreas:polygonExceptionAreas:corridorExceptionAreas:)"></a>
<a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE008boundingD14ExceptionAreas07polygoniJ008corridoriJ0AcA03GeoD0V_SayAIGSayAA0M7PolygonVGSayAA0M8CorridorVGtcfc">init(avoidBoundingBoxArea:<wbr/>boundingBoxExceptionAreas:<wbr/>polygonExceptionAreas:<wbr/>corridorExceptionAreas:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">avoidBoundingBoxArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">boundingBoxExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">polygonExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">corridorExceptionAreas</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocorridor">GeoCorridor</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

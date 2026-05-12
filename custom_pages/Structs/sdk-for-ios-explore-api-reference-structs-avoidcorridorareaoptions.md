---
title: "AvoidCorridorAreaOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-avoidcorridorareaoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AvoidCorridorAreaOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/AvoidCorridorAreaOptions"></a>
<a title="AvoidCorridorAreaOptions Structure Reference"></a>
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
        AvoidCorridorAreaOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct AvoidCorridorAreaOptions : Hashable</code></pre>
</div>
</div>
<p>Area of corridor shape which routes must not cross and exceptions for this area.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AvoidCorridorAreaOptionsV05avoidcD0AA03GeoC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidCorridorArea"></a>
<a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV05avoidcD0AA03GeoC0Vvp">avoidCorridorArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area of corridor shape which routes must not cross. Strictly enforced.
Violations are reported as <code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">SectionNoticeCode.violatedBlockedRoad</a></code>.
<strong>Note:</strong>
This avoidance option is not supported for <code><a href="../Structs/IsolineOptions.html">IsolineOptions</a></code>. If it is defined for isoline calculation then an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an [sdk.routing.RoutingError.INVALID_PARAMETER] error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var avoidCorridorArea: GeoCorridor</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AvoidCorridorAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBoxExceptionAreas"></a>
<a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp">boundingBoxExceptionAreas</a>
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
<pre><code>public var boundingBoxExceptionAreas: [GeoBox]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AvoidCorridorAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polygonExceptionAreas"></a>
<a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp">polygonExceptionAreas</a>
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
<pre><code>public var polygonExceptionAreas: [GeoPolygon]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AvoidCorridorAreaOptionsV22corridorExceptionAreasSayAA03GeoC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/corridorExceptionAreas"></a>
<a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV22corridorExceptionAreasSayAA03GeoC0VGvp">corridorExceptionAreas</a>
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
<pre><code>public var corridorExceptionAreas: [GeoCorridor]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AvoidCorridorAreaOptionsV05avoidcD025boundingBoxExceptionAreas07polygoniJ008corridoriJ0AcA03GeoC0V_SayAA0mH0VGSayAA0M7PolygonVGSayAIGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(avoidCorridorArea:boundingBoxExceptionAreas:polygonExceptionAreas:corridorExceptionAreas:)"></a>
<a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV05avoidcD025boundingBoxExceptionAreas07polygoniJ008corridoriJ0AcA03GeoC0V_SayAA0mH0VGSayAA0M7PolygonVGSayAIGtcfc">init(avoidCorridorArea:<wbr/>boundingBoxExceptionAreas:<wbr/>polygonExceptionAreas:<wbr/>corridorExceptionAreas:<wbr/>)</a>
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
<pre><code>public init(avoidCorridorArea: GeoCorridor, boundingBoxExceptionAreas: [GeoBox] = [], polygonExceptionAreas: [GeoPolygon] = [], corridorExceptionAreas: [GeoCorridor] = [])</code></pre>
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

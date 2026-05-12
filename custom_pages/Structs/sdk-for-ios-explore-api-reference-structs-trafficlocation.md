---
title: "TrafficLocation Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-trafficlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficLocation.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficLocation"></a>
<a title="TrafficLocation Structure Reference"></a>
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
<a href="../Traffic.html">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficLocation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct TrafficLocation : Hashable</code></pre>
</div>
</div>
<p>The location reference to the traffic incident.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV11descriptionSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV11descriptionSSvp">description</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The description of the location.
In general, the language can’t be bound to the description.
Usually, the language is one of the local languages of the incident region.
Note: A localizable description of the incident is part of <code>description</code>.
This description describes only the location where the incident occurred.
Defaults to an empty string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var description: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV8polylineAA11GeoPolylineVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polyline"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV8polylineAA11GeoPolylineVvp">polyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The polyline representing the traffic entity shape.
The current field contains a continuous polyline with no gaps between geo-coordinates.
All others following the gap are present in the <code>additional_polylines</code> field.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var polyline: GeoPolyline</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV19additionalPolylinesSayAA11GeoPolylineVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/additionalPolylines"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV19additionalPolylinesSayAA11GeoPolylineVGvp">additionalPolylines</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of polylines that were not included in continuous polyline.
Use this to fill any gaps in the continuous polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var additionalPolylines: [GeoPolyline]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV14lengthInMeterss5Int32Vvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The affected road length in meters.
The length can be 0 only if the incident supplier has provided incomplete data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var lengthInMeters: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV11description8polyline19additionalPolylines14lengthInMetersACSS_AA11GeoPolylineVSayAIGs5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(description:polyline:additionalPolylines:lengthInMeters:)"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV11description8polyline19additionalPolylines14lengthInMetersACSS_AA11GeoPolylineVSayAIGs5Int32Vtcfc">init(description:<wbr/>polyline:<wbr/>additionalPolylines:<wbr/>lengthInMeters:<wbr/>)</a>
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
<pre><code>public init(description: String = "", polyline: GeoPolyline, additionalPolylines: [GeoPolyline], lengthInMeters: Int32)</code></pre>
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

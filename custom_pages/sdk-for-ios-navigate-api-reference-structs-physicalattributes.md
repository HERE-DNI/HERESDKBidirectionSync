---
title: "sdk-for-ios-navigate-api-reference-structs-physicalattributes"
slug: "sdk-for-ios-navigate-api-reference-structs-physicalattributes"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PhysicalAttributes"></a>
<a title="PhysicalAttributes Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>
<img alt="" id="carat" src="/carat.png"/>
        PhysicalAttributes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PhysicalAttributes</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PhysicalAttributes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Physical attributes of the segment.</p>
<p><strong><em>Note</em></strong> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV10isDirtRoadSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDirtRoad"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV10isDirtRoadSbvp">isDirtRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether the navigable segment is paved.
Paved is primarily used for map display and routing by assigning
higher penalties to unpaved roads.
Paved roads are made of concrete, asphalt, cobblestone or brick.
Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDirtRoad</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV8isTunnelSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTunnel"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV8isTunnelSbvp">isTunnel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies an enclosed (on all sides) passageway through or under an obstruction.
This attribute can be used for display or route guidance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTunnel</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV8isBridgeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBridge"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV8isBridgeSbvp">isBridge</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a structure that allows a road, railway, or walkway
to pass over another road, railway, waterway, or valley serving
map display and route guidance functionalities.
Bridge is published on segments that represent significant
bridges and/or overpasses; elevated roads are not published as bridge.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isBridge</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV9isPrivateSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPrivate"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV9isPrivateSbvp">isPrivate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Private identifies roads that are not maintained by an organization
responsible for maintenance of public roads.
Allows for unique cartographic representation of roads that restrict public use.
May be used to avoid routing through a private road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPrivate</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV12isRoundaboutSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRoundabout"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV12isRoundaboutSbvp">isRoundabout</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the presence of a roundabout.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRoundabout</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV19isMultiplyDigitizedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isMultiplyDigitized"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV19isMultiplyDigitizedSbvp">isMultiplyDigitized</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies separately digitised roads, i.e., roads that are digitised with one line per
direction of traffic instead of one line per road.
It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus
lane) are located between the separately digitised opposing roadbeds if driver perception
remains unchanged.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isMultiplyDigitized</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV7dividerAA11RoadDividerOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/divider"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV7dividerAA11RoadDividerOSgvp">divider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the presence of a road divider.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">divider</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roaddivider">RoadDivider</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV11isBoatFerrySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBoatFerry"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV11isBoatFerrySbvp">isBoatFerry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a generalised route of a boat ferry for passengers or vehicles over water.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isBoatFerry</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV11isRailFerrySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRailFerry"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV11isRailFerrySbvp">isRailFerry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied
on a segment that represent a ferry route for vehicles over rail such as: a route for
ferrying passengers over rail, if destination is not accessible by the road network or
prohibits the use of automobiles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRailFerry</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV10isDirtRoad0D6Tunnel0D6Bridge0D7Private0D10Roundabout0D17MultiplyDigitized7divider0D9BoatFerry0d4RailO0ACSb_S5bAA0F7DividerOSgS2btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isDirtRoad:isTunnel:isBridge:isPrivate:isRoundabout:isMultiplyDigitized:divider:isBoatFerry:isRailFerry:)"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV10isDirtRoad0D6Tunnel0D6Bridge0D7Private0D10Roundabout0D17MultiplyDigitized7divider0D9BoatFerry0d4RailO0ACSb_S5bAA0F7DividerOSgS2btcfc">init(isDirtRoad:<wbr/>isTunnel:<wbr/>isBridge:<wbr/>isPrivate:<wbr/>isRoundabout:<wbr/>isMultiplyDigitized:<wbr/>divider:<wbr/>isBoatFerry:<wbr/>isRailFerry:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isDirtRoad</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isTunnel</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isBridge</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isPrivate</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isRoundabout</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isMultiplyDigitized</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">divider</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roaddivider">RoadDivider</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isBoatFerry</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isRailFerry</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

---
title: "RoadAttributes"
slug: "sdk-for-ios-navigate-api-reference-structs-roadattributes"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadAttributes"></a>
<a title="RoadAttributes Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        RoadAttributes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadAttributes</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadAttributes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Road attributes, including usage and physical characteristics.
Note that a road can have more than one attribute at the same time.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV06isDirtB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDirtRoad"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV06isDirtB0Sbvp">isDirtRoad</a>
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
<a name="/s:7heresdk14RoadAttributesV8isTunnelSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTunnel"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV8isTunnelSbvp">isTunnel</a>
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
<a name="/s:7heresdk14RoadAttributesV8isBridgeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBridge"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV8isBridgeSbvp">isBridge</a>
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
<a name="/s:7heresdk14RoadAttributesV6isRampSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRamp"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV6isRampSbvp">isRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Range is a ramp: connects roads that do not intersect at grade.
Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
and for route guidance when determining if sign text should be used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRamp</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV18isControlledAccessSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isControlledAccess"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV18isControlledAccessSbvp">isControlledAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controlled access roads are roads with limited entrances and exits
that allow uninterrupted high-speed traffic flow.
For example, the Interstate/Freeway network in the United States or
the Motorway network in Europe.
Controlled Access can be used for map display, avoidance of freeway/motorway,
publishing speed limits, and route guidance timing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV9isPrivateSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPrivate"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV9isPrivateSbvp">isPrivate</a>
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
<a name="/s:7heresdk14RoadAttributesV11isNoThroughSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isNoThrough"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV11isNoThroughSbvp">isNoThrough</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isNoThrough</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV9isTollwaySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTollway"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV9isTollwaySbvp">isTollway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a road for which a fee must be paid to use the road.
Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
Tollway is flagged on roads that require a fee for traversal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTollway</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV09isDividedB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDividedRoad"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV09isDividedB0Sbvp">isDividedRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if there is a physical structure or painted road marking intended to legally
prohibit left turns in right-side driving countries, right turns in left-side driving
countries, and U-turns at divided intersections or in the middle of divided segments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDividedRoad</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRightDrivingSide"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp">isRightDrivingSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.
For example, in New York it is always <code>true</code> and in London always <code>false</code> as the United Kingdom is
a left-hand driving country.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRightDrivingSide</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV12isRoundaboutSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRoundabout"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV12isRoundaboutSbvp">isRoundabout</a>
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
<a name="/s:7heresdk14RoadAttributesV13isBuiltUpAreaSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBuiltUpArea"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV13isBuiltUpAreaSbvp">isBuiltUpArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the navigable segment is a built up area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isBuiltUpArea</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoadAttributesV06isDirtB00D6Tunnel0D6Bridge0D4Ramp0D16ControlledAccess0D7Private0D9NoThrough0D7Tollway0d7DividedB00D16RightDrivingSide0D10Roundabout0D11BuiltUpAreaACSb_S11btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isDirtRoad:isTunnel:isBridge:isRamp:isControlledAccess:isPrivate:isNoThrough:isTollway:isDividedRoad:isRightDrivingSide:isRoundabout:isBuiltUpArea:)"></a>
<a class="token" href="#/s:7heresdk14RoadAttributesV06isDirtB00D6Tunnel0D6Bridge0D4Ramp0D16ControlledAccess0D7Private0D9NoThrough0D7Tollway0d7DividedB00D16RightDrivingSide0D10Roundabout0D11BuiltUpAreaACSb_S11btcfc">init(isDirtRoad:<wbr/>isTunnel:<wbr/>isBridge:<wbr/>isRamp:<wbr/>isControlledAccess:<wbr/>isPrivate:<wbr/>isNoThrough:<wbr/>isTollway:<wbr/>isDividedRoad:<wbr/>isRightDrivingSide:<wbr/>isRoundabout:<wbr/>isBuiltUpArea:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isDirtRoad</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isTunnel</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isBridge</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isRamp</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isPrivate</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isNoThrough</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isTollway</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isDividedRoad</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isRightDrivingSide</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isRoundabout</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isBuiltUpArea</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
} </HTMLBlock>

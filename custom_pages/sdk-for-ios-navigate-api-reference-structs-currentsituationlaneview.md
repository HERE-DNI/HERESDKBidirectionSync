---
title: "CurrentSituationLaneView"
slug: "sdk-for-ios-navigate-api-reference-structs-currentsituationlaneview"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CurrentSituationLaneView"></a>
<a title="CurrentSituationLaneView Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        CurrentSituationLaneView Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CurrentSituationLaneView</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CurrentSituationLaneView</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides current situation lane assistance view
information for the street at the current position of a single lane.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/access"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp">access</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates which vehicle types can access this lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-laneaccess">LaneAccess</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directionCategory"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp">directionCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates towards which directions this lane leads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directionCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanedirectioncategory">LaneDirectionCategory</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates this lane’s properties.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanetype">LaneType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/laneMarkings"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp">laneMarkings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the lane markings between the lanes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">laneMarkings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanemarkings">LaneMarkings</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directions"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp">directions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates which lane directions are available for this lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directionsOnRoute"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp">directionsOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates which lane directions are on the route. Following those directions keeps the driver on the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directionsOnRoute</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV6access17directionCategory4type12laneMarkings10directions0L7OnRouteAcA0D6AccessV_AA0d9DirectionH0VAA0D4TypeVAA0dK0VSayAA0dP0OGATtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(access:directionCategory:type:laneMarkings:directions:directionsOnRoute:)"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV6access17directionCategory4type12laneMarkings10directions0L7OnRouteAcA0D6AccessV_AA0d9DirectionH0VAA0D4TypeVAA0dK0VSayAA0dP0OGATtcfc">init(access:<wbr/>directionCategory:<wbr/>type:<wbr/>laneMarkings:<wbr/>directions:<wbr/>directionsOnRoute:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-laneaccess">LaneAccess</a></span><span class="p">,</span> <span class="nv">directionCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanedirectioncategory">LaneDirectionCategory</a></span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanetype">LaneType</a></span><span class="p">,</span> <span class="nv">laneMarkings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanemarkings">LaneMarkings</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanemarkings">LaneMarkings</a></span><span class="p">(),</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">directionsOnRoute</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-lanedirection">LaneDirection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

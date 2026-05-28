---
title: "Navigation / Lane"
slug: "sdk-for-ios-navigate-api-reference-structs-lane"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Lane"></a>
<a title="Lane Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Lane Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Lane</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Lane</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides information for a lane.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV4typeAA0B4TypeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk4LaneV4typeAA0B4TypeVvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the properties of this lane.
For example, it indicates whether parking is allowed, if it is an acceleration lane,
an express lane, or other attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanetype">LaneType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV19recommendationStateAA0b14RecommendationD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/recommendationState"></a>
<a class="token" href="#/s:7heresdk4LaneV19recommendationStateAA0b14RecommendationD0Ovp">recommendationState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if this lane leads to the upcoming maneuvers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">recommendationState</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanerecommendationstate">LaneRecommendationState</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV6accessAA0B6AccessVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/access"></a>
<a class="token" href="#/s:7heresdk4LaneV6accessAA0B6AccessVvp">access</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-laneaccess">LaneAccess</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV12laneMarkingsAA0bD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/laneMarkings"></a>
<a class="token" href="#/s:7heresdk4LaneV12laneMarkingsAA0bD0Vvp">laneMarkings</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">laneMarkings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanemarkings">LaneMarkings</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV10directionsSayAA0B9DirectionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directions"></a>
<a class="token" href="#/s:7heresdk4LaneV10directionsSayAA0B9DirectionOGvp">directions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates all the lane directions that are available for this lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanedirection">LaneDirection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV17directionsOnRouteSayAA0B9DirectionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directionsOnRoute"></a>
<a class="token" href="#/s:7heresdk4LaneV17directionsOnRouteSayAA0B9DirectionOGvp">directionsOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the lane directions that are on the route.
Following these directions keeps the driver on the route.
This is a subset of <code><a href="../Structs/Lane.html#/s:7heresdk4LaneV10directionsSayAA0B9DirectionOGvp">Lane.directions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directionsOnRoute</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanedirection">LaneDirection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV4type19recommendationState6access12laneMarkings10directions0I7OnRouteAcA0B4TypeV_AA0b14RecommendationE0OAA0B6AccessVAA0bH0VSayAA0B9DirectionOGATtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:recommendationState:access:laneMarkings:directions:directionsOnRoute:)"></a>
<a class="token" href="#/s:7heresdk4LaneV4type19recommendationState6access12laneMarkings10directions0I7OnRouteAcA0B4TypeV_AA0b14RecommendationE0OAA0B6AccessVAA0bH0VSayAA0B9DirectionOGATtcfc">init(type:<wbr/>recommendationState:<wbr/>access:<wbr/>laneMarkings:<wbr/>directions:<wbr/>directionsOnRoute:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanetype">LaneType</a></span><span class="p">,</span> <span class="nv">recommendationState</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanerecommendationstate">LaneRecommendationState</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanerecommendationstate">LaneRecommendationState</a></span><span class="o">.</span><span class="n">notRecommended</span><span class="p">,</span> <span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-laneaccess">LaneAccess</a></span><span class="p">,</span> <span class="nv">laneMarkings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanemarkings">LaneMarkings</a></span><span class="p">,</span> <span class="nv">directions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanedirection">LaneDirection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">directionsOnRoute</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-lanedirection">LaneDirection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

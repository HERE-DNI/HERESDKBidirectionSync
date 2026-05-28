---
title: "Navigation / LaneAccess"
slug: "sdk-for-ios-navigate-api-reference-structs-laneaccess"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneAccess"></a>
<a title="LaneAccess Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LaneAccess Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneAccess</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneAccess</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct which identifies the vehicle type(s) allowed to
access a lane.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV11automobilesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/automobiles"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV11automobilesSbvp">automobiles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">automobiles</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV5busesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/buses"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV5busesSbvp">buses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Buses that are used for public transportation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">buses</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV5taxisSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/taxis"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV5taxisSbvp">taxis</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
along with their driver, to carry passengers to any specified destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">taxis</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV8carpoolsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carpools"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV8carpoolsSbvp">carpools</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the sharing of car journeys so that more than one person travels in a car, and
prevents the need for others to have to drive to a location themselves.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">carpools</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV11pedestriansSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pedestrians"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV11pedestriansSbvp">pedestrians</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Persons traveling on foot, whether walking or running.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pedestrians</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV6trucksSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trucks"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV6trucksSbvp">trucks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Large vehicles that range from medium to heavy duty trucks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trucks</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV14throughTrafficSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/throughTraffic"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV14throughTrafficSbvp">throughTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
allowed to access roads that have traffic restrictions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">throughTraffic</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV16deliveryVehiclesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/deliveryVehicles"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV16deliveryVehiclesSbvp">deliveryVehicles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Delivery <code><a href="../Structs/LaneAccess.html#/s:7heresdk10LaneAccessV6trucksSbvp">LaneAccess.trucks</a></code> that are permitted to enter the city proper
to unload goods at businesses.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">deliveryVehicles</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV17emergencyVehiclesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/emergencyVehicles"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV17emergencyVehiclesSbvp">emergencyVehicles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Any vehicle that is designated and authorized to respond to an emergency in a
life-threatening situation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">emergencyVehicles</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV11motorcyclesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/motorcycles"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV11motorcyclesSbvp">motorcycles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
motorcycles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">motorcycles</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV11automobiles5buses5taxis8carpools11pedestrians6trucks14throughTraffic16deliveryVehicles09emergencyM011motorcyclesACSb_S9btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(automobiles:buses:taxis:carpools:pedestrians:trucks:throughTraffic:deliveryVehicles:emergencyVehicles:motorcycles:)"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV11automobiles5buses5taxis8carpools11pedestrians6trucks14throughTraffic16deliveryVehicles09emergencyM011motorcyclesACSb_S9btcfc">init(automobiles:<wbr/>buses:<wbr/>taxis:<wbr/>carpools:<wbr/>pedestrians:<wbr/>trucks:<wbr/>throughTraffic:<wbr/>deliveryVehicles:<wbr/>emergencyVehicles:<wbr/>motorcycles:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">automobiles</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">buses</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">taxis</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">carpools</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">pedestrians</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">trucks</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">throughTraffic</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">deliveryVehicles</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">emergencyVehicles</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">motorcycles</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
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

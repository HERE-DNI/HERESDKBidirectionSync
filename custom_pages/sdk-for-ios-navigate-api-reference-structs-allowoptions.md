---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-allowoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AllowOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AllowOptions"></a>
<a title="AllowOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AllowOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AllowOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AllowOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options explicitly allowed by user for route calculations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AllowOptionsV8allowHovSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowHov"></a>
<a class="token" href="#/s:7heresdk12AllowOptionsV8allowHovSbvp">allowHov</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that specifies whether HOV lanes can be used in the route calculation.</p>
<p>A HOV (High occupancy Vehicle) lane or carpool lane is reserved for carpool usage. Carpool lane requires
a minimum number of passengers in order for the car to use the carpool lane.</p>
<p><strong>Note:</strong> Can be used with <code>RoutingOptions.transport_specification.vehicle_specification.occupancy</code> to specify the number of occupants
in the vehicle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowHov</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AllowOptionsV8allowHotSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowHot"></a>
<a class="token" href="#/s:7heresdk12AllowOptionsV8allowHotSbvp">allowHot</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that specifies whether HOT lanes can be used in the calculation.</p>
<p>HOT (high-occupancy toll) lanes are HOV lanes where vehicles that do not qualify as high-occupancy are allowed to pass by paying a toll.</p>
<p><strong>Note:</strong> Can be used with <code>RoutingOptions.transport_specification.vehicle_specification.occupancy</code> to specify the number of occupants
in the vehicle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowHot</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AllowOptionsV8allowHov0D3HotACSb_Sbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(allowHov:allowHot:)"></a>
<a class="token" href="#/s:7heresdk12AllowOptionsV8allowHov0D3HotACSb_Sbtcfc">init(allowHov:<wbr/>allowHot:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>allowHov: A flag that specifies whether HOV lanes can be used in the route calculation.</li>
</ul>
<p>A HOV (High occupancy Vehicle) lane or carpool lane is reserved for carpool usage. Carpool lane requires
  a minimum number of passengers in order for the car to use the carpool lane.</p>
<p><strong>Note:</strong> Can be used with <code>RoutingOptions.transport_specification.vehicle_specification.occupancy</code> to specify the number of occupants
  in the vehicle.</p>
<ul>
<li>allowHot: A flag that specifies whether HOT lanes can be used in the calculation.</li>
</ul>
<p>HOT (high-occupancy toll) lanes are HOV lanes where vehicles that do not qualify as high-occupancy are allowed to pass by paying a toll.</p>
<p><strong>Note:</strong> Can be used with <code>RoutingOptions.transport_specification.vehicle_specification.occupancy</code> to specify the number of occupants
  in the vehicle.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">allowHov</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">allowHot</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

</div>
`
}</HTMLBlock>

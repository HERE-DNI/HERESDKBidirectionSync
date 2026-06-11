---
title: "sdk-for-ios-navigate-api-reference-structs-transitdeparture"
slug: "sdk-for-ios-navigate-api-reference-structs-transitdeparture"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitDeparture"></a>
<a title="TransitDeparture Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        TransitDeparture Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransitDeparture</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitDeparture</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This struct holds the transit departure or arrival information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/place"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp">place</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The departure or arrival place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeplace">RoutePlace</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV4time10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/time"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV4time10Foundation4DateVSgvp">time</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Expected departure or arrival time of the event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">time</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5delays5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/delay"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5delays5Int32VSgvp">delay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The accumulated delay in seconds from the scheduled time of the event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">delay</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/status"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp">status</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Status of the departure.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transitdeparturestatus">TransitDepartureStatus</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(place:time:delay:status:)"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc">init(place:<wbr/>time:<wbr/>delay:<wbr/>status:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeplace">RoutePlace</a></span><span class="p">,</span> <span class="nv">time</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">delay</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transitdeparturestatus">TransitDepartureStatus</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

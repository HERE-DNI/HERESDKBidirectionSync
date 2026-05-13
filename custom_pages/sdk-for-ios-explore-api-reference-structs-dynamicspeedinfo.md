---
title: "DynamicSpeedInfo Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-dynamicspeedinfo"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- DynamicSpeedInfo.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/DynamicSpeedInfo"></a>
<a title="DynamicSpeedInfo Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DynamicSpeedInfo Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct DynamicSpeedInfo : Hashable</code></pre>
</div>
</div>
<p>Provides estimated speed information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">baseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed in meters per second without taking traffic into consideration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var baseSpeedInMetersPerSecond: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp">trafficSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed in meters per second considering traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var trafficSpeedInMetersPerSecond: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/turnTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp">turnTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time it takes to make a turn, represented in seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var turnTimeInSeconds: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(baseSpeedInMetersPerSecond:trafficSpeedInMetersPerSecond:turnTimeInSeconds:)"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc">init(baseSpeedInMetersPerSecond:<wbr/>trafficSpeedInMetersPerSecond:<wbr/>turnTimeInSeconds:<wbr/>)</a>
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
<pre><code>public init(baseSpeedInMetersPerSecond: Double, trafficSpeedInMetersPerSecond: Double, turnTimeInSeconds: Int32)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateJamFactor()"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF">calculateJamFactor()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Calculates the traffic jam factor that shows the traffic condition in a numeric way.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func calculateJamFactor() -&gt; Double</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Returns calculated jam factor in the range [0.0, 10.0].
A large jamFactor value means more traffic jam in general.
Specifically, 0.0 means free traffic and 10.0 means stationary traffic.</p>
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

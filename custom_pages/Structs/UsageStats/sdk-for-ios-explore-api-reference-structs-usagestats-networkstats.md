---
title: "NetworkStats Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-usagestats-networkstats"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- NetworkStats.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/NetworkStats"></a>
<a title="NetworkStats Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Core.html">Core</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Structs/UsageStats.html">UsageStats</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        NetworkStats Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct NetworkStats</code></pre>
</div>
</div>
<p>Provides network statistics in bytes per method.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V9sentBytess6UInt64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sentBytes"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V9sentBytess6UInt64Vvp">sentBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of bytes sent over the network.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var sentBytes: UInt64</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V13receivedBytess6UInt64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/receivedBytes"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V13receivedBytess6UInt64Vvp">receivedBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of bytes received from the network.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var receivedBytes: UInt64</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V10methodCallSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/methodCall"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V10methodCallSSvp">methodCall</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name or description of the method being called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var methodCall: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V14requestCounters6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requestCounter"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V14requestCounters6UInt32Vvp">requestCounter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Amount of calls for particular family of methodCall.
methodCall in this case is considered as base request,
additional query params are ignored, all calculated as one request.
e.g. <a href="https://search.hereapi.com/someparams">https://search.hereapi.com/someparams</a> and <a href="https://search.hereapi.com/someparams2">https://search.hereapi.com/someparams2</a>
will be considered as 1 methodCall, and requestCounter is 2.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var requestCounter: UInt32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V9sentBytes08receivedF010methodCall14requestCounterAEs6UInt64V_AKSSs6UInt32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sentBytes:receivedBytes:methodCall:requestCounter:)"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V9sentBytes08receivedF010methodCall14requestCounterAEs6UInt64V_AKSSs6UInt32Vtcfc">init(sentBytes:<wbr/>receivedBytes:<wbr/>methodCall:<wbr/>requestCounter:<wbr/>)</a>
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
<pre><code>public init(sentBytes: UInt64, receivedBytes: UInt64, methodCall: String, requestCounter: UInt32)</code></pre>
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

---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-trafficflowqueryoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficFlowQueryOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficFlowQueryOptions"></a>
<a title="TrafficFlowQueryOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-traffic">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficFlowQueryOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficFlowQueryOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficFlowQueryOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify how traffic flow data should be queried.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficFlowQueryOptionsV12minJamFactorSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minJamFactor"></a>
<a class="token" href="#/s:7heresdk23TrafficFlowQueryOptionsV12minJamFactorSdSgvp">minJamFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Min jam factor value.
The jam factor is a value for the amount of traffic on the roadway. The value is between 0.0 and 10.0 (inclusive).
This will be used with <code><a href="../Structs/TrafficFlowQueryOptions.html#/s:7heresdk23TrafficFlowQueryOptionsV12maxJamFactorSdSgvp">TrafficFlowQueryOptions.maxJamFactor</a></code> to filter queried flow.
If the value is <code>nil</code>, then filtering by the min jam factor is not applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minJamFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficFlowQueryOptionsV12maxJamFactorSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxJamFactor"></a>
<a class="token" href="#/s:7heresdk23TrafficFlowQueryOptionsV12maxJamFactorSdSgvp">maxJamFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max jam factor value.
The jam factor is a value for the amount of traffic on the roadway. The value is between 0.0 and 10.0 (inclusive).
This will be used with <code><a href="../Structs/TrafficFlowQueryOptions.html#/s:7heresdk23TrafficFlowQueryOptionsV12minJamFactorSdSgvp">TrafficFlowQueryOptions.minJamFactor</a></code> to filter queried flow.
If the value is null filtering by the max jam factor is not applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxJamFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficFlowQueryOptionsV12minJamFactor03maxgH0ACSdSg_AFtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(minJamFactor:maxJamFactor:)"></a>
<a class="token" href="#/s:7heresdk23TrafficFlowQueryOptionsV12minJamFactor03maxgH0ACSdSg_AFtcfc">init(minJamFactor:<wbr/>maxJamFactor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">minJamFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxJamFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

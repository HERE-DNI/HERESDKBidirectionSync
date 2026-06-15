---
title: "DynamicRoutingEngineOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-dynamicroutingengineoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DynamicRoutingEngineOptions"></a>
<a title="DynamicRoutingEngineOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        DynamicRoutingEngineOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DynamicRoutingEngineOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DynamicRoutingEngineOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Options defining the behavior of the <code><a href="sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine">DynamicRoutingEngine</a></code>.
Both, <code>minTimeDifference</code> and <code>minTimeDifferencePercentage</code>, will be checked:
When the poll interval is reached, the smaller difference will win and
the <code><a href="sdk-for-ios-navigate-api-reference-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></code> is notified.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27DynamicRoutingEngineOptionsV27minTimeDifferencePercentageSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minTimeDifferencePercentage"></a>
<a class="token" href="#/s:7heresdk27DynamicRoutingEngineOptionsV27minTimeDifferencePercentageSdSgvp">minTimeDifferencePercentage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value is in the range of [0, 1] over the remaining (current position to next waypoint)
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt;= newRouteDuration * [min_time_difference_percentage].
A value of 0 will be treated as <code>nil</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minTimeDifferencePercentage</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27DynamicRoutingEngineOptionsV17minTimeDifferenceSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minTimeDifference"></a>
<a class="token" href="#/s:7heresdk27DynamicRoutingEngineOptionsV17minTimeDifferenceSdSgvp">minTimeDifference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The minimum time difference, before notifying the <code><a href="sdk-for-ios-navigate-api-reference-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></code>.
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt; <code>DynamicRoutingEngineOptions.minTimeDifference</code>.
A value of 0 will be treated as <code>nil</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minTimeDifference</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pollInterval"></a>
<a class="token" href="#/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">pollInterval</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The poll interval.
Zero duration triggers a route calculation with each position update.
Triggered via <code><a href="../Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF">DynamicRoutingEngine.updateCurrentLocation(...)</a></code>
Defaults to 15 minutes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pollInterval</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27DynamicRoutingEngineOptionsV27minTimeDifferencePercentage0fgH012pollIntervalACSdSg_AGSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(minTimeDifferencePercentage:minTimeDifference:pollInterval:)"></a>
<a class="token" href="#/s:7heresdk27DynamicRoutingEngineOptionsV27minTimeDifferencePercentage0fgH012pollIntervalACSdSg_AGSdtcfc">init(minTimeDifferencePercentage:<wbr/>minTimeDifference:<wbr/>pollInterval:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">minTimeDifferencePercentage</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">minTimeDifference</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">pollInterval</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">15</span> <span class="o">*</span> <span class="mi">60</span><span class="p">)</span></code></pre>
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

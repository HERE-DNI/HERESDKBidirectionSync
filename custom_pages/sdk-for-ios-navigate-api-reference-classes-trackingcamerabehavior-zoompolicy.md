---
title: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-zoompolicy"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-zoompolicy"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/ZoomPolicy"></a>
<a title="ZoomPolicy Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
<img alt="" id="carat" src="/carat.png"/>
        ZoomPolicy Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ZoomPolicy</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ZoomPolicy</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Defines zoom behavior in different policy settings.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC09makeFixedeF09zoomLevelAESd_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/makeFixedZoomPolicy(zoomLevel:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC09makeFixedeF09zoomLevelAESd_tFZ">makeFixedZoomPolicy(zoomLevel:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a zoom policy that always returns a fixed zoom level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">makeFixedZoomPolicy</span><span class="p">(</span><span class="nv">zoomLevel</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>zoomLevel</em>
</code>
</td>
<td>
<div>
<p>The constant zoom level that the policy will return.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The ZoomPolicy instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC023makeFunctionalRoadClasseF07optionsAeC0hijeF7OptionsV_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/makeFunctionalRoadClassZoomPolicy(options:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC023makeFunctionalRoadClasseF07optionsAeC0hijeF7OptionsV_tFZ">makeFunctionalRoadClassZoomPolicy(options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiates a zoom policy that selects zoom levels based on functional road class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">makeFunctionalRoadClassZoomPolicy</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">FunctionalRoadClassZoomPolicyOptions</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Configuration mapping road classes to zoom levels, including a default fallback.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The ZoomPolicy instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC014makeSpeedBasedeF07optionsAeC0hieF7OptionsV_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/makeSpeedBasedZoomPolicy(options:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC014makeSpeedBasedeF07optionsAeC0hieF7OptionsV_tFZ">makeSpeedBasedZoomPolicy(options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiates a zoom policy driven by speed thresholds defined per road classification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">makeSpeedBasedZoomPolicy</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">SpeedBasedZoomPolicyOptions</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Configuration describing the speed thresholds mapping
to road classifications.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The ZoomPolicy instance.</p>
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

---
title: "Positioning / LocationSimulatorOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-locationsimulatoroptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationSimulatorOptions"></a>
<a title="LocationSimulatorOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-positioning">Positioning</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationSimulatorOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationSimulatorOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocationSimulatorOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Options to specify how the location simulator will behave.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24LocationSimulatorOptionsV11speedFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedFactor"></a>
<a class="token" href="#/s:7heresdk24LocationSimulatorOptionsV11speedFactorSdvp">speedFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A factor to scale the speed.
Useful to speed up (or down) the simulation.
By default, the speed factor is 1.0, which is equal to the speed that one normally drives along
each route segment without taking into account any traffic-related constraints.
The default speed may vary based on the road geometry, road condition and other statistical
data.
Values above 1.0 will increase the speed, values below 1.0 will reduce the speed.
For example, a value of 2.0 will double the speed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedFactor</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24LocationSimulatorOptionsV20notificationIntervalSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/notificationInterval"></a>
<a class="token" href="#/s:7heresdk24LocationSimulatorOptionsV20notificationIntervalSdvp">notificationInterval</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interval between notifications.
Defaults to 1 second.
Note that <code>TimeInterval</code> accepts seconds as double, so 500 ms can be set as 0.5 s.
Values less than 1 ms are not acceptable and the interval is raised to this minimum in object constructors.</p>
<p>Note: This value does not affect <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationsimulator">LocationSimulator</a></code> when created with a <code><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrack">GPXTrack</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">notificationInterval</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24LocationSimulatorOptionsV11speedFactor20notificationIntervalACSd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(speedFactor:notificationInterval:)"></a>
<a class="token" href="#/s:7heresdk24LocationSimulatorOptionsV11speedFactor20notificationIntervalACSd_Sdtcfc">init(speedFactor:<wbr/>notificationInterval:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>speedFactor: A factor to scale the speed.
Useful to speed up (or down) the simulation.
By default, the speed factor is 1.0, which is equal to the speed that one normally drives along
each route segment without taking into account any traffic-related constraints.
The default speed may vary based on the road geometry, road condition and other statistical
data.
Values above 1.0 will increase the speed, values below 1.0 will reduce the speed.
For example, a value of 2.0 will double the speed.</li>
<li>notificationInterval: Interval between notifications.
Defaults to 1 second.
Note that <code>TimeInterval</code> accepts seconds as double, so 500 ms can be set as 0.5 s.
Values less than 1 ms are not acceptable and the interval is raised to this minimum in object constructors.</li>
</ul>
<p>Note: This value does not affect <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationsimulator">LocationSimulator</a></code> when created with a <code><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrack">GPXTrack</a></code>.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">speedFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span> <span class="nv">notificationInterval</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">1000</span> <span class="o">*</span> <span class="mf">0.001</span><span class="p">)</span></code></pre>
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

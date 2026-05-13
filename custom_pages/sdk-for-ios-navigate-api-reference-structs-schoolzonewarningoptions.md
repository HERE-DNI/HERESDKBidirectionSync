---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-schoolzonewarningoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SchoolZoneWarningOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SchoolZoneWarningOptions"></a>
<a title="SchoolZoneWarningOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SchoolZoneWarningOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SchoolZoneWarningOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SchoolZoneWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>School zone warning options. Set the options for configuring of school zone notifications.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SchoolZoneWarningOptionsV38filterOutInactiveTimeDependentWarningsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/filterOutInactiveTimeDependentWarnings"></a>
<a class="token" href="#/s:7heresdk24SchoolZoneWarningOptionsV38filterOutInactiveTimeDependentWarningsSbvp">filterOutInactiveTimeDependentWarnings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If set to true, all the school zone notifications which have a time restrictions
that does not apply for the current time will not be given.
If the value is false, all school zone notifications will be given regardless
of the time restrictions that they might have.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">filterOutInactiveTimeDependentWarnings</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SchoolZoneWarningOptionsV23warningDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warningDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk24SchoolZoneWarningOptionsV23warningDistanceInMeterss5Int32Vvp">warningDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The warning notification distance in meters applicable for school warning regardless of the timing profile.
Defaults to 100 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">warningDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SchoolZoneWarningOptionsV38filterOutInactiveTimeDependentWarnings23warningDistanceInMetersACSb_s5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(filterOutInactiveTimeDependentWarnings:warningDistanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk24SchoolZoneWarningOptionsV38filterOutInactiveTimeDependentWarnings23warningDistanceInMetersACSb_s5Int32Vtcfc">init(filterOutInactiveTimeDependentWarnings:<wbr/>warningDistanceInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">filterOutInactiveTimeDependentWarnings</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">warningDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">100</span><span class="p">)</span></code></pre>
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

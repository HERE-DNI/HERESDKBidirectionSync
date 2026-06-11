---
title: "sdk-for-ios-navigate-api-reference-structs-dangerzonewarning"
slug: "sdk-for-ios-navigate-api-reference-structs-dangerzonewarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DangerZoneWarning"></a>
<a title="DangerZoneWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        DangerZoneWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DangerZoneWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DangerZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents danger zones. A danger zone refers to areas where there is an increased risk of
traffic incidents. These zones are designated to alert drivers to potential hazards and encourage
safer driving behaviors. Legally, certain devices can alert you to being in a danger zone,
typically indicating the presence of a speed camera. In line with applicable law and industry
standard, these alerts are usually provided along a road within a range of 4 km on a motorway,
2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching
the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or
more speed cameras in it. The exact location of such speed cameras is not provided. Note that
danger zones are only available in selected countries, such as France.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific danger zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV02isC5StartSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isZoneStart"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV02isC5StartSbvp">isZoneStart</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag indicating whether the Danger Zone officially start in the location the user is
entering it.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isZoneStart</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceInMeters"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp">distanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance from the current location to the Danger zone.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is
ahead, then <code><a href="../Structs/DangerZoneWarning.html#/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp">DangerZoneWarning.distanceInMeters</a></code> is greater than 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV2id02isC5Start16distanceInMeters0H4TypeACs5Int32V_SbSdAA08DistanceK0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:isZoneStart:distanceInMeters:distanceType:)"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV2id02isC5Start16distanceInMeters0H4TypeACs5Int32V_SbSdAA08DistanceK0Otcfc">init(id:<wbr/>isZoneStart:<wbr/>distanceInMeters:<wbr/>distanceType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">isZoneStart</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">)</span></code></pre>
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

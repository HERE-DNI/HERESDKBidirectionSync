---
title: "LocationAccuracy"
slug: "sdk-for-ios-navigate-api-reference-enums-locationaccuracy"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationAccuracy"></a>
<a title="LocationAccuracy Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-positioning">Positioning</a>

        LocationAccuracy Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationAccuracy</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationAccuracy</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indicates the desired location accuracy, however the actual accuracy is not
guaranteed. When requesting high-accuracy locations, the initial update delivered
by the LocationEngine may not have the requested accuracy. Requesting higher
accuracy location updates usually means higher power consumption, therefore
you should use the lowest accuracy suitable for your use case to preserve the
device battery.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO13bestAvailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bestAvailable"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO13bestAvailableyA2CmF">bestAvailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The best level of accuracy available when you don’t need the level of accuracy required for navigation apps.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bestAvailable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO18subMeterNavigationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/subMeterNavigation"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO18subMeterNavigationyA2CmF">subMeterNavigation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Not supported in iOS.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">subMeterNavigation</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO10navigationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/navigation"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO10navigationyA2CmF">navigation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The highest possible accuracy that uses additional sensor data to facilitate navigation apps.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">navigation</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO12tensOfMetersyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tensOfMeters"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO12tensOfMetersyA2CmF">tensOfMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Accurate to within tens of meters of the desired target.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tensOfMeters</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO16hundredsOfMetersyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hundredsOfMeters"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO16hundredsOfMetersyA2CmF">hundredsOfMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Accurate to within hundreds of meters of the desired target.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hundredsOfMeters</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO10kilometersyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/kilometers"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO10kilometersyA2CmF">kilometers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Accurate to within kilometers of the desired target.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">kilometers</span></code></pre>
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

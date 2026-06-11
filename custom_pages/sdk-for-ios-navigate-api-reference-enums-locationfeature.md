---
title: "LocationFeature"
slug: "sdk-for-ios-navigate-api-reference-enums-locationfeature"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationFeature"></a>
<a title="LocationFeature Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-positioning">Positioning</a>

        LocationFeature Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationFeature</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationFeature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Location features supported by HERE positioning.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO19cellularPositioningyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cellularPositioning"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO19cellularPositioningyA2CmF">cellularPositioning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cellular network positioning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cellularPositioning</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO17wifiPositioning2dyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/wifiPositioning2d"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO17wifiPositioning2dyA2CmF">wifiPositioning2d</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>WiFi network positioning without altitude.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">wifiPositioning2d</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO17wifiPositioning3dyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/wifiPositioning3d"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO17wifiPositioning3dyA2CmF">wifiPositioning3d</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>WiFi network positioning with altitude.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">wifiPositioning3d</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO17hdGnssPositioningyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hdGnssPositioning"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO17hdGnssPositioningyA2CmF">hdGnssPositioning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HD GNSS positioning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hdGnssPositioning</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO14vdrPositioningyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/vdrPositioning"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO14vdrPositioningyA2CmF">vdrPositioning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle Dead Reckoning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">vdrPositioning</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO9undefinedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/undefined"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO9undefinedyA2CmF">undefined</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Not defined.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">undefined</span></code></pre>
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

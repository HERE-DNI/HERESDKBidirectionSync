---
title: "SpecialSpeedType"
slug: "sdk-for-ios-navigate-api-reference-enums-specialspeedtype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SpecialSpeedType"></a>
<a title="SpecialSpeedType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>

        SpecialSpeedType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpecialSpeedType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SpecialSpeedType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents the speed situation type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unknown special speed type</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknown</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO08advisoryC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/advisorySpeed"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO08advisoryC0yA2CmF">advisorySpeed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>These posted speeds are not the legal limit, but rather serve to warn a driver that road conditions
indicate a lower speed is practical. Typically, the road condition is a curved road or a ramp but it may be
due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign
is on a different road than the one for which it applies (this can happen with ramps). In this case, the
advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters
from the particular road.</p>
<ul>
<li>Advisory speed signs due to construction are not included.</li>
<li>A speed value is published for advisory signs.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">advisorySpeed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO17speedBumpsPresentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/speedBumpsPresent"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO17speedBumpsPresentyA2CmF">speedBumpsPresent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This indicates that for a stretch of road, speed bumps are
present or chicanes are present that effectively reduce the posted speed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">speedBumpsPresent</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO6schoolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/school"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO6schoolyA2CmF">school</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>School zone signs are often placed to slow drivers before reaching an intersection where children are
crossing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">school</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO13timeDependentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/timeDependent"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO13timeDependentyA2CmF">timeDependent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
Speed limit that is in effect considering the current local time provided by the device’s
clock.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">timeDependent</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO23approximateSeasonalTimeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/approximateSeasonalTime"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO23approximateSeasonalTimeyA2CmF">approximateSeasonalTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Speed limit that is in effect considering the season</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">approximateSeasonalTime</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO13laneDependentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/laneDependent"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO13laneDependentyA2CmF">laneDependent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>These are situations where a road has different speed limits per lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">laneDependent</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO4rainyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rain"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO4rainyA2CmF">rain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when it is raining or there is water on the road.</p>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rain</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO4snowyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/snow"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO4snowyA2CmF">snow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when there is snow on the road.</p>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">snow</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO3fogyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/fog"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO3fogyA2CmF">fog</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility decreases due to fog.</p>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">fog</span></code></pre>
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

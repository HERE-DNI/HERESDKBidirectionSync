---
title: "SpeedLimit"
slug: "sdk-for-ios-navigate-structs-speedlimit"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedLimit"></a>
<a title="SpeedLimit Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        SpeedLimit Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpeedLimit</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents the speed limit of the current road.
Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits,
the HERE SDK internally reads the current device time and notifies only on speed limits
that are currently active.</p>
<p>It is recommended to use <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV09effectivebC17InMetersPerSecondSdSgyF">SpeedLimit.effectiveSpeedLimitInMetersPerSecond(...)</a></code> when
an application does not offer dedicated speed limit indicators for other cases, such as
weather-dependent speed limits.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regular speed limit if available. In case of unbounded speed limit, the value is zero.</p>
<p><strong>Note:</strong>
When following a route, then this value will depend on the selected transport mode.
For other speed limits, like weather-dependent speed limits only the value as shown
on the local road sign is provided. It may not be applicable to all transport modes.
For tracking mode (without following a route), the VehicleProfile is ignored and only
the speed limit from the local road sign is provided or the regular speed limit
for a particular type of road or area like regular inner-city speed limits.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV08advisorybC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/advisorySpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV08advisorybC17InMetersPerSecondSdSgvp">advisorySpeedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A recommended speed limit that may not be indicated on the local road signs,
but that serves to warn a driver that the road conditions may indicate a lower speed.
Typically, the road condition is a curved road or a ramp but it may be due to a narrow road,
narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a
different road than the one for which it applies (this can happen with ramps). In this case,
the advisory speed is indicated for the road for which it is intended, even if the sign is
further than 50 meters from the particular road.</p>
<ul>
<li>Advisory speed signs due to construction are not included.</li>
<li>A speed value is published for advisory signs.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">advisorySpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV04snowbC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/snowSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV04snowbC17InMetersPerSecondSdSgvp">snowSpeedLimitInMetersPerSecond</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">snowSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV04rainbC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rainSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV04rainbC17InMetersPerSecondSdSgvp">rainSpeedLimitInMetersPerSecond</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rainSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV03fogbC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fogSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV03fogbC17InMetersPerSecondSdSgvp">fogSpeedLimitInMetersPerSecond</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fogSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/optimalWeatherSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp">optimalWeatherSpeedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility is optimal due to weather
conditions.</p>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
<p><strong>Note:</strong>
This speed limit is conditioned by factors not expressed by the other ones.
For example, it may be a time-related speed limit or a vehicle-related one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">optimalWeatherSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp">schoolZoneSpeedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A conditional speed limit as indicated on the local road signs.
School zone signs are often placed to slow drivers before reaching an intersection where
children are crossing.</p>
<p>A possible usage example can be to show an icon on the device’s screen containing both
special speed limit value and a visual cue in order to warn the user about the conditional
speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">schoolZoneSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeDependentSpeedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp">timeDependentSpeedLimitInMetersPerSecond</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeDependentSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecond08advisorybcefgH004snowbcefgH004rainbcefgH003fogbcefgH0014optimalWeatherbcefgH0010schoolZonebcefgH0013timeDependentbcefgH0ACSdSg_A7Ltcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(speedLimitInMetersPerSecond:advisorySpeedLimitInMetersPerSecond:snowSpeedLimitInMetersPerSecond:rainSpeedLimitInMetersPerSecond:fogSpeedLimitInMetersPerSecond:optimalWeatherSpeedLimitInMetersPerSecond:schoolZoneSpeedLimitInMetersPerSecond:timeDependentSpeedLimitInMetersPerSecond:)"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecond08advisorybcefgH004snowbcefgH004rainbcefgH003fogbcefgH0014optimalWeatherbcefgH0010schoolZonebcefgH0013timeDependentbcefgH0ACSdSg_A7Ltcfc">init(speedLimitInMetersPerSecond:<wbr/>advisorySpeedLimitInMetersPerSecond:<wbr/>snowSpeedLimitInMetersPerSecond:<wbr/>rainSpeedLimitInMetersPerSecond:<wbr/>fogSpeedLimitInMetersPerSecond:<wbr/>optimalWeatherSpeedLimitInMetersPerSecond:<wbr/>schoolZoneSpeedLimitInMetersPerSecond:<wbr/>timeDependentSpeedLimitInMetersPerSecond:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>speedLimitInMetersPerSecond: Regular speed limit if available. In case of unbounded speed limit, the value is zero.</li>
</ul>
<p><strong>Note:</strong>
  When following a route, then this value will depend on the selected transport mode.
  For other speed limits, like weather-dependent speed limits only the value as shown
  on the local road sign is provided. It may not be applicable to all transport modes.
  For tracking mode (without following a route), the VehicleProfile is ignored and only
  the speed limit from the local road sign is provided or the regular speed limit
  for a particular type of road or area like regular inner-city speed limits.</p>
<ul>
<li>advisorySpeedLimitInMetersPerSecond: A recommended speed limit that may not be indicated on the local road signs,
but that serves to warn a driver that the road conditions may indicate a lower speed.
Typically, the road condition is a curved road or a ramp but it may be due to a narrow road,
narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a
different road than the one for which it applies (this can happen with ramps). In this case,
the advisory speed is indicated for the road for which it is intended, even if the sign is
further than 50 meters from the particular road.

<ul>
<li>Advisory speed signs due to construction are not included.</li>
<li>A speed value is published for advisory signs.</li>
</ul></li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<ul>
<li>snowSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when there is snow on the road.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<ul>
<li>rainSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when it is raining or there is water on the road.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<ul>
<li>fogSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility decreases due to fog.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<ul>
<li>optimalWeatherSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility is optimal due to weather
conditions.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<p><strong>Note:</strong>
  This speed limit is conditioned by factors not expressed by the other ones.
  For example, it may be a time-related speed limit or a vehicle-related one.</p>
<ul>
<li>schoolZoneSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
School zone signs are often placed to slow drivers before reaching an intersection where
children are crossing.</li>
</ul>
<p>A possible usage example can be to show an icon on the device’s screen containing both
  special speed limit value and a visual cue in order to warn the user about the conditional
  speed limit.</p>
<ul>
<li>timeDependentSpeedLimitInMetersPerSecond: A conditional speed limit as indicated on the local road signs.
Speed limit that is in effect considering the current local time provided by the device’s
clock.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">advisorySpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">snowSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">rainSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">fogSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">optimalWeatherSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">schoolZoneSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timeDependentSpeedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV09effectivebC17InMetersPerSecondSdSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/effectiveSpeedLimitInMetersPerSecond()"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV09effectivebC17InMetersPerSecondSdSgyF">effectiveSpeedLimitInMetersPerSecond()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the effective (lowest) speed limit between <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp">SpeedLimit.speedLimitInMetersPerSecond</a></code>,
<code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp">SpeedLimit.schoolZoneSpeedLimitInMetersPerSecond</a></code>, <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp">SpeedLimit.timeDependentSpeedLimitInMetersPerSecond</a></code>
and <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp">SpeedLimit.optimalWeatherSpeedLimitInMetersPerSecond</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">effectiveSpeedLimitInMetersPerSecond</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Returns the lowest value between: <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV05speedC17InMetersPerSecondSdSgvp">SpeedLimit.speedLimitInMetersPerSecond</a></code>,
<code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV010schoolZonebC17InMetersPerSecondSdSgvp">SpeedLimit.schoolZoneSpeedLimitInMetersPerSecond</a></code>, <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV013timeDependentbC17InMetersPerSecondSdSgvp">SpeedLimit.timeDependentSpeedLimitInMetersPerSecond</a></code>
and <code><a href="../Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV014optimalWeatherbC17InMetersPerSecondSdSgvp">SpeedLimit.optimalWeatherSpeedLimitInMetersPerSecond</a></code>.</p>
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

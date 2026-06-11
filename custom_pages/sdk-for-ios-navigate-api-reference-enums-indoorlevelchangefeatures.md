---
title: "IndoorLevelChangeFeatures"
slug: "sdk-for-ios-navigate-api-reference-enums-indoorlevelchangefeatures"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IndoorLevelChangeFeatures"></a>
<a title="IndoorLevelChangeFeatures Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-other%20enums">Other Enumerations</a>

        IndoorLevelChangeFeatures Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorLevelChangeFeatures</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IndoorLevelChangeFeatures</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indoor route features.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO9connectoryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/connector"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO9connectoryA2CmF">connector</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Generic connector for indoor routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">connector</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO8elevatoryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/elevator"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO8elevatoryA2CmF">elevator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of an elevator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">elevator</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO9escalatoryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/escalator"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO9escalatoryA2CmF">escalator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of an escalator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">escalator</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO4rampyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ramp"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO4rampyA2CmF">ramp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of a ramp.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ramp</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO6stairsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/stairs"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO6stairsyA2CmF">stairs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of stairs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">stairs</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO14pedestrianRampyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrianRamp"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO14pedestrianRampyA2CmF">pedestrianRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of a pedestrian ramp.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pedestrianRamp</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO7carLiftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/carLift"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO7carLiftyA2CmF">carLift</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of a car lift.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">carLift</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO9driveRampyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/driveRamp"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO9driveRampyA2CmF">driveRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of a drive ramp.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">driveRamp</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25IndoorLevelChangeFeaturesO12elevatorBankyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/elevatorBank"></a>
<a class="token" href="#/s:7heresdk25IndoorLevelChangeFeaturesO12elevatorBankyA2CmF">elevatorBank</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route requires the usage of an elevator bank.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">elevatorBank</span></code></pre>
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

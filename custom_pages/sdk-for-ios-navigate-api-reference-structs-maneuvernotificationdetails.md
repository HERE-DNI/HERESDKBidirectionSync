---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-maneuvernotificationdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ManeuverNotificationDetails.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationDetails"></a>
<a title="ManeuverNotificationDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ManeuverNotificationDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverNotificationDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides the information regarding the next maneuver to be triggered</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationDetailsV8maneuverAA0B0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuver"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationDetailsV8maneuverAA0B0Cvp">maneuver</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current maneuver data. In case of a double maneuver e.g. “Now turn right and then turn left”,
this attribute will contain the maneuver data of the first maneuver of the combined maneuver “Now turn right”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuver</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-maneuver">Maneuver</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationDetailsV08maneuverC4TypeAA0bcF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverNotificationType"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationDetailsV08maneuverC4TypeAA0bcF0Ovp">maneuverNotificationType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the type of the current maneuver notification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverNotificationType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-maneuvernotificationtype">ManeuverNotificationType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationDetailsV010isCombinedB4TextSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCombinedManeuverText"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationDetailsV010isCombinedB4TextSbvp">isCombinedManeuverText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether the current text notification combines information regarding current and next maneuver,
such as, “Now turn right and then turn left onto Invalidenstrasse”, or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCombinedManeuverText</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationDetailsV8maneuver0eC4Type010isCombinedB4TextAcA0B0C_AA0bcF0OSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maneuver:maneuverNotificationType:isCombinedManeuverText:)"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationDetailsV8maneuver0eC4Type010isCombinedB4TextAcA0B0C_AA0bcF0OSbtcfc">init(maneuver:<wbr/>maneuverNotificationType:<wbr/>isCombinedManeuverText:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maneuver</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-maneuver">Maneuver</a></span><span class="p">,</span> <span class="nv">maneuverNotificationType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-maneuvernotificationtype">ManeuverNotificationType</a></span><span class="p">,</span> <span class="nv">isCombinedManeuverText</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

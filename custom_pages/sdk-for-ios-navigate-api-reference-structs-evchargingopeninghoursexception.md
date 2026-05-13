---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingopeninghoursexception"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingOpeningHoursException.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHoursException"></a>
<a title="EVChargingOpeningHoursException Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingOpeningHoursException Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingOpeningHoursException</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingOpeningHoursException</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents exceptions to the regular opening hours schedule for EV charging locations,
such as special closures or extended hours.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31EVChargingOpeningHoursExceptionV4date10Foundation4DateVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/date"></a>
<a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV4date10Foundation4DateVvp">date</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Date of special opening hours.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">date</span><span class="p">:</span> <span class="kt">Date</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/periods"></a>
<a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp">periods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of time periods when the charging location is open on the specified date.
The time periods are in the local time zone of the charging location, and
are represented as a list of objects with <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV4fromSSvp">TimeOfDayRange.from</a></code>
and <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV2toSSvp">TimeOfDayRange.to</a></code> properties.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">periods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-timeofdayrange">TimeOfDayRange</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31EVChargingOpeningHoursExceptionV6closedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/closed"></a>
<a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV6closedSbvp">closed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>True if the charging location is closed on particular date, in which case
<code><a href="../Structs/EVChargingOpeningHoursException.html#/s:7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp">EVChargingOpeningHoursException.periods</a></code> is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">closed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31EVChargingOpeningHoursExceptionV4date7periods6closedAC10Foundation4DateV_SayAA14TimeOfDayRangeVGSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(date:periods:closed:)"></a>
<a class="token" href="#/s:7heresdk31EVChargingOpeningHoursExceptionV4date7periods6closedAC10Foundation4DateV_SayAA14TimeOfDayRangeVGSbtcfc">init(date:<wbr/>periods:<wbr/>closed:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">date</span><span class="p">:</span> <span class="kt">Date</span> <span class="o">=</span> <span class="kt">Date</span><span class="p">(</span><span class="nv">timeIntervalSince1970</span><span class="p">:</span> <span class="mi">0</span><span class="p">),</span> <span class="nv">periods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-timeofdayrange">TimeOfDayRange</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">closed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

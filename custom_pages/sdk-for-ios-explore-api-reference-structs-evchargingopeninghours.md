---
title: "EVChargingOpeningHours Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingopeninghours"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingOpeningHours.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHours"></a>
<a title="EVChargingOpeningHours Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingOpeningHours Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingOpeningHours : Hashable</code></pre>
</div>
</div>
<p>Represents the times when the EVSEs at the charging location can be accessed for charging.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/open24x7"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp">open24x7</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the charging location is open 24 hours a day, 7 days per week.
If true, <code><a href="../Structs/EVChargingOpeningHours.html#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp">EVChargingOpeningHours.regularSchedule</a></code> and <code><a href="../Structs/EVChargingOpeningHours.html#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp">EVChargingOpeningHours.exceptions</a></code> will be empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var open24x7: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingWhenClosed"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp">chargingWhenClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if it is allowed to leave vehicles in the charging location to continue
charging outside opening hours.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var chargingWhenClosed: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/regularSchedule"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp">regularSchedule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of regular opening hours schedule for EV charging locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var regularSchedule: [EVChargingOpeningHoursSchedule]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/exceptions"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp">exceptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of opening hours exceptions for EV charging locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var exceptions: [EVChargingOpeningHoursException]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22EVChargingOpeningHoursV8open24x718chargingWhenClosed15regularSchedule10exceptionsACSb_SbSayAA0bcdJ0VGSayAA0bcD9ExceptionVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(open24x7:chargingWhenClosed:regularSchedule:exceptions:)"></a>
<a class="token" href="#/s:7heresdk22EVChargingOpeningHoursV8open24x718chargingWhenClosed15regularSchedule10exceptionsACSb_SbSayAA0bcdJ0VGSayAA0bcD9ExceptionVGtcfc">init(open24x7:<wbr/>chargingWhenClosed:<wbr/>regularSchedule:<wbr/>exceptions:<wbr/>)</a>
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
<pre><code>public init(open24x7: Bool = false, chargingWhenClosed: Bool = true, regularSchedule: [EVChargingOpeningHoursSchedule] = [], exceptions: [EVChargingOpeningHoursException] = [])</code></pre>
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



</div>
`
}</HTMLBlock>

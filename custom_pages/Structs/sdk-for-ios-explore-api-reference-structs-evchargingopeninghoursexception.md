---
title: "EVChargingOpeningHoursException Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingopeninghoursexception"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingOpeningHoursException.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOpeningHoursException"></a>
<a title="EVChargingOpeningHoursException Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingOpeningHoursException Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingOpeningHoursException : Hashable</code></pre>
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
<pre><code>public var date: Date</code></pre>
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
<pre><code>public var periods: [TimeOfDayRange]</code></pre>
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
<pre><code>public var closed: Bool</code></pre>
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
<pre><code>public init(date: Date = Date(timeIntervalSince1970: 0), periods: [TimeOfDayRange] = [], closed: Bool = false)</code></pre>
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

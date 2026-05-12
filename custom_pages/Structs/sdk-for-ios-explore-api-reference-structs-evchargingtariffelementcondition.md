---
title: "EVChargingTariffElementCondition Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingtariffelementcondition"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingTariffElementCondition.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariffElementCondition"></a>
<a title="EVChargingTariffElementCondition Structure Reference"></a>
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
        EVChargingTariffElementCondition Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingTariffElementCondition : Hashable</code></pre>
</div>
</div>
<p>Condition that the charging session needs to meet to apply the tariff element.
Tariff elements may include conditions that define when they apply:</p>
<ul>
<li>Time of day (e.g., 22:00–06:00)</li>
<li>Day of week (e.g., weekends only)</li>
</ul><div class="aside aside-date">
<p class="aside-title">Date</p>
    Date range (e.g., seasonal pricing)

</div><ul>
<li>Charging session duration</li>
<li>Battery level thresholds (e.g., overstay fees)</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/date"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp">date</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Date range when the tariff element is valid. This is typically used to indicate seasonal
tariffs or to announce an update to the tariff in advance. It may also be used to indicate
spot prices, together with time period.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var date: DateRange?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/days"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp">days</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Day(s) of the week when the tariff element is valid.
An example would be to specify lower prices for weekends</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var days: [DayOfWeek]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV4timeAA14TimeOfDayRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/time"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV4timeAA14TimeOfDayRangeVSgvp">time</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time period when the tariff element is valid, in local time. The time period wraps around to
the next day, when end time of the period <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV2toSSvp">TimeOfDayRange.to</a></code>
is smaller than the beginning <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV4fromSSvp">TimeOfDayRange.from</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var time: TimeOfDayRange?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV8durationAA0B13DurationRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV8durationAA0B13DurationRangeVSgvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Duration of the charging session when the tariff element is valid, in seconds.</p>
<p>Often only either one of the values is present, indicating the minimum or maximum duration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var duration: EVChargingDurationRange?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV20overstayBatteryLevels5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/overstayBatteryLevel"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV20overstayBatteryLevels5Int32VSgvp">overstayBatteryLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum battery level when the tariff element is valid, in percentages. This can be used to
set additional fees for charging a full or nearly full battery.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var overstayBatteryLevel: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EVChargingTariffElementConditionV4date4days4time8duration20overstayBatteryLevelAcA9DateRangeVSg_SayAA9DayOfWeekOGAA04TimepoN0VSgAA0b8DurationN0VSgs5Int32VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(date:days:time:duration:overstayBatteryLevel:)"></a>
<a class="token" href="#/s:7heresdk32EVChargingTariffElementConditionV4date4days4time8duration20overstayBatteryLevelAcA9DateRangeVSg_SayAA9DayOfWeekOGAA04TimepoN0VSgAA0b8DurationN0VSgs5Int32VSgtcfc">init(date:<wbr/>days:<wbr/>time:<wbr/>duration:<wbr/>overstayBatteryLevel:<wbr/>)</a>
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
<div class="aside aside-date">
<p class="aside-title">Date</p>
    Date range when the tariff element is valid. This is typically used to indicate seasonal
tariffs or to announce an update to the tariff in advance. It may also be used to indicate
spot prices, together with time period.

</div><ul>
<li>days: Day(s) of the week when the tariff element is valid.
An example would be to specify lower prices for weekends</li>
<li>time: Time period when the tariff element is valid, in local time. The time period wraps around to
the next day, when end time of the period <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV2toSSvp">TimeOfDayRange.to</a></code>
is smaller than the beginning <code><a href="../Structs/TimeOfDayRange.html#/s:7heresdk14TimeOfDayRangeV4fromSSvp">TimeOfDayRange.from</a></code>.</li>
<li>duration: Duration of the charging session when the tariff element is valid, in seconds.</li>
</ul>
<p>Often only either one of the values is present, indicating the minimum or maximum duration.</p>
<ul>
<li>overstayBatteryLevel: Minimum battery level when the tariff element is valid, in percentages. This can be used to
set additional fees for charging a full or nearly full battery.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(date: DateRange? = nil, days: [DayOfWeek] = [], time: TimeOfDayRange? = nil, duration: EVChargingDurationRange? = nil, overstayBatteryLevel: Int32? = nil)</code></pre>
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

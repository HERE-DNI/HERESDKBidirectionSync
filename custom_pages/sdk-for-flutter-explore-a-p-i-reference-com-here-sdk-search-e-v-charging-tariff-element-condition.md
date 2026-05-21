---
title: "EVCharging Tariff Element Condition"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/EVChargingTariffElementCondition///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/EVChargingTariffElementCondition</div>
<div class="cover">
<h1 class="cover">EVCharging<wbr/>Tariff<wbr/>Element<wbr/>Condition</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition</div><p class="paragraph">Condition that the charging session needs to meet to apply the tariff element. Tariff elements may include conditions that define when they apply:</p><ul><li><p class="paragraph">Time of day (e.g., 22:00–06:00)</p></li><li><p class="paragraph">Day of week (e.g., weekends only)</p></li><li><p class="paragraph">Date range (e.g., seasonal pricing)</p></li><li><p class="paragraph">Charging session duration</p></li><li><p class="paragraph">Battery level thresholds (e.g., overstay fees)</p></li></ul><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="EVChargingTariffElementCondition" data-filterable-set=":modules:dokkaHtml/release" data-name="848702704%2FConstructors%2F1617540583" id="848702704%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-e-v-charging-tariff-element-condition</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="date" data-filterable-set=":modules:dokkaHtml/release" data-name="1316940039%2FProperties%2F1617540583" id="1316940039%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-date</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-date: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-date-range?</div><div class="brief"><p class="paragraph">Date range when the tariff element is valid. This is typically used to indicate seasonal tariffs or to announce an update to the tariff in advance. It may also be used to indicate spot prices, together with time period.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="days" data-filterable-set=":modules:dokkaHtml/release" data-name="-2030647170%2FProperties%2F1617540583" id="-2030647170%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-days</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-days: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-day-of-week&gt;</div><div class="brief"><p class="paragraph">Day(s) of the week when the tariff element is valid. An example would be to specify lower prices for weekends</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="duration" data-filterable-set=":modules:dokkaHtml/release" data-name="236944865%2FProperties%2F1617540583" id="236944865%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-duration-range?</div><div class="brief"><p class="paragraph">Duration of the charging session when the tariff element is valid, in seconds.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="overstayBatteryLevel" data-filterable-set=":modules:dokkaHtml/release" data-name="423202353%2FProperties%2F1617540583" id="423202353%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-overstay-battery-level</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-overstay-battery-level: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Minimum battery level when the tariff element is valid, in percentages. This can be used to set additional fees for charging a full or nearly full battery.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="time" data-filterable-set=":modules:dokkaHtml/release" data-name="-657590584%2FProperties%2F1617540583" id="-657590584%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-time</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-time: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-time-of-day-range?</div><div class="brief"><p class="paragraph">Time period when the tariff element is valid, in local time. The time period wraps around to the next day, when end time of the period <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/index.html">com.here.sdk.search.TimeOfDayRange.to</a> is smaller than the beginning /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-time-of-day-range-from.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-306965972%2FFunctions%2F1617540583" id="-306965972%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-1328106182%2FFunctions%2F1617540583" id="-1328106182%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff-element-condition-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>

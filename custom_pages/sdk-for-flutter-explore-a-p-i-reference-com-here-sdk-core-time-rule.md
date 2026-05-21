---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core/TimeRule///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core/TimeRule</div>
<div class="cover">
<h1 class="cover">Time<wbr/>Rule</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification. For example: -*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p><p class="paragraph">The operator * represents reccuring occurrence, <code class="lang-kotlin">+</code> represents a logical OR operation and <code class="lang-kotlin">-</code> represents exclusion meaning, BUT NOT operations.</p><p class="paragraph">This example string represents a time period that meets the following criteria:</p><ul><li><p class="paragraph"><code class="lang-kotlin">M3f21h2</code>: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as "f" might indicate "first", "second", "third", etc.), 1 stands for the day of the week (1...7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.</p></li><li><p class="paragraph"><code class="lang-kotlin">{M9}</code>: This denotes "for 9 months", with "M9" standing for nine months. The brackets {} indicate a duration.</p></li><li><p class="paragraph"><code class="lang-kotlin">M11f12h2</code>: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1...7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.</p></li><li><p class="paragraph">{-M9}: This denotes "9 months ago from the current stated time", with "-M9" standing for nine months in the past.</p></li><li><p class="paragraph"><code class="lang-kotlin">(h15){h2}(h20){h2}</code>: 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.</p></li></ul><p class="paragraph">Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.</p><p class="paragraph">For more advanced examples of <code class="lang-kotlin">TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="TimeRule" data-filterable-set=":modules:dokkaHtml/release" data-name="-1116246249%2FConstructors%2F1617540583" id="-1116246249%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-time-rule</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(timeRule: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, timeZoneOffsetSeconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, dstSpec: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-549352673%2FClasslikes%2F1617540583" id="-549352673%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="dstSpec" data-filterable-set=":modules:dokkaHtml/release" data-name="1103315320%2FProperties%2F1617540583" id="1103315320%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-dst-spec</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-dst-spec: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="timeRuleString" data-filterable-set=":modules:dokkaHtml/release" data-name="-1078040856%2FProperties%2F1617540583" id="-1078040856%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-time-rule-string</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-time-rule-string: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The time rule as a string in ISO 14825 format.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="timeZoneOffsetSeconds" data-filterable-set=":modules:dokkaHtml/release" data-name="-944224795%2FProperties%2F1617540583" id="-944224795%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-time-zone-offset-seconds</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-time-zone-offset-seconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">The time zone offset in seconds for the location where the time rule applies.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="appliesTo" data-filterable-set=":modules:dokkaHtml/release" data-name="569747043%2FFunctions%2F1617540583" id="569747043%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-applies-to</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-applies-to(dateTime: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a>): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-245270657%2FFunctions%2F1617540583" id="-245270657%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-171346297%2FFunctions%2F1617540583" id="-171346297%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

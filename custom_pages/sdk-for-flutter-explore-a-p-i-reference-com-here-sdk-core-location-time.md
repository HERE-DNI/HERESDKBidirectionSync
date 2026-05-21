---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core/LocationTime///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core/LocationTime</div>
<div class="cover">
<h1 class="cover">Location<wbr/>Time</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time</div><p class="paragraph">This struct presents all the time data tied to a location, like an arrival or departure time. The time data is originally specified in RFC 3339, section 5.6 format. For example, "2022-03-23T16:07:31+01:00" in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn't give any data on the tied location. The location should be derived from the context.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="LocationTime" data-filterable-set=":modules:dokkaHtml/release" data-name="1228598933%2FConstructors%2F1617540583" id="1228598933%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-location-time</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(localTime: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a>, utcTime: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a>, utcOffset: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="localTime" data-filterable-set=":modules:dokkaHtml/release" data-name="2075912743%2FProperties%2F1617540583" id="2075912743%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-local-time</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-local-time: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a></div><div class="brief"><p class="paragraph">The time as observed in the tied location. For example, if a route is requested in Cracow, Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="utcOffset" data-filterable-set=":modules:dokkaHtml/release" data-name="1000477832%2FProperties%2F1617540583" id="1000477832%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-utc-offset</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-utc-offset: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration</div><div class="brief"><p class="paragraph">The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is UTC-05:00, it is -18000.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="utcTime" data-filterable-set=":modules:dokkaHtml/release" data-name="-786291954%2FProperties%2F1617540583" id="-786291954%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-utc-time</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-utc-time: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a></div><div class="brief"><p class="paragraph">The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland, the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-1148950874%2FFunctions%2F1617540583" id="-1148950874%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-107966592%2FFunctions%2F1617540583" id="-107966592%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-time-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

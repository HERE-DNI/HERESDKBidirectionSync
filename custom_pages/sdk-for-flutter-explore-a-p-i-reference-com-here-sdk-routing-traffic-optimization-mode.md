---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/TrafficOptimizationMode///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/TrafficOptimizationMode</div>
<div class="cover">
<h1 class="cover">Traffic<wbr/>Optimization<wbr/>Mode</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode&gt; </div><p class="paragraph">Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
<div class="tabs-section-body">
<div data-togglable="ENTRY">
<h2 class="">Entries</h2>
<div class="table"><a anchor-label="TIME_DEPENDENT" data-filterable-set=":modules:dokkaHtml/release" data-name="1641674960%2FClasslikes%2F1617540583" id="1641674960%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-t-i-m-e-d-e-p-e-n-d-e-n-t</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-t-i-m-e-d-e-p-e-n-d-e-n-t</div></div><div class="brief"><p class="paragraph">Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-departure-time or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-arrival-time. As a result, streets with heavy traffic will be avoided whenever possible. Note that this mode enables traffic-aware routing.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="LONG_TERM_CLOSURES_ONLY" data-filterable-set=":modules:dokkaHtml/release" data-name="-1072592600%2FClasslikes%2F1617540583" id="-1072592600%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-l-o-n-g-t-e-r-m-c-l-o-s-u-r-e-s-o-n-l-y</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-l-o-n-g-t-e-r-m-c-l-o-s-u-r-e-s-o-n-l-y</div></div><div class="brief"><p class="paragraph">Only long-term road closures are taken into account. Both /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-departure-time and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-arrival-time are ignored, and the route will be shaped disregarding all the available current and historical traffic information, except long-term road closures. Note that this mode disables traffic-aware routing regardless of other settings.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="DISABLED" data-filterable-set=":modules:dokkaHtml/release" data-name="-1126531489%2FClasslikes%2F1617540583" id="-1126531489%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-d-i-s-a-b-l-e-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-d-i-s-a-b-l-e-d</div></div><div class="brief"><p class="paragraph">Traffic optimization is completely disabled, including long-term road closures. Both /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-departure-time and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-arrival-time are ignored, and the route will be shaped disregarding all the available current and historical traffic information. Note that seasonal closures are not excluded. To exclude seasonal closures, use /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-road-features-s-e-a-s-o-n-a-l-c-l-o-s-u-r-e. Note that this mode disables traffic-aware routing regardless of other settings.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="entries" data-filterable-set=":modules:dokkaHtml/release" data-name="-1623892547%2FProperties%2F1617540583" id="-1623892547%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-entries</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-entries: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode&gt;</div><div class="brief"><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="value" data-filterable-set=":modules:dokkaHtml/release" data-name="-1542929412%2FProperties%2F1617540583" id="-1542929412%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-value</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="valueOf" data-filterable-set=":modules:dokkaHtml/release" data-name="-810321153%2FFunctions%2F1617540583" id="-810321153%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-value-of</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-value-of(value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode</div><div class="brief"><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="values" data-filterable-set=":modules:dokkaHtml/release" data-name="980083275%2FFunctions%2F1617540583" id="980083275%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-values</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode-values(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-traffic-optimization-mode&gt;</div><div class="brief"><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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

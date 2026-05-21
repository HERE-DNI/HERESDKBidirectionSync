---
title: "Routing Options"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/RoutingOptions///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/RoutingOptions</div>
<div class="cover">
<h1 class="cover">Routing<wbr/>Options</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options</div><p class="paragraph">The options defines how a route should be calculated.</p><p class="paragraph">The options are used for all transport modes and engines.</p><p class="paragraph">** Electric vehicle specific requirements ** Electric vehicle consumption are estimated when at least one consumption model is defined. Currently two models are supported:</p><ul><li><p class="paragraph">PhysicalConsumptionModel Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-current-weight-in-kilograms from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-specification-vehicle-specification     from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-transport-specification</p></li><li><p class="paragraph">Additionally /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-current-weight-change-in-kilograms can be defined.</p></li><li><p class="paragraph">EmpiricalConsumptionModel</p></li></ul><p class="paragraph">By setting /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-electric-vehicle-options-ensure-reachability the <code class="lang-kotlin">RoutingEngine</code> inserts additional charging stations to reach the waypoints. This feature requires setting the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-battery-specifications. By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints. See the parameter description below for more details.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="RoutingOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="1548904092%2FConstructors%2F1617540583" id="1548904092%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-routing-options</div>

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
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1933025363%2FClasslikes%2F1617540583" id="-1933025363%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="allowOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="1590171391%2FProperties%2F1617540583" id="1590171391%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-allow-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-allow-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-allow-options</div><div class="brief"><p class="paragraph">The options explicitly allowed by user for route calculations. By default no options are opt in.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="avoidanceOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="307940474%2FProperties%2F1617540583" id="307940474%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-avoidance-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-avoidance-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options</div><div class="brief"><p class="paragraph">Options to specify restrictions for route calculations. By default no restrictions are applied.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="evOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="1880760921%2FProperties%2F1617540583" id="1880760921%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-ev-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-ev-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-electric-vehicle-options?</div><div class="brief"><p class="paragraph">Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability. When no EV options are defined an internal combustion engine is assumed.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxSpeedOnSegments" data-filterable-set=":modules:dokkaHtml/release" data-name="435559730%2FProperties%2F1617540583" id="435559730%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-max-speed-on-segments</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-max-speed-on-segments: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-max-speed-on-segment&gt;</div><div class="brief"><p class="paragraph">Segments with restriction on maximum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-dynamic-speed-info-base-speed-in-meters-per-second. <strong>Note</strong> Not used for offline calculations.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-4381185%2FProperties%2F1617540583" id="-4381185%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-route-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-route-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options</div><div class="brief"><p class="paragraph">Specifies the common route calculation options.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="textOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="1889494165%2FProperties%2F1617540583" id="1889494165%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-text-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-text-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-text-options</div><div class="brief"><p class="paragraph">Customize textual content returned from the route calculation, such as localization, format, and unit system.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="tollOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-1461989213%2FProperties%2F1617540583" id="-1461989213%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-toll-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-toll-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-toll-options</div><div class="brief"><p class="paragraph">Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type. <strong>Note</strong> Not used for offline calculations.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="transportSpecification" data-filterable-set=":modules:dokkaHtml/release" data-name="-73619302%2FProperties%2F1617540583" id="-73619302%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-transport-specification</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-transport-specification: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-specification</div><div class="brief"><p class="paragraph">Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. <strong>Notes:</strong></p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-1563828723%2FFunctions%2F1617540583" id="-1563828723%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="753850425%2FFunctions%2F1617540583" id="753850425%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

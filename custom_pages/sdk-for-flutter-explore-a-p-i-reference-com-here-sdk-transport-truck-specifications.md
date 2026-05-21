---
title: "Truck Specifications"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.transport/TruckSpecifications///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport/TruckSpecifications</div>
<div class="cover">
<h1 class="cover">Truck<wbr/>Specifications</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use `TransportSpecification` instead.</p></div><p class="paragraph">Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="TruckSpecifications" data-filterable-set=":modules:dokkaHtml/release" data-name="2047592185%2FConstructors%2F1617540583" id="2047592185%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-truck-specifications</div>

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
<div class="table"><a anchor-label="axleCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-234710615%2FProperties%2F1617540583" id="-234710615%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering <code class="lang-kotlin">sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count greater than /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count will not be displayed. When specifying /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count, then /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count is required and must be greater than /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="currentWeightInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="-797290643%2FProperties%2F1617540583" id="-797290643%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-current-weight-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-current-weight-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-gross-weight-in-kilograms. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="grossWeightInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="-744916040%2FProperties%2F1617540583" id="-744916040%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-gross-weight-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-gross-weight-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-current-weight-in-kilograms. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="heightInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="1048115753%2FProperties%2F1617540583" id="1048115753%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-height-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-height-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isTruckLight" data-filterable-set=":modules:dokkaHtml/release" data-name="-1368256975%2FProperties%2F1617540583" id="-1368256975%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-is-truck-light</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-is-truck-light: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to <code class="lang-kotlin">true</code> in other countries than Japan. The flag defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lengthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="411065512%2FProperties%2F1617540583" id="411065512%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-length-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-length-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="payloadCapacityInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="634305988%2FProperties%2F1617540583" id="634305988%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-payload-capacity-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-payload-capacity-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="trailerAxleCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-1427514426%2FProperties%2F1617540583" id="-1427514426%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines total number of axles across all the trailers attached to the vehicle. This number is included in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count, hence /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count must be less than /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count and greater than or equal to 1. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-axle-count and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-count are required to specify /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count. By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="trailerCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-795394122%2FProperties%2F1617540583" id="-795394122%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-axle-count, then /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-trailer-count is required and must be greater than 0.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="truckType" data-filterable-set=":modules:dokkaHtml/release" data-name="32015791%2FProperties%2F1617540583" id="32015791%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-truck-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-truck-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-type</div><div class="brief"><p class="paragraph">Defines the type of truck. By default, it is /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-type-s-t-r-a-i-g-h-t. Rendering <code class="lang-kotlin">sdk.mapview.TruckProfile</code>: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-truck-type is ignored and has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="weightPerAxleGroup" data-filterable-set=":modules:dokkaHtml/release" data-name="2106506472%2FProperties%2F1617540583" id="2106506472%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-weight-per-axle-group</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-weight-per-axle-group: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-weight-per-axle-group?</div><div class="brief"><p class="paragraph">Allows specification of axle weights in a more fine-grained way than <code class="lang-kotlin">weight_per_axle_in_kilograms</code>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. <strong>Note:</strong> <code class="lang-kotlin">weight_per_axle_in_kilograms</code> and <code class="lang-kotlin">weight_per_axle_group</code> are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an sdk.routing.RoutingError.INVALID_PARAMETER error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="weightPerAxleInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="-606214863%2FProperties%2F1617540583" id="-606214863%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-weight-per-axle-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-weight-per-axle-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. <strong>Note:</strong> <code class="lang-kotlin">weight_per_axle_in_kilograms</code> and <code class="lang-kotlin">weight_per_axle_group</code> are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an sdk.routing.RoutingError.INVALID_PARAMETER error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="widthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-1037982318%2FProperties%2F1617540583" id="-1037982318%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-width-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-width-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-554776209%2FFunctions%2F1617540583" id="-554776209%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1925920407%2FFunctions%2F1617540583" id="1925920407%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-specifications-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

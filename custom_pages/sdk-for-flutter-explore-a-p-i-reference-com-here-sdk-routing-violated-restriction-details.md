---
title: "Details"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/ViolatedRestriction.Details///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction/Details</div>
<div class="cover">
<h1 class="cover">Details</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details</div><p class="paragraph">Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member <code class="lang-kotlin">max_height_in_centimeters</code> will be set with the maximum allowed height value.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="Details" data-filterable-set=":modules:dokkaHtml/release" data-name="-2052023910%2FConstructors%2F1617540583" id="-2052023910%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-details</div>

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
<div class="table"><a anchor-label="forbiddenAxleCount" data-filterable-set=":modules:dokkaHtml/release" data-name="970598488%2FProperties%2F1617540583" id="970598488%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-axle-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-axle-count: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-integer-range?</div><div class="brief"><p class="paragraph">The restriction to trucks with axles number within specified range during the trip. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-axle-count is within this range.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forbiddenHazardousGoods" data-filterable-set=":modules:dokkaHtml/release" data-name="894386056%2FProperties%2F1617540583" id="894386056%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-hazardous-goods</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-hazardous-goods: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-hazardous-material&gt;</div><div class="brief"><p class="paragraph">There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-hazardous-materials from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-specification-vehicle-specification from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-transport-specification. This property is the intersection of the two lists.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forbiddenTrailerCount" data-filterable-set=":modules:dokkaHtml/release" data-name="641498791%2FProperties%2F1617540583" id="641498791%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-trailer-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-trailer-count: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-integer-range?</div><div class="brief"><p class="paragraph">Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-trailer-count is within this range.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forbiddenTruckCategory" data-filterable-set=":modules:dokkaHtml/release" data-name="-330865254%2FProperties%2F1617540583" id="-330865254%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-category</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-category: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-category?</div><div class="brief"><p class="paragraph">This property will be set if a restriction applies to the value of /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-category parameter used for route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forbiddenTruckRoadTypes" data-filterable-set=":modules:dokkaHtml/release" data-name="1954711273%2FProperties%2F1617540583" id="1954711273%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-road-types</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-road-types: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-road-type&gt;</div><div class="brief"><p class="paragraph">Contains violated restrictions for truck road types.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forbiddenTruckType" data-filterable-set=":modules:dokkaHtml/release" data-name="1237324894%2FProperties%2F1617540583" id="1237324894%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-forbidden-truck-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-type?</div><div class="brief"><p class="paragraph">This property will be set if a restriction applies to the value of /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-truck-type parameter used for route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxHeightInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-2116903997%2FProperties%2F1617540583" id="-2116903997%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-height-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-height-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Max permitted height during the trip, in centimeters. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-height-in-centimeters exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxKingpinToRearAxleDistanceInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-1206095340%2FProperties%2F1617540583" id="-1206095340%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-kingpin-to-rear-axle-distance-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-kingpin-to-rear-axle-distance-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-kingpin-to-rear-axle-distance-in-centimeters exceeds the specified value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxLengthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="1541013058%2FProperties%2F1617540583" id="1541013058%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-length-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-length-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Max permitted length during the trip, in centimeters. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-length-in-centimeters exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxNumberOfTires" data-filterable-set=":modules:dokkaHtml/release" data-name="969840343%2FProperties%2F1617540583" id="969840343%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-number-of-tires</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-number-of-tires: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Contains the maximum permitted number of tires. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-tires-count exceeds the specified value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxPayloadCapacityInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="922942186%2FProperties%2F1617540583" id="922942186%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-payload-capacity-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-payload-capacity-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Max permitted payload capacity during the trip, in kilograms. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-payload-capacity-in-kilograms exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxTunnelCategory" data-filterable-set=":modules:dokkaHtml/release" data-name="-1440761358%2FProperties%2F1617540583" id="-1440761358%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-tunnel-category</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-tunnel-category: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-tunnel-category?</div><div class="brief"><p class="paragraph">Tunnel category to restrict transport of specific goods during the trip. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-tunnel-category from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-specification-vehicle-specification from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options-transport-specification exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxWeight" data-filterable-set=":modules:dokkaHtml/release" data-name="1822752832%2FProperties%2F1617540583" id="1822752832%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-vehicle-restriction-max-weight?</div><div class="brief"><p class="paragraph">Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-gross-weight-in-kilograms parameter used for route calculation exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxWeightPerAxleGroupInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="-663192298%2FProperties%2F1617540583" id="-663192298%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight-per-axle-group-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight-per-axle-group-in-kilograms: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-max-axle-group-weight?</div><div class="brief"><p class="paragraph">Max permitted weight per axle group during the trip, in kilograms. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-weight-per-axle-group exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxWeightPerAxleInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="-1960102953%2FProperties%2F1617540583" id="-1960102953%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight-per-axle-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-weight-per-axle-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Max permitted weight per axle during the trip, in kilograms. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-weight-per-axle-in-kilograms exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxWidthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="245393592%2FProperties%2F1617540583" id="245393592%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-width-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-max-width-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Max permitted width during the trip, in centimeters. This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-vehicle-specification-width-in-centimeters exceeds this value.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routingZoneReference" data-filterable-set=":modules:dokkaHtml/release" data-name="-1901480795%2FProperties%2F1617540583" id="-1901480795%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-routing-zone-reference</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-routing-zone-reference: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Contains the restricted routing zone reference This property will be set if the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options-zone-categories is not empty</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="timeRule" data-filterable-set=":modules:dokkaHtml/release" data-name="-849809771%2FProperties%2F1617540583" id="-849809771%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-time-rule</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-time-rule: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-time-rule?</div><div class="brief"><p class="paragraph">Time intervals during which restrictions are enforced.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-806092957%2FFunctions%2F1617540583" id="-806092957%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1243069987%2FFunctions%2F1617540583" id="1243069987%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-violated-restriction-details-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

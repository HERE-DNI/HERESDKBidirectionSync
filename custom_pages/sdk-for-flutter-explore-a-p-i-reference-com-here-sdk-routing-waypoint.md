---
title: "Waypoint"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/Waypoint///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/Waypoint</div>
<div class="cover">
<h1 class="cover">Waypoint</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint</div><p class="paragraph">Represents a waypoint, used as input for route calculation.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="Waypoint" data-filterable-set=":modules:dokkaHtml/release" data-name="647429666%2FConstructors%2F1617540583" id="647429666%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-waypoint</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type, transitRadiusInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, headingInDegrees: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>?, sideOfStreetHint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates?, minCourseDistanceInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type, transitRadiusInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, headingInDegrees: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>?, sideOfStreetHint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates?, minCourseDistanceInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?, nameHint: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="chargingStop" data-filterable-set=":modules:dokkaHtml/release" data-name="1695154826%2FProperties%2F1617540583" id="1695154826%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-charging-stop</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-charging-stop: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop?</div><div class="brief"><p class="paragraph">Specifies of a user-planned charging stop. The resulting <code class="lang-kotlin">Route</code> may contain this waypoint as a <code class="lang-kotlin">RoutePlace</code> with a non-null <code class="lang-kotlin">ChargingStation</code> member when the provided specifications indicate that a stop is required to charge the EV battery. <strong>Note:</strong> If EVCarOptions.ensure_reachability is not set as <code class="lang-kotlin">true</code> and ChargingStop.min_duration is not provided, route calculation may suggest a better charging stop instead of this stop.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="coordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="-1319688030%2FProperties%2F1617540583" id="-1319688030%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates</div><div class="brief"><p class="paragraph">The waypoint's geographic coordinates.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="currentWeightChangeInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="1728784232%2FProperties%2F1617540583" id="1728784232%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-current-weight-change-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-current-weight-change-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Changes the value of <code class="lang-kotlin">vehicle[currentWeight]</code> by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren't supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). <strong>Note:</strong></p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="displayLocation" data-filterable-set=":modules:dokkaHtml/release" data-name="655527814%2FProperties%2F1617540583" id="655527814%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-display-location</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-display-location: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates?</div><div class="brief"><p class="paragraph">Optional coordinates to indicate physical location of the Points of Interest (PoI). It is different from coordinates and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-side-of-street-hint which are generally expected to to be on the navigable road network and can be different from actual location of the PoI. display_location is used for visualization of the PoI regardless of road network.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="duration" data-filterable-set=":modules:dokkaHtml/release" data-name="-1363904983%2FProperties%2F1617540583" id="-1363904983%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration</div><div class="brief"><p class="paragraph">The duration in seconds that should be spent at a waypoint of type /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type-s-t-o-p-o-v-e-r. Impacts time-aware calculations. Ignored for waypoints of type /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type-p-a-s-s-t-h-r-o-u-g-h. The default duration is 0 seconds.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="headingInDegrees" data-filterable-set=":modules:dokkaHtml/release" data-name="1296984797%2FProperties%2F1617540583" id="1296984797%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-heading-in-degrees</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-heading-in-degrees: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>?</div><div class="brief"><p class="paragraph">Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when <code class="lang-kotlin">null</code> is set, heading is ignored for route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="matchSideOfStreet" data-filterable-set=":modules:dokkaHtml/release" data-name="-908443289%2FProperties%2F1617540583" id="-908443289%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-match-side-of-street</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-match-side-of-street: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-match-side-of-street?</div><div class="brief"><p class="paragraph">Specifies how the location set by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-side-of-street-hint should be handled. Note that this setting might affect the geometry of the resulting route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="minCourseDistanceInMeters" data-filterable-set=":modules:dokkaHtml/release" data-name="2001808780%2FProperties%2F1617540583" id="2001808780%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-min-course-distance-in-meters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-min-course-distance-in-meters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="nameHint" data-filterable-set=":modules:dokkaHtml/release" data-name="1200566731%2FProperties%2F1617540583" id="1200566731%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-name-hint</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-name-hint: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: <code class="lang-kotlin">North</code> being used to differentiate between interstates <code class="lang-kotlin">I66 North</code> and <code class="lang-kotlin">I66 South</code>, <code class="lang-kotlin">Downtown Avenue</code> being used to correctly select a residential street.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onRoadThresholdInMeters" data-filterable-set=":modules:dokkaHtml/release" data-name="470398306%2FProperties%2F1617540583" id="470398306%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-on-road-threshold-in-meters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-on-road-threshold-in-meters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="segmentHint" data-filterable-set=":modules:dokkaHtml/release" data-name="726719267%2FProperties%2F1617540583" id="726719267%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-segment-hint</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-segment-hint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-segment-reference?</div><div class="brief"><p class="paragraph">Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="sideOfStreetHint" data-filterable-set=":modules:dokkaHtml/release" data-name="-1684623643%2FProperties%2F1617540583" id="-1684623643%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-side-of-street-hint</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-side-of-street-hint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates?</div><div class="brief"><p class="paragraph">Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-transit-radius-in-meters option with a value greater than zero.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="transitRadiusInMeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-89859639%2FProperties%2F1617540583" id="-89859639%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-transit-radius-in-meters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-transit-radius-in-meters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-side-of-street-hint option is ignored if the user sets this option with a value greater than zero.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="type" data-filterable-set=":modules:dokkaHtml/release" data-name="335412035%2FProperties%2F1617540583" id="335412035%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type</div><div class="brief"><p class="paragraph">Defines how a waypoint should be considered for route calculation. The default waypoint type is /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type-s-t-o-p-o-v-e-r.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-1914836252%2FFunctions%2F1617540583" id="-1914836252%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1366011266%2FFunctions%2F1617540583" id="1366011266%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

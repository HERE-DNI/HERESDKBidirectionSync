---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/Route///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/Route</div>
<div class="cover">
<h1 class="cover">Route</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">A route is a path through a road network over which someone travels.</p><p class="paragraph"><strong>Note:</strong> Each /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section of a route contains a list of /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section-notice objects that describe <i>potential issues</i> after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1112203752%2FClasslikes%2F1617540583" id="-1112203752%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="boundingBox" data-filterable-set=":modules:dokkaHtml/release" data-name="2007719978%2FProperties%2F1617540583" id="2007719978%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-bounding-box</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-bounding-box: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box</div><div class="brief"><p class="paragraph">The closest rectangular area where this route fits in.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="consumptionInKilowattHours" data-filterable-set=":modules:dokkaHtml/release" data-name="-1839867963%2FProperties%2F1617540583" id="-1839867963%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-consumption-in-kilowatt-hours</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-consumption-in-kilowatt-hours: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>?</div><div class="brief"><p class="paragraph">Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="duration" data-filterable-set=":modules:dokkaHtml/release" data-name="-1395398379%2FProperties%2F1617540583" id="-1395398379%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration</div><div class="brief"><p class="paragraph">The estimated time in seconds needed to travel along this route, including real-time traffic delays if available.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="geometry" data-filterable-set=":modules:dokkaHtml/release" data-name="441156599%2FProperties%2F1617540583" id="441156599%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-geometry</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polyline</div><div class="brief"><p class="paragraph">The /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polyline object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="language" data-filterable-set=":modules:dokkaHtml/release" data-name="1875961809%2FProperties%2F1617540583" id="1875961809%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-language</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-language: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code</div><div class="brief"><p class="paragraph">Indicates the language requested for all textual information related to this route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lengthInMeters" data-filterable-set=":modules:dokkaHtml/release" data-name="319684660%2FProperties%2F1617540583" id="319684660%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-length-in-meters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-length-in-meters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">The length of this route in meters.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="optimizationMode" data-filterable-set=":modules:dokkaHtml/release" data-name="1208140153%2FProperties%2F1617540583" id="1208140153%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-optimization-mode</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-optimization-mode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode</div><div class="brief"><p class="paragraph">The optimization mode requested for route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="railwayCrossings" data-filterable-set=":modules:dokkaHtml/release" data-name="-867674315%2FProperties%2F1617540583" id="-867674315%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-railway-crossings</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-railway-crossings: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-railway-crossing&gt;</div><div class="brief"><p class="paragraph">Collection of railway crossings along the route. Railway crossing information is only available for routes created with the online <code class="lang-kotlin">RoutingEngine</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="requestedTransportMode" data-filterable-set=":modules:dokkaHtml/release" data-name="1610450251%2FProperties%2F1617540583" id="1610450251%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-requested-transport-mode</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-requested-transport-mode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-mode</div><div class="brief"><p class="paragraph">The transport mode requested for route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeHandle" data-filterable-set=":modules:dokkaHtml/release" data-name="-906697952%2FProperties%2F1617540583" id="-906697952%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-route-handle</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-route-handle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-handle?</div><div class="brief"><p class="paragraph">The route handle of this route. Note that it is provided only if /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-enable-route-handle is set before route calculation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeLabels" data-filterable-set=":modules:dokkaHtml/release" data-name="948756777%2FProperties%2F1617540583" id="948756777%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-route-labels</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-route-labels: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-label&gt;</div><div class="brief"><p class="paragraph">A collection containing a maximum of 2 <code class="lang-kotlin">RouteLabel</code> instances for the route. It will return an empty list if no labels are available. The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via <code class="lang-kotlin">RouteOptions</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routingOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-295576783%2FProperties%2F1617540583" id="-295576783%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-routing-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-routing-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options?</div><div class="brief"><p class="paragraph">The set of options used to calculate the route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="sections" data-filterable-set=":modules:dokkaHtml/release" data-name="184932795%2FProperties%2F1617540583" id="184932795%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-sections</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-sections: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section&gt;</div><div class="brief"><p class="paragraph">The sections that make up this route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="trafficDelay" data-filterable-set=":modules:dokkaHtml/release" data-name="1578448739%2FProperties%2F1617540583" id="1578448739%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-traffic-delay</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-traffic-delay: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration</div><div class="brief"><p class="paragraph">The estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.</p></div></div></div>
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

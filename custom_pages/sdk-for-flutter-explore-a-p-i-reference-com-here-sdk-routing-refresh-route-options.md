---
title: "Refresh Route Options"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-refresh-route-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/RefreshRouteOptions///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/RefreshRouteOptions</div>
<div class="cover">
<h1 class="cover">Refresh<wbr/>Route<wbr/>Options</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-refresh-route-options : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the `RoutingOptions` class instead.</p></div><p class="paragraph">The options to specify how to refresh an already calculated route identified by a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-handle. All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-alternatives, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-arrival-time, and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-optimization-mode. If new /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options are specified, they are ignored as well and instead new /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section-notice's are generated that indicate where the requested /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options are violated. Note that when /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ensure-reachability is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="RefreshRouteOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="217179754%2FConstructors%2F1617540583" id="217179754%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-refresh-route-options-refresh-route-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(transportMode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-mode)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-transport-mode.</p></div><div class="symbol monospace">constructor(carOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-car-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-car-options.</p></div><div class="symbol monospace">constructor(truckOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-truck-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-truck-options.</p></div><div class="symbol monospace">constructor(pedestrianOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-pedestrian-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-pedestrian-options.</p></div><div class="symbol monospace">constructor(scooterOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-scooter-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-scooter-options.</p></div><div class="symbol monospace">constructor(taxiOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-taxi-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-taxi-options.</p></div><div class="symbol monospace">constructor(evCarOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options.</p></div><div class="symbol monospace">constructor(evTruckOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-truck-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-truck-options.</p></div><div class="symbol monospace">constructor(bicycleOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bicycle-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bicycle-options.</p></div><div class="symbol monospace">constructor(busOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bus-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bus-options.</p></div><div class="symbol monospace">constructor(privateBusOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-private-bus-options)</div><div class="brief"><p class="paragraph">Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-private-bus-options.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-913361935%2FClasslikes%2F1617540583" id="-913361935%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-refresh-route-options-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-refresh-route-options-companion</div></div></div>
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

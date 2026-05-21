---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/TransitRoutingEngine///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/TransitRoutingEngine</div>
<div class="cover">
<h1 class="cover">Transit<wbr/>Routing<wbr/>Engine</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between. Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.</p><p class="paragraph"><strong>Note</strong>: Clients need to explicitly call /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-dispose in order to prevent a possible, though unlikely, deadlock on destruction.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="TransitRoutingEngine" data-filterable-set=":modules:dokkaHtml/release" data-name="1824554203%2FConstructors%2F1617540583" id="1824554203%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-transit-routing-engine</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace">constructor(sdkEngine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine)</div><div class="brief"><p class="paragraph">Creates a new instance of TransitRoutingEngine.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1629989776%2FClasslikes%2F1617540583" id="-1629989776%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="calculateRoute" data-filterable-set=":modules:dokkaHtml/release" data-name="2080856513%2FFunctions%2F1617540583" id="2080856513%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-calculate-route</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-calculate-route(startingPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-waypoint, destination: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-waypoint, routeOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-route-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a public transit route from the origin to the destination.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="dispose" data-filterable-set=":modules:dokkaHtml/release" data-name="302455018%2FFunctions%2F1617540583" id="302455018%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-dispose</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-transit-routing-engine-dispose()</div><div class="brief"><p class="paragraph">Cancels pending requests and closes the background worker thread. <strong>Note:</strong> This method should be called from main thread.</p></div></div></div>
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

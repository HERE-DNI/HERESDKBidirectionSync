---
title: "Routing Interface"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/RoutingInterface///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/RoutingInterface</div>
<div class="cover">
<h1 class="cover">Routing<wbr/>Interface</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface</div><p class="paragraph">Provides the interface for the online and offline routing engines.</p><p class="paragraph"><strong>Note</strong>: Clients need to explicitly call /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-dispose in order to prevent a possible, though unlikely, deadlock on destruction.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-engine</div></div></div></div></div></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="calculateRoute" data-filterable-set=":modules:dokkaHtml/release" data-name="845384302%2FFunctions%2F1617540583" id="845384302%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, bicycleOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bicycle-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, busOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-bus-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, carOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-car-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, evCarOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, evTruckOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-truck-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, pedestrianOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-pedestrian-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, privateBusOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-private-bus-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, scooterOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-scooter-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, taxiOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-taxi-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-calculate-route(waypoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint&gt;, truckOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-truck-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="dispose" data-filterable-set=":modules:dokkaHtml/release" data-name="482140716%2FFunctions%2F1617540583" id="482140716%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-dispose</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-dispose()</div><div class="brief"><p class="paragraph">Cancels pending requests and closes the background worker thread. <strong>Note:</strong> This method should be called from main thread.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="returnToRoute" data-filterable-set=":modules:dokkaHtml/release" data-name="-590574508%2FFunctions%2F1617540583" id="-590574508%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-return-to-route</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface-return-to-route(route: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route, startingPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint, lastTraveledSectionIndex: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, traveledDistanceOnLastSectionInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.</p></div></div></div>
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

---
title: "return To Route"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-engine-return-to-route"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- return-to-route.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.routing/RoutingEngine/returnToRoute/#com.here.sdk.routing.Route#com.here.sdk.routing.Waypoint#kotlin.Int#kotlin.Int#com.here.sdk.routing.CalculateRouteCallback/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-engine/returnToRoute</div>
<div class="cover">
<h1 class="cover">return<wbr/>To<wbr/>Route</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-engine-return-to-route(route: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route, startingPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint, lastTraveledSectionIndex: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, traveledDistanceOnLastSectionInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-route-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><p class="paragraph">Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.</p><p class="paragraph"><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-alternatives, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-arrival-time, and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-optimization-mode. Most route options are only applied to the newly calculated part back to the route.</p><p class="paragraph">An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.</p><p class="paragraph">Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.</p><p class="paragraph">A typical use case is to await at least 3 <code class="lang-kotlin">RouteDeviation</code> events before calling this method.</p><ul><li><p class="paragraph">Or alternatively, wait at least 10 seconds after getting the first deviation event.</p></li><li><p class="paragraph">On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.</p></li><li><p class="paragraph">Optionally, it may make sense to verify if the vehicle was ever following the route by checking if <code class="lang-kotlin">RouteDeviation.lastLocationOnRoute</code> is set.</p></li></ul><p class="paragraph">Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.</p><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>route</u></div></div><div><div class="title"><p class="paragraph">A /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route calculated using the online or offline route engine. For the offline case, It     should not contain an indoor /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section as such routes will fail. For the online case, it     should have /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-handle.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>starting<wbr/>Point</u></div></div><div><div class="title"><p class="paragraph">The current location, for example, provided by a <code class="lang-kotlin">RouteDeviation</code> event. The waypoint needs to be of     type /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint-type-s-t-o-p-o-v-e-r. Otherwise, an /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-error-i-n-v-a-l-i-d-p-a-r-a-m-e-t-e-r     error is generated.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>last<wbr/>Traveled<wbr/>Section<wbr/>Index</u></div></div><div><div class="title"><p class="paragraph">Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>traveled<wbr/>Distance<wbr/>On<wbr/>Last<wbr/>Section<wbr/>In<wbr/>Meters</u></div></div><div><div class="title"><p class="paragraph">Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>callback</u></div></div><div><div class="title"><p class="paragraph">Callback object that will be invoked after route calculation.     It is always invoked on the main thread.</p></div></div></div></div></div></div></div>
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

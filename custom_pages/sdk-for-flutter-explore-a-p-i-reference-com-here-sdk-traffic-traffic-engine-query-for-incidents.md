---
title: "query For Incidents"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- query-for-incidents.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.traffic/TrafficEngine/queryForIncidents/#com.here.sdk.core.GeoBox#com.here.sdk.traffic.TrafficIncidentsQueryOptions#com.here.sdk.traffic.TrafficIncidentsQueryCallback/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine/queryForIncidents</div>
<div class="cover">
<h1 class="cover">query<wbr/>For<wbr/>Incidents</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(boxArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><p class="paragraph">Asynchronously queries for traffic incidents using a bounding box as a filter.</p><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>box<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">The bounding box area to search for traffic incidents.     The maximum width and height for a bounding box filter is 1 degree.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>query<wbr/>Options</u></div></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>callback</u></div></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div><hr/><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(circleArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><p class="paragraph">Asynchronously queries for traffic incidents using a circle as a filter.</p><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>circle<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">The circle area to search for traffic incidents.     The maximum radius of the circle filter is 50000 meters.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>query<wbr/>Options</u></div></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>callback</u></div></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div><hr/><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(corridorArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><p class="paragraph">Asynchronously queries for traffic incidents by a corridor as a filter.</p><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>corridor<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">The corridor box to search for traffic incidents.     The maximum length for the corridor is 500000 meters and the maximum <code class="lang-kotlin">GeoCorridor.half_width_in_meters</code> is 5000 meters.     If the number of points in corridor is greater than 300 then request is split into smaller ones and results are     aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">To reduce number of points in the corridor use [com.here.sdk.core.PolylineSimplifier].

If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>query<wbr/>Options</u></div></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>callback</u></div></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div></div></div>
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

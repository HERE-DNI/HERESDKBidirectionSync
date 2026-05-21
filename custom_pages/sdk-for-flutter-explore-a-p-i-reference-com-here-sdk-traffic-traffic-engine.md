---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.traffic/TrafficEngine///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic/TrafficEngine</div>
<div class="cover">
<h1 class="cover">Traffic<wbr/>Engine</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor. Provides optional parameters given in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-options to filter the result.</p><p class="paragraph">By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.</p><p class="paragraph">The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.</p><p class="paragraph">Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine-pass-through-features</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="TrafficEngine" data-filterable-set=":modules:dokkaHtml/release" data-name="-1818046149%2FConstructors%2F1617540583" id="-1818046149%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-traffic-engine</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace">constructor(sdkEngine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine)</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-60290133%2FClasslikes%2F1617540583" id="-60290133%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="lookupIncident" data-filterable-set=":modules:dokkaHtml/release" data-name="-1336384619%2FFunctions%2F1617540583" id="-1336384619%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-lookup-incident</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-lookup-incident(originalId: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, lookupOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incident-lookup-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incident-lookup-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic incident by the original id. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incident-original-id for more information.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="queryForFlow" data-filterable-set=":modules:dokkaHtml/release" data-name="1653310548%2FFunctions%2F1617540583" id="1653310548%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-flow</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-flow(boxArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic flow using a bounding box as a filter.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-flow(circleArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic flow using a circle as a filter.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-flow(corridorArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-flow-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic flow by a corridor as a filter.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="queryForIncidents" data-filterable-set=":modules:dokkaHtml/release" data-name="236008499%2FFunctions%2F1617540583" id="236008499%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(boxArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic incidents using a bounding box as a filter.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(circleArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic incidents using a circle as a filter.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-engine-query-for-incidents(corridorArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor, queryOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incidents-query-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously queries for traffic incidents by a corridor as a filter.</p></div></div></div>
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

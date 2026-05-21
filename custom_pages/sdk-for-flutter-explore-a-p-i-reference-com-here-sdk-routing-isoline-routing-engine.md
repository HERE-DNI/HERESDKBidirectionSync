---
title: "Isoline Routing Engine"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/IsolineRoutingEngine///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/IsolineRoutingEngine</div>
<div class="cover">
<h1 class="cover">Isoline<wbr/>Routing<wbr/>Engine</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Use the IsolineRoutingEngine to calculate a reachable area from a center point. The calculation is done asynchronously and requires an online connection.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="IsolineRoutingEngine" data-filterable-set=":modules:dokkaHtml/release" data-name="-911895903%2FConstructors%2F1617540583" id="-911895903%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-isoline-routing-engine</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace">constructor(connectionSettings: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-connection-settings)</div><div class="brief"><p class="paragraph">Creates a new instance of RoutingEngine.</p></div><div class="symbol monospace">constructor(sdkEngine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine, connectionSettings: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-connection-settings)</div><div class="brief"><p class="paragraph">Creates a new instance of RoutingEngine.</p></div><div class="symbol monospace">constructor(sdkEngine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine)</div><div class="brief"><p class="paragraph">Creates a new instance of IsolineRoutingEngine.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="1806284950%2FClasslikes%2F1617540583" id="1806284950%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="calculateIsoline" data-filterable-set=":modules:dokkaHtml/release" data-name="1506248043%2FFunctions%2F1617540583" id="1506248043%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-calculate-isoline</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-calculate-isoline(center: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-waypoint, isolineOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-calculate-isoline-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Asynchronously calculates isolines to indicate the reachable area from a center point. This finds all destinations that can be reached in a specific amount of time, a maximum travel distance, or even the charge level available in an electric vehicle. The result is a polygon area where each point is reachable within the provided limit.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setCustomOption" data-filterable-set=":modules:dokkaHtml/release" data-name="-366491999%2FFunctions%2F1617540583" id="-366491999%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-set-custom-option</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-routing-engine-set-custom-option(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-error?</div><div class="brief"><p class="paragraph">Sets a custom option for routing backend queries. The custom option is applied to all the queries that <code class="lang-kotlin">IsolineRoutingEngine</code> performs. For a complete list of available parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>. <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.</p></div></div></div>
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

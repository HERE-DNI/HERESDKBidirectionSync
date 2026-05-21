---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon-geo-polygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -geo-polygon.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.core/GeoPolygon/GeoPolygon/#kotlin.collections.List[com.here.sdk.core.GeoCoordinates]/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon/GeoPolygon</div>
<div class="cover">
<h1 class="cover">Geo<wbr/>Polygon</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(vertices: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates&gt;)</div><p class="paragraph">Constructs an instance of this class from the provided vertices. Throws InstantiationError if the number of vertices is less than three.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>vertices</u></div></div><div><div class="title"><p class="paragraph">List of vertices representing the polygon outer boundary in clockwise order.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-errors-instantiation-error-exception</div></div><div><div class="title"><p class="paragraph">Instantiation error.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(vertices: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates&gt;, innerBoundaries: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates&gt;&gt;)</div><p class="paragraph">Constructs an instance of this class from the provided vertices and inner boundaries (holes). Throws InstantiationError if the number of vertices is less than three.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>vertices</u></div></div><div><div class="title"><p class="paragraph">List of vertices representing the polygon outer boundary in clockwise order.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>inner<wbr/>Boundaries</u></div></div><div><div class="title"><p class="paragraph">List of polygon inner boundaries (holes), each in counterclockwise order.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-errors-instantiation-error-exception</div></div><div><div class="title"><p class="paragraph">Instantiation error.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(geoCircle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle)</div><p class="paragraph">Constructs an instance of this class from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geo<wbr/>Circle</u></div></div><div><div class="title"><p class="paragraph">A /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle to be converted into /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(geoBox: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box)</div><p class="paragraph">Constructs an instance of this class from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geo<wbr/>Box</u></div></div><div><div class="title"><p class="paragraph">A rectangle defined by the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box to be converted into /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon.     The corner coordinates defined by the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box will define the outer boundary verticies of the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon.</p></div></div></div></div></div></div></div>
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

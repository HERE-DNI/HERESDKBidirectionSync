---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query-area-area"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -area.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.search/CategoryQuery.Area/Area/#com.here.sdk.core.GeoCoordinates/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query-area/Area</div>
<div class="cover">
<h1 class="cover">Area</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(areaCenter: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates)</div><p class="paragraph">Constructs a new instance of this class from provided parameters.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>area<wbr/>Center</u></div></div><div><div class="title"><p class="paragraph">Geographic coordinates of the center around which to provide the most relevant places.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(areaCenter: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, boxArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box)</div><p class="paragraph">Constructs a new instance of this class from provided parameters.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>area<wbr/>Center</u></div></div><div><div class="title"><p class="paragraph">Geographic coordinates of the center around which to provide the most relevant places.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>box<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">Geographic rectangle area in which to provide the most relevant places.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(areaCenter: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, circleArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle)</div><p class="paragraph">Constructs a new instance of this class from provided parameters.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>area<wbr/>Center</u></div></div><div><div class="title"><p class="paragraph">Geographic coordinates of the center around which to provide the most relevant places.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>circle<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">Geographic circle area in which to provide the most relevant places.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(corridorArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor, areaCenter: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates)</div><p class="paragraph">Constructs a new instance of this class from provided parameters. The given corridor and center define the area that will be used in the search query.</p><p class="paragraph">When used with <code class="lang-kotlin">SearchEngine</code>, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p><p class="paragraph">The area center has to be within the corridor, otherwise it is ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>corridor<wbr/>Area</u></div></div><div><div class="title"><p class="paragraph">Geographic corridor area in which to provide the most relevant places.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>area<wbr/>Center</u></div></div><div><div class="title"><p class="paragraph">Geographic coordinates of the prioritized area center.</p></div></div></div></div></div></div></div>
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

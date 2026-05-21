---
title: "Map Polygon"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-map-polygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -map-polygon.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapPolygon/MapPolygon/#com.here.sdk.core.GeoPolygon#com.here.sdk.core.Color/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon/MapPolygon</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Polygon</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color)</div><p class="paragraph">Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</p><p class="paragraph">The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.</p><p class="paragraph">Note:</p><ul><li><p class="paragraph">The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.</p></li><li><p class="paragraph">Polygons which are self-intersecting are not supported and may lead to render artifacts.</p></li><li><p class="paragraph">The inner boundaries (holes) specified in the GeoPolygon are ignored.</p></li></ul><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geometry</u></div></div><div><div class="title"><p class="paragraph">The list of vertices representing the outer boundary of polygon.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>color</u></div></div><div><div class="title"><p class="paragraph">The fill color for the polygon</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color, outlineColor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color, outlineWidthInPixels: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><p class="paragraph">Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</p><p class="paragraph">Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque by interpreting the alpha value as 1.</p><p class="paragraph">The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.</p><p class="paragraph">Note:</p><ul><li><p class="paragraph">The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.</p></li><li><p class="paragraph">Polygons which are self-intersecting are not supported and may lead to render artifacts.</p></li><li><p class="paragraph">The inner boundaries (holes) specified in the GeoPolygon are ignored.</p></li></ul><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geometry</u></div></div><div><div class="title"><p class="paragraph">The list of vertices representing the outer boundary of polygon.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>color</u></div></div><div><div class="title"><p class="paragraph">The fill color for the polygon.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>outline<wbr/>Color</u></div></div><div><div class="title"><p class="paragraph">The color of the polygon outline, alpha channel is ignored and treated as 1.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>outline<wbr/>Width<wbr/>In<wbr/>Pixels</u></div></div><div><div class="title"><p class="paragraph">The width of the polygon outline (in pixels). Negative values are clamped to 0.</p></div></div></div></div></div></div></div>
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

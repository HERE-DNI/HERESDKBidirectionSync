---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapPolygon///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapPolygon</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Polygon</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">A visual representation of a polygon on the map. Can be used to visualize areas of all shapes and sizes.</p><p class="paragraph">The geometry to be visualized is represented by an instance of /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon. To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle using com.here.sdk.core.GeoPolygon.GeoPolygon.</p><p class="paragraph">Note:</p><ul><li><p class="paragraph">The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.</p></li><li><p class="paragraph">Polygons which are self-intersecting are not supported and may lead to render artifacts.</p></li><li><p class="paragraph">The inner boundaries (holes) specified in the GeoPolygon are ignored.</p></li></ul></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapPolygon" data-filterable-set=":modules:dokkaHtml/release" data-name="1102408381%2FConstructors%2F1617540583" id="1102408381%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-map-polygon</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color)</div><div class="brief"><p class="paragraph">Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</p></div><div class="symbol monospace">constructor(geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color, outlineColor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color, outlineWidthInPixels: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-411910238%2FClasslikes%2F1617540583" id="-411910238%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="drawOrder" data-filterable-set=":modules:dokkaHtml/release" data-name="-1204566735%2FProperties%2F1617540583" id="-1204566735%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-draw-order</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-draw-order: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">The draw order of this map polygon relative to other map polygons.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="fillColor" data-filterable-set=":modules:dokkaHtml/release" data-name="-107282757%2FProperties%2F1617540583" id="-107282757%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-fill-color</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-fill-color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color</div><div class="brief"><p class="paragraph">Color of the polygon's fill.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="geometry" data-filterable-set=":modules:dokkaHtml/release" data-name="1156483373%2FProperties%2F1617540583" id="1156483373%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-geometry</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-geometry: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polygon</div><div class="brief"><p class="paragraph">The geometry of the polygon. Setting a new geometry will update the appearance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="metadata" data-filterable-set=":modules:dokkaHtml/release" data-name="-706759408%2FProperties%2F1617540583" id="-706759408%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-metadata</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-metadata: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-metadata?</div><div class="brief"><p class="paragraph">The Metadata instance attached to this polygon, <code class="lang-kotlin">null</code> by default.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="outlineColor" data-filterable-set=":modules:dokkaHtml/release" data-name="-768870594%2FProperties%2F1617540583" id="-768870594%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-outline-color</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-outline-color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color</div><div class="brief"><p class="paragraph">The color of the polygon outline.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="outlineWidth" data-filterable-set=":modules:dokkaHtml/release" data-name="1834606139%2FProperties%2F1617540583" id="1834606139%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-outline-width</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-outline-width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The width of the polygon outline in pixels.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="visibilityRanges" data-filterable-set=":modules:dokkaHtml/release" data-name="378850263%2FProperties%2F1617540583" id="378850263%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-visibility-ranges</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon-visibility-ranges: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-range&gt;</div><div class="brief"><p class="paragraph">The list of visibility ranges. The map polygon is visible only inside these map measure ranges.</p></div></div></div>
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

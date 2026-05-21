---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-raster-data-source-configuration-provider-provider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -provider.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview.datasource/RasterDataSourceConfiguration.Provider/Provider/#com.here.sdk.mapview.datasource.TileUrlProviderCallback#com.here.sdk.mapview.datasource.TilingScheme#kotlin.collections.List[kotlin.Int]#kotlin.Boolean#kotlin.collections.Map[kotlin.String,kotlin.String]?/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-raster-data-source-configuration//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-raster-data-source-configuration-provider/Provider</div>
<div class="cover">
<h1 class="cover">Provider</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(urlProvider: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-tile-url-provider-callback, tilingScheme: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-tiling-scheme, storageLevels: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>&gt;, hasAlphaChannel: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>, headers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>&gt;?)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>url<wbr/>Provider</u></div></div><div><div class="title"><p class="paragraph">Provides a function that generates URLs based on tile coordinates and storage level.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>tiling<wbr/>Scheme</u></div></div><div><div class="title"><p class="paragraph">The tiling scheme used by this source.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>storage<wbr/>Levels</u></div></div><div><div class="title"><p class="paragraph">The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>has<wbr/>Alpha<wbr/>Channel</u></div></div><div><div class="title"><p class="paragraph">A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code class="lang-kotlin">false</code>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>headers</u></div></div><div><div class="title"><p class="paragraph">The optional name-value pairs specifying HTTP headers that are passed with each tile request.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(urlProvider: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-tile-url-provider-callback, tilingScheme: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-tiling-scheme, storageLevels: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>&gt;)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>url<wbr/>Provider</u></div></div><div><div class="title"><p class="paragraph">Provides a function that generates URLs based on tile coordinates and storage level.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>tiling<wbr/>Scheme</u></div></div><div><div class="title"><p class="paragraph">The tiling scheme used by this source.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>storage<wbr/>Levels</u></div></div><div><div class="title"><p class="paragraph">The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.</p></div></div></div></div></div></div></div>
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

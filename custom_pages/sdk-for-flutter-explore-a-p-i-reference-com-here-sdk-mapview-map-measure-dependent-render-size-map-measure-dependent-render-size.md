---
title: "Map Measure Dependent Render Size"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size-map-measure-dependent-render-size"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -map-measure-dependent-render-size.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapMeasureDependentRenderSize/MapMeasureDependentRenderSize/#com.here.sdk.mapview.MapMeasure.Kind#com.here.sdk.mapview.RenderSize.Unit#kotlin.collections.Map[kotlin.Double,kotlin.Double]/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size/MapMeasureDependentRenderSize</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Measure<wbr/>Dependent<wbr/>Render<wbr/>Size</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(measureKind: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-kind, sizeUnit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit, sizes: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>&gt;)</div><p class="paragraph">Constructs a <code class="lang-kotlin">MapMeasureDependentRenderSize</code> from given parameters.</p><p class="paragraph">Supplying <code class="lang-kotlin">sizes</code> map with a single entry indicates using a fixed size value across all map measures.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>measure<wbr/>Kind</u></div></div><div><div class="title"><p class="paragraph">The unit used for the key in <code class="lang-kotlin">sizes</code>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>size<wbr/>Unit</u></div></div><div><div class="title"><p class="paragraph">The unit used for the value in <code class="lang-kotlin">sizes</code>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>sizes</u></div></div><div><div class="title"><p class="paragraph">The dictionary describing the size (value) per map measure (key).</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size-instantiation-exception</div></div><div><div class="title"><p class="paragraph">Instantiation error if <code class="lang-kotlin">sizes</code> map is empty or contains negative keys or values.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(sizeUnit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit, size: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><p class="paragraph">Constructs a <code class="lang-kotlin">MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.</p><p class="paragraph">The given <code class="lang-kotlin">size</code> value is stored in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size-sizes map at key 0 and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size-measure-kind is set to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-kind-z-o-o-m-l-e-v-e-l.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>size<wbr/>Unit</u></div></div><div><div class="title"><p class="paragraph">The unit used for the value in <code class="lang-kotlin">size</code>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>size</u></div></div><div><div class="title"><p class="paragraph">The size independent of map measure. Must not be negative.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size-instantiation-exception</div></div><div><div class="title"><p class="paragraph">Instantiation error if <code class="lang-kotlin">size</code> is negative.</p></div></div></div></div></div></div></div>
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

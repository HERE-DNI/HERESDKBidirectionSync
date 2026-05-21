---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapPolyline.SolidMultiColorRepresentation///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline/SolidMultiColorRepresentation</div>
<div class="cover">
<h1 class="cover">Solid<wbr/>Multi<wbr/>Color<wbr/>Representation</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation : /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-representation</div><p class="paragraph">Representation allows map polyline to be colored in multiple specified color segments.</p><p class="paragraph">Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.</p><p class="paragraph">Progress color <code class="lang-kotlin">MapPolyline.progressColor</code> overrides any of the multiple color.</p><p class="paragraph">Examples: The following configuration will color map polyline as follows:</p><ul><li><p class="paragraph">from the start to the middle of it at the 0.5 point - in Red</p></li><li><p class="paragraph">from the middle point 0.5 to the 0.7 point - in Green</p></li><li><p class="paragraph">from 0.7 to 1.0 - in Red 'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'</p></li></ul><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="SolidMultiColorRepresentation" data-filterable-set=":modules:dokkaHtml/release" data-name="2073598289%2FConstructors%2F1617540583" id="2073598289%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-solid-multi-color-representation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(lineWidth: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, capShape: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-line-cap, colorStops: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>&gt;, colorIndices: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>&gt;, colors: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color&gt;, gradientLength: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Creates a representation for a multicolored line without an outline.</p></div><div class="symbol monospace">constructor(lineWidth: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, outlineWidth: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, outlineColor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color, capShape: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-line-cap, colorStops: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>&gt;, colorIndices: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>&gt;, colors: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color&gt;, gradientLength: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Creates a representation for a multicolored line with an outline.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="722848534%2FClasslikes%2F1617540583" id="722848534%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="setMultiColorGradientLength" data-filterable-set=":modules:dokkaHtml/release" data-name="1678778327%2FFunctions%2F1617540583" id="1678778327%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-set-multi-color-gradient-length</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-set-multi-color-gradient-length(length: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Sets the multiple color segment gradient length.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setMultiColors" data-filterable-set=":modules:dokkaHtml/release" data-name="2098660190%2FFunctions%2F1617540583" id="2098660190%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-set-multi-colors</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation-set-multi-colors(colorStops: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>&gt;, colorIndices: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>&gt;, colors: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color&gt;): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Sets lists of colors and multiple color segment stops for the polyline to be colored in. When this representation is already set on any <code class="lang-kotlin">MapPolyline</code>, values will be applied on that <code class="lang-kotlin">MapPolyline</code> right away. If this representation is not set on any <code class="lang-kotlin">MapPolyline</code>, values will be applied once representation is set on a <code class="lang-kotlin">MapPolyline</code>.</p></div></div></div>
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

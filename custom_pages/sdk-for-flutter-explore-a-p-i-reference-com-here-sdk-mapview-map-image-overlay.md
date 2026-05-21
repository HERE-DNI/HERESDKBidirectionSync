---
title: "Map Image Overlay"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapImageOverlay///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapImageOverlay</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Image<wbr/>Overlay</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph"><code class="lang-kotlin">MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.</p><p class="paragraph">The image to be displayed is represented by a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image object. By default, the overlay is centered on the given view coordinate.</p><p class="paragraph">The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate, the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.</p><p class="paragraph">To display the map overlay, it needs to be added to the scene using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-image-overlay. To stop displaying it, remove it from the scene using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-image-overlay.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapImageOverlay" data-filterable-set=":modules:dokkaHtml/release" data-name="1978251138%2FConstructors%2F1617540583" id="1978251138%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-map-image-overlay</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(viewCoordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image)</div><div class="brief"><p class="paragraph">Creates an instance of an overlay at given view coordinates, represented by specified image.</p></div><div class="symbol monospace">constructor(viewCoordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d)</div><div class="brief"><p class="paragraph">Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay's view coordinates.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1491533099%2FClasslikes%2F1617540583" id="-1491533099%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="anchor" data-filterable-set=":modules:dokkaHtml/release" data-name="489722487%2FProperties%2F1617540583" id="489722487%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-anchor</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d</div><div class="brief"><p class="paragraph">The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="drawOrder" data-filterable-set=":modules:dokkaHtml/release" data-name="2010777700%2FProperties%2F1617540583" id="2010777700%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-draw-order</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-draw-order: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">Draw order of this <code class="lang-kotlin">MapImageOverlay</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="image" data-filterable-set=":modules:dokkaHtml/release" data-name="1372308755%2FProperties%2F1617540583" id="1372308755%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-image</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image</div><div class="brief"><p class="paragraph">Image overlayed on the map.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="viewCoordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="1937684344%2FProperties%2F1617540583" id="1937684344%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-view-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay-view-coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d</div><div class="brief"><p class="paragraph">The view point in pixels on the map viewport where the map overlay is drawn.</p></div></div></div>
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

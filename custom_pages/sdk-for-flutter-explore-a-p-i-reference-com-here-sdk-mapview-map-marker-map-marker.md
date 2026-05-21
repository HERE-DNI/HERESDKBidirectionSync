---
title: "Map Marker"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-map-marker"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -map-marker.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapMarker/MapMarker/#com.here.sdk.core.GeoCoordinates#com.here.sdk.mapview.MapImage/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker/MapMarker</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Marker</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image)</div><p class="paragraph">Creates an instance of a marker at given coordinates, represented by specified image.</p><p class="paragraph">The altitude component of the coordinates is ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>coordinates</u></div></div><div><div class="title"><p class="paragraph">The marker's geographical coordinates.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image</u></div></div><div><div class="title"><p class="paragraph">The image to draw on the map.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, text: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><p class="paragraph">Creates a <code class="lang-kotlin">MapMarker</code> instance at given coordinates with specified image and text and a default text style.</p><p class="paragraph">The altitude component of the coordinates is ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>coordinates</u></div></div><div><div class="title"><p class="paragraph">The marker's geographical coordinates.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image</u></div></div><div><div class="title"><p class="paragraph">The image to draw on the map.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>text</u></div></div><div><div class="title"><p class="paragraph">The text to draw on the map.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d)</div><p class="paragraph">Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.</p><p class="paragraph">The anchor is a way of specifying position offset relative to image's dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the marker's coordinates. (1, 1) would place the bottom-right corner of the image at the marker's coordinates. (0.5, 0.5) which is the default value would center the image at the marker's coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker's coordinates at the distance in pixels that is equal to the height of the image.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>coordinates</u></div></div><div><div class="title"><p class="paragraph">The marker's geographical coordinates.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image</u></div></div><div><div class="title"><p class="paragraph">The image to draw on the map.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>anchor</u></div></div><div><div class="title"><p class="paragraph">The anchor point for the marker image which specifies the position offset relative     to the marker's coordinates.</p></div></div></div></div></div></div></div>
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

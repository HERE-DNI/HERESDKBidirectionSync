---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-map-image"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -map-image.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapImage/MapImage/#kotlin.ByteArray#com.here.sdk.mapview.ImageFormat/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image/MapImage</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Image</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(pixelData: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html">ByteArray</a>, imageFormat: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-image-format)</div><p class="paragraph">Creates a new map image from the provided image data. Currently only /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-image-format-p-n-g is accepted.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>pixel<wbr/>Data</u></div></div><div><div class="title"><p class="paragraph">Data to be used for the image. The bytes of a PNG image datastream are expected as     defined in https://www.w3.org/TR/PNG</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image<wbr/>Format</u></div></div><div><div class="title"><p class="paragraph">The format of the image data to be used.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(imageData: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html">ByteArray</a>, imageFormat: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-image-format, width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>, height: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><p class="paragraph">Creates a new map image from the provided image data.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image<wbr/>Data</u></div></div><div><div class="title"><p class="paragraph">Data to be used for the image. For image format /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-image-format-s-v-g the bytes     of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification     see https://www.w3.org/TR/SVGTiny12</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>image<wbr/>Format</u></div></div><div><div class="title"><p class="paragraph">The format of the image data to be used.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>width</u></div></div><div><div class="title"><p class="paragraph">The width of the image in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>height</u></div></div><div><div class="title"><p class="paragraph">The height of the image in pixels.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(filePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>, height: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><p class="paragraph">Creates a new map image from the provided path to the SVG Tiny or PNG image.</p><p class="paragraph">Will throw an error if either the height or width equals zero or the path is empty.</p><p class="paragraph">Trying to load a file that is not compliant with SVG Tiny or PNG results in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG specification may result in an image that exhibits unexpected artifacts.</p><p class="paragraph">The caller must ensure that the file remains accessible for the entire duration of its usage by the SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that remains accessible for the entire duration of its usage by the SDK or load and pass the file content to one of the <code class="lang-kotlin">MapImage</code> constructors that creates instances out of image data (com.here.sdk.mapview.MapImage.MapImage, com.here.sdk.mapview.MapImage.MapImage).}</p><p class="paragraph">This constructor needs read storage permission to be granted.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>file<wbr/>Path</u></div></div><div><div class="title"><p class="paragraph">The path to image file.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>width</u></div></div><div><div class="title"><p class="paragraph">The width of image in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>height</u></div></div><div><div class="title"><p class="paragraph">The height of image in pixels.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-errors-instantiation-error-exception</div></div><div><div class="title"><p class="paragraph">Indicates what went wrong when the instantiation was attempted.</p></div></div></div></div></div></div></div>
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

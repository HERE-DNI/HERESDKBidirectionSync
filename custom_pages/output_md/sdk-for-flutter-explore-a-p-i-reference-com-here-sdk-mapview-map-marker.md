---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapMarker///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapMarker</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Marker</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph"><code class="lang-kotlin">MapMarker</code> is used to draw images on the map, for example to mark a specific location. By default, the marker is centered on the given geographic coordinates. Markers keep their size regardless of the current zoom level of the map view.</p><p class="paragraph">The image to be displayed is represented by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image object. For performance reasons, it is highly recommended to reuse a single instance of the image when creating multiple identical markers.</p><p class="paragraph">To display the map marker, it needs to be added to the scene using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker. To stop displaying it, remove it from the scene using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker.</p><p class="paragraph">The display of a map marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects map markers which are visually large and cover a sizeable part of the viewport.</p><p class="paragraph"><strong>Note:</strong> Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation the following approach can be used: Register to map camera updates using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-add-listener. Query the bounding box of the camera viewport using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-bounding-box (it may be extended) and then use the method /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box-contains in combination with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state-distance-to-target-in-meters to determine which MapMarkers are actually visible to the user in the current camera viewport and thus need to be added to the map.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapMarker" data-filterable-set=":modules:dokkaHtml/release" data-name="-1718288520%2FConstructors%2F1617540583" id="-1718288520%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-map-marker</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image)</div><div class="brief"><p class="paragraph">Creates an instance of a marker at given coordinates, represented by specified image.</p></div><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, text: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a <code class="lang-kotlin">MapMarker</code> instance at given coordinates with specified image and text and a default text style.</p></div><div class="symbol monospace">constructor(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d)</div><div class="brief"><p class="paragraph">Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-330122192%2FClasslikes%2F1617540583" id="-330122192%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="TextStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="2107546040%2FClasslikes%2F1617540583" id="2107546040%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text-style : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><div class="brief"><p class="paragraph">Styling options for the text of a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="anchor" data-filterable-set=":modules:dokkaHtml/release" data-name="651808508%2FProperties%2F1617540583" id="651808508%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-anchor</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d</div><div class="brief"><p class="paragraph">The anchor point for the marker image which specifies the position offset relative to the marker's coordinates.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="coordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="1019491918%2FProperties%2F1617540583" id="1019491918%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates</div><div class="brief"><p class="paragraph">The point on the map where the map marker is drawn.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="drawOrder" data-filterable-set=":modules:dokkaHtml/release" data-name="-1122778689%2FProperties%2F1617540583" id="-1122778689%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-draw-order</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-draw-order: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">The draw order of this marker relative to other markers.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="fadeDuration" data-filterable-set=":modules:dokkaHtml/release" data-name="-496843039%2FProperties%2F1617540583" id="-496843039%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-fade-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-fade-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration</div><div class="brief"><p class="paragraph">Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="image" data-filterable-set=":modules:dokkaHtml/release" data-name="-1116314642%2FProperties%2F1617540583" id="-1116314642%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-image</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image</div><div class="brief"><p class="paragraph">Image representing the marker on the screen.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isOverlapAllowed" data-filterable-set=":modules:dokkaHtml/release" data-name="-939902394%2FProperties%2F1617540583" id="-939902394%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-is-overlap-allowed</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-is-overlap-allowed: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Determines whether or not the marker can overlap other markers.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isTextOptional" data-filterable-set=":modules:dokkaHtml/release" data-name="-786570758%2FProperties%2F1617540583" id="-786570758%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-is-text-optional</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-is-text-optional: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Determines if the marker can be displayed with icon and without text.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="metadata" data-filterable-set=":modules:dokkaHtml/release" data-name="1374088898%2FProperties%2F1617540583" id="1374088898%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-metadata</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-metadata: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-metadata?</div><div class="brief"><p class="paragraph">The Metadata instance attached to this marker, see /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-metadata.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="opacity" data-filterable-set=":modules:dokkaHtml/release" data-name="-1222942658%2FProperties%2F1617540583" id="-1222942658%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-opacity</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-opacity: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">Opacity, the factor applied to the alpha channel of the marker image.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="text" data-filterable-set=":modules:dokkaHtml/release" data-name="1767999620%2FProperties%2F1617540583" id="1767999620%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The text to be drawn on the map along with the image of the <code class="lang-kotlin">MapMarker</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="textStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="-1201853723%2FProperties%2F1617540583" id="-1201853723%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text-style: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-text-style</div><div class="brief"><p class="paragraph">The <code class="lang-kotlin">TextStyle</code> applied to the text of the <code class="lang-kotlin">MapMarker</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="visibilityRanges" data-filterable-set=":modules:dokkaHtml/release" data-name="-269995127%2FProperties%2F1617540583" id="-269995127%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-visibility-ranges</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-visibility-ranges: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-range&gt;</div><div class="brief"><p class="paragraph">The list of visibility ranges. The map marker is visible only inside these map measure ranges.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="cancelAnimation" data-filterable-set=":modules:dokkaHtml/release" data-name="-189807290%2FFunctions%2F1617540583" id="-189807290%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cancel-animation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cancel-animation(animation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-map-marker-animation)</div><div class="brief"><p class="paragraph">Cancels single ongoing animation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="startAnimation" data-filterable-set=":modules:dokkaHtml/release" data-name="-1877535773%2FFunctions%2F1617540583" id="-1877535773%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-start-animation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-start-animation(animation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-map-marker-animation, animationListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-animation-listener?)</div><div class="brief"><p class="paragraph">Starts animation of this map marker according to provided /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-map-marker-animation.</p></div></div></div>
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

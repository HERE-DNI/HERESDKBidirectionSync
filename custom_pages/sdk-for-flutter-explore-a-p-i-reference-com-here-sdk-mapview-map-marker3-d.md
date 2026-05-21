---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapMarker3D///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapMarker3D</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Marker3D</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Represents a 3D shape drawn on the map at specified geodetic coordinates.</p><p class="paragraph">It can have a solid color or be textured, depending on the data from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model.</p><p class="paragraph">By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-is-depth-check-enabled.</p><p class="paragraph">The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.</p><h1 class="">Sizing and scaling</h1><p class="paragraph">Two aspects determine how big the <code class="lang-kotlin">MapMarker3D</code> will be on the screen and how will it behave when the map is zoomed in and out.</p><p class="paragraph">The first, and most impactful is /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit, which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.</p><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit-m-e-t-e-r-s will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.</p><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit-p-i-x-e-l-s makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.</p><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit-d-e-n-s-i-t-y-i-n-d-e-p-e-n-d-e-n-t-p-i-x-e-l-s is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.</p><p class="paragraph">The second aspect that determines size of <code class="lang-kotlin">MapMarker3D</code> is scale. It can be specified at construction time and can be changed later at any time using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-scale.</p><h1 class="">Modifying at runtime</h1><p class="paragraph">A 3D marker can be moved around a map by updating its coordinates using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-coordinates.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><p class="paragraph">Its orientation is specified by bearing, pitch and roll and can be changed by using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-bearing, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-pitch and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-roll.</p><h1 class="">Flat marker</h1><p class="paragraph">A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it's an image drawn "on the ground". Such 3D marker can be conveniently created using com.here.sdk.mapview.MapMarker3D.MapMarker3D constructor. Of course, once created, it can be rotated to face any direction.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapMarker3D" data-filterable-set=":modules:dokkaHtml/release" data-name="-1108773546%2FConstructors%2F1617540583" id="-1108773546%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-map-marker3-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(at: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model)</div><div class="brief"><p class="paragraph">Creates an instance of a 3D marker.</p></div><div class="symbol monospace">constructor(at: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, unit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit)</div><div class="brief"><p class="paragraph">Creates a flat marker from provided map image.</p></div><div class="symbol monospace">constructor(at: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Creates an instance of a 3D marker with scale factor.</p></div><div class="symbol monospace">constructor(at: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, unit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit)</div><div class="brief"><p class="paragraph">Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="1997741279%2FClasslikes%2F1617540583" id="1997741279%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="bearing" data-filterable-set=":modules:dokkaHtml/release" data-name="-2070516118%2FProperties%2F1617540583" id="-2070516118%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-bearing</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-bearing: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The bearing of the 3D model in degrees, from the true North in clockwise direction. The bearing axis is perpendicular to the ground and passes through the 3D marker's location. The Z-axis of the model is aligned with bearing axis.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="coordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="418326333%2FProperties%2F1617540583" id="418326333%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates</div><div class="brief"><p class="paragraph">The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system. The altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isDepthCheckEnabled" data-filterable-set=":modules:dokkaHtml/release" data-name="629855910%2FProperties%2F1617540583" id="629855910%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-is-depth-check-enabled</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-is-depth-check-enabled: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Determines whether the depth of the 3D marker's vertices is considered during rendering. If set to <code class="lang-kotlin">false</code>, the 3D marker will always appear in front of any other map objects. If set to <code class="lang-kotlin">true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isRenderInternalsEnabled" data-filterable-set=":modules:dokkaHtml/release" data-name="-1208889257%2FProperties%2F1617540583" id="-1208889257%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-is-render-internals-enabled</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-is-render-internals-enabled: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is <code class="lang-kotlin">false</code>. Can be used with translucent 3D marker.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="metadata" data-filterable-set=":modules:dokkaHtml/release" data-name="340802611%2FProperties%2F1617540583" id="340802611%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-metadata</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-metadata: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-metadata?</div><div class="brief"><p class="paragraph">The /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-metadata instance attached to this 3D marker.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="opacity" data-filterable-set=":modules:dokkaHtml/release" data-name="1653219501%2FProperties%2F1617540583" id="1653219501%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-opacity</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-opacity: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The opacity factor adjusting the opacity of a 3D marker. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="pitch" data-filterable-set=":modules:dokkaHtml/release" data-name="-328411688%2FProperties%2F1617540583" id="-328411688%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-pitch</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-pitch: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="roll" data-filterable-set=":modules:dokkaHtml/release" data-name="152589605%2FProperties%2F1617540583" id="152589605%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-roll</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-roll: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The roll angle of the 3D model in degrees. The roll axis is parallel to the ground, passes through the 3D marker's location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="scale" data-filterable-set=":modules:dokkaHtml/release" data-name="358453006%2FProperties%2F1617540583" id="358453006%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-scale</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">Scale factor applied to the 3D model before rendering.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="visibilityRanges" data-filterable-set=":modules:dokkaHtml/release" data-name="1089044474%2FProperties%2F1617540583" id="1089044474%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-visibility-ranges</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-visibility-ranges: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-range&gt;</div><div class="brief"><p class="paragraph">The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.</p></div></div></div>
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

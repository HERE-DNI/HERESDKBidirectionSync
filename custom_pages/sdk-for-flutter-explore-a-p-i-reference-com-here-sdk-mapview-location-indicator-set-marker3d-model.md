---
title: "set Marker3d Model"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- set-marker3d-model.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/LocationIndicator/setMarker3dModel/#com.here.sdk.mapview.MapMarker3DModel#kotlin.Double#com.here.sdk.mapview.LocationIndicator.MarkerType#com.here.sdk.mapview.RenderSize.Unit/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator/setMarker3dModel</div>
<div class="cover">
<h1 class="cover">set<wbr/>Marker3d<wbr/>Model</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model(model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type, renderSizeUnit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit)</div><p class="paragraph">Sets the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model created from <code class="lang-kotlin">obj</code> files are supported. Models created from Mesh will be ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>model</u></div></div><div><div class="title"><p class="paragraph">The /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model object to be displayed for the specified type. Only models     created from <code class="lang-kotlin">obj</code> files are supported. Those created from mesh will be ignored.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>scale</u></div></div><div><div class="title"><p class="paragraph">A scale factor applied to the marker model.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>type</u></div></div><div><div class="title"><p class="paragraph">The type of location marker for which the marker 3d model should be replaced.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>render<wbr/>Size<wbr/>Unit</u></div></div><div><div class="title"><p class="paragraph">The /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit specifying how the vertex coordinates of the     3D model are being interpreted. It specifies whether the 3D model is placed in world or     screen coordinate space.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">[com.here.sdk.mapview.RenderSize.Unit.METERS] will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube
will have a size of 10 by 10 by 10 meters in world space.

[com.here.sdk.mapview.RenderSize.Unit.PIXELS] makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. A simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.

[com.here.sdk.mapview.RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS] is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div></div><hr/><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model(model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type)</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.27.0. Please use the overloaded method with [com.here.sdk.mapview.RenderSize.Unit] instead.</p></div><p class="paragraph">Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from *.obj files are supported. Models created from Mesh will be ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>model</u></div></div><div><div class="title"><p class="paragraph">The MapMarker3DModel object to be displayed for the specified type. Only models     created from obj files are supported. Those created from mesh will be ignored.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>scale</u></div></div><div><div class="title"><p class="paragraph">The scaling which will be applied to the marker model. As the size of the     location marker should be aligned on devices with different resolutions the     scale factor is applied relative to the ppi value and thus differs from the     scale which is passed to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d objects.     Meter is used for the unit of the map marker 3d model coordinate system.     For historical reason, the scale factor is internally devided by 6.     To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>type</u></div></div><div><div class="title"><p class="paragraph">The type of location marker for which the marker 3d model should be replaced.</p></div></div></div></div></div></div></div>
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

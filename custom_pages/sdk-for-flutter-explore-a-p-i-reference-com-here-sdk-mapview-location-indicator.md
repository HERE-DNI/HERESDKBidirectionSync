---
title: "Location Indicator"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/LocationIndicator///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/LocationIndicator</div>
<div class="cover">
<h1 class="cover">Location<wbr/>Indicator</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Graphical object to represent the location of the user on the map.</p><p class="paragraph">It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-location-indicator-style</p><p class="paragraph">The location is made available to an instance of this class by calling /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-update-location or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-update-location.</p><p class="paragraph">Use /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-enable to add this object to the map and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-disable to remove it.</p><p class="paragraph">Take care that the location indicator is not accidentally added to the map view multiple times for example when the android activity is recreated after an orientation change.</p><p class="paragraph">Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="LocationIndicator" data-filterable-set=":modules:dokkaHtml/release" data-name="1171485068%2FConstructors%2F1617540583" id="1171485068%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-location-indicator</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates an instance of LocationIndicator.</p></div><div class="symbol monospace">constructor(mapView: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base)</div><div class="brief"><p class="paragraph">Creates an instance of LocationIndicator and adds it to provided /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="462929292%2FClasslikes%2F1617540583" id="462929292%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="IndicatorStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="1003080456%2FClasslikes%2F1617540583" id="1003080456%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style&gt; </div><div class="brief"><p class="paragraph">The predefined styles for the location indicator which are pedestrian and navigation mode.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="MarkerType" data-filterable-set=":modules:dokkaHtml/release" data-name="2134659606%2FClasslikes%2F1617540583" id="2134659606%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type&gt; </div><div class="brief"><p class="paragraph">Enum to identify different types of markers of the location indicator.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="isAccuracyVisualized" data-filterable-set=":modules:dokkaHtml/release" data-name="-1178882014%2FProperties%2F1617540583" id="-1178882014%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-is-accuracy-visualized</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-is-accuracy-visualized: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isActive" data-filterable-set=":modules:dokkaHtml/release" data-name="-1084603547%2FProperties%2F1617540583" id="-1084603547%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-is-active</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-is-active: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">A Boolean value that determines whether the active on inactive version of location indicator is shown.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="locationIndicatorStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="1676927006%2FProperties%2F1617540583" id="1676927006%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-location-indicator-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-location-indicator-style: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style</div><div class="brief"><p class="paragraph">The visual style of location indicator. By default, it is set to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style-n-a-v-i-g-a-t-i-o-n.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="materialReflectivity" data-filterable-set=":modules:dokkaHtml/release" data-name="-1651430902%2FProperties%2F1617540583" id="-1651430902%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-material-reflectivity</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-material-reflectivity: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-material-reflectivity?</div><div class="brief"><p class="paragraph">The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While <code class="lang-kotlin">materialReflectivity</code> is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to <code class="lang-kotlin">null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="opacity" data-filterable-set=":modules:dokkaHtml/release" data-name="-1289156454%2FProperties%2F1617540583" id="-1289156454%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-opacity</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-opacity: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color. Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="disable" data-filterable-set=":modules:dokkaHtml/release" data-name="2063786077%2FFunctions%2F1617540583" id="2063786077%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-disable</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-disable()</div><div class="brief"><p class="paragraph">This function removes /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator from map view. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator was not added to any map view yet, this function does nothing.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="enable" data-filterable-set=":modules:dokkaHtml/release" data-name="-884957582%2FFunctions%2F1617540583" id="-884957582%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-enable</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-enable(mapView: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base)</div><div class="brief"><p class="paragraph">Enables /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator for provided /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator is already enabled (added to map view) for passed map view, this function does nothing. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator is added to different /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base, this function removes first /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator from previous map view before adding to new one.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getHaloColor" data-filterable-set=":modules:dokkaHtml/release" data-name="-1147246538%2FFunctions%2F1617540583" id="-1147246538%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-get-halo-color</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-get-halo-color(style: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color</div><div class="brief"><p class="paragraph">Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle. The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setHaloColor" data-filterable-set=":modules:dokkaHtml/release" data-name="-651078348%2FFunctions%2F1617540583" id="-651078348%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-halo-color</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-halo-color(style: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-indicator-style, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color)</div><div class="brief"><p class="paragraph">Sets the color of the accuracy indicator halo for a given style.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setMarker3dModel" data-filterable-set=":modules:dokkaHtml/release" data-name="1160386236%2FFunctions%2F1617540583" id="1160386236%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model(model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type)</div><div class="brief"><p class="paragraph">Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from *.obj files are supported. Models created from Mesh will be ignored.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model(model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model, scale: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-marker-type, renderSizeUnit: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-render-size-unit)</div><div class="brief"><p class="paragraph">Sets the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model created from <code class="lang-kotlin">obj</code> files are supported. Models created from Mesh will be ignored.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="updateLocation" data-filterable-set=":modules:dokkaHtml/release" data-name="-973659045%2FFunctions%2F1617540583" id="-973659045%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-update-location</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-update-location(location: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location)</div><div class="brief"><p class="paragraph">Updates the indicator to a new location. If accuracy visualized is set to <code class="lang-kotlin">true</code> the field /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location-horizontal-accuracy-in-meters determines the size of the accuracy indicator halo.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-location-indicator-update-location(location: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-location, cameraUpdate: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update)</div><div class="brief"><p class="paragraph">Updates the indicator to a new location and applies a camera update at the same time.</p></div></div></div>
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

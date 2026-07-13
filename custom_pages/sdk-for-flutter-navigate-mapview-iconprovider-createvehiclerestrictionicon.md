---
title: "createVehicleRestrictionIcon method - IconProvider class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictionicon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createVehicleRestrictionIcon.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/IconProvider-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">createVehicleRestrictionIcon</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">createVehicleRestrictionIcon</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-pickingResult" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-pickvehiclerestrictionsresult-class">PickVehicleRestrictionsResult</a></span> <span class="parameter-name">pickingResult</span>, </span>
2.  <span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span>
3.  <span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-assetType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a></span> <span class="parameter-name">assetType</span>, </span>
4.  <span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-sizeConstraintsInPixels" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span> <span class="parameter-name">sizeConstraintsInPixels</span>, </span>
5.  <span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.

`pickingResult` The result of picking vehicle restrictions.

`mapScheme` The map scheme for which the vehicle restriction icon should be created.

`assetType` The asset type for which the vehicle restriction icon should be created.

`sizeConstraintsInPixels` The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon's aspect ratio.

`callback` The callback which is used to return the created image along with a description of the icon based on the type of road and/or place it is used, or an error code.

</div>

## Implementation

``` dart
void createVehicleRestrictionIcon(
    PickVehicleRestrictionsResult pickingResult,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    Size2D sizeConstraintsInPixels,
    IconProviderCallback callback) {
  _createVehicleRestrictionIconWithPickResult(
      pickingResult, mapScheme, assetType, sizeConstraintsInPixels, callback);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

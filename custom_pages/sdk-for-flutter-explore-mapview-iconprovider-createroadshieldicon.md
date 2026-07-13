---
title: "createRoadShieldIcon method - IconProvider class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-iconprovider-createroadshieldicon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createRoadShieldIcon.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/IconProvider-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">createRoadShieldIcon</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">createRoadShieldIcon</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-properties" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-roadshieldiconproperties-class">RoadShieldIconProperties</a></span> <span class="parameter-name">properties</span>, </span>
2.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span>
3.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-assetType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-iconproviderassettype">IconProviderAssetType</a></span> <span class="parameter-name">assetType</span>, </span>
4.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-widthConstraintInPixels" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">widthConstraintInPixels</span>, </span>
5.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-heightConstraintInPixels" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">heightConstraintInPixels</span>, </span>
6.  <span id="sdk-for-flutter-explore-createRoadShieldIcon-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-iconprovidercallback">IconProviderCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Creates an image displaying a road shield according to the given parameters.

`properties` The properties which determine the kind of road shield to be created.

`mapScheme` The map scheme for which the road shield should be created.

`assetType` The asset type for which the road shield should be created.

`widthConstraintInPixels` The maximum width of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the width will be calculated based on the heightConstraintInPixels to preserve the aspect ratio.

`heightConstraintInPixels` The maximum height of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the original image-asset's height will be used.

`callback` The callback which is used to return the created image along with a description of the icon based on the type of road and/or place it is used, or an error code.

Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
void createRoadShieldIcon(
    RoadShieldIconProperties properties,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    int widthConstraintInPixels,
    int heightConstraintInPixels,
    IconProviderCallback callback) {
  _createRoadShieldIcon(properties,
    mapScheme,
    assetType,
    widthConstraintInPixels,
    heightConstraintInPixels,
    callback);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

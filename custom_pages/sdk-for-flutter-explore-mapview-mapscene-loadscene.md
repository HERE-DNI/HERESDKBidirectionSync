---
title: "loadScene method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-loadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadScene.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadScene</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">loadScene</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-loadScene-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a></span> <span class="parameter-name">options</span>, </span>
2.  <span id="sdk-for-flutter-explore-loadScene-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously loads a map scene using MapSceneLoadOptions.

This is an unified API that supports loading from either a map scheme or configuration file, with optional feature and watermark configuration. It's more efficient to load the scene with this function by specifying the list of enabled features and disabled features, compared to loading the scene first and enabling or disabling map features in the scene loading callback function.

Configuration defaults are used for features that are not part of the enabled features or disabled features parameters. When a feature is in both the enabled and disabled lists, the feature is considered as requested to be enabled. If the same feature is present multiple times in the enabled list with different modes, then the feature is considered as requested to be enabled, but with an unspecified mode (any of the many specified in the enabled list).

Any previous map scene config will be replaced. The callback is called on the main thread.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `options` Scene configuration options created using MapSceneLoadOptionsBuilder.

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void loadScene(MapSceneLoadOptions options, MapSceneLoadSceneCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

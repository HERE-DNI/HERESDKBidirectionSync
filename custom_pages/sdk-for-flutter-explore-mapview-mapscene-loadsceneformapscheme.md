---
title: "loadSceneForMapScheme method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadSceneForMapScheme</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">loadSceneForMapScheme</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-loadSceneForMapScheme-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span>
2.  <span id="sdk-for-flutter-explore-loadSceneForMapScheme-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously loads a map scene described by a specified map scheme.

Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.

Map features enabled or disabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and <a href="sdk-for-flutter-explore-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a> will be reset to defaults for the new scene configuration.

The callback is called on the main thread.

- `mapScheme` Map scheme.

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void loadSceneForMapScheme(MapScheme mapScheme, MapSceneLoadSceneCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


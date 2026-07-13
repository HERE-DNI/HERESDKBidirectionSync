---
title: "loadSceneFromConfigurationFile method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscene-loadscenefromconfigurationfile"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadSceneFromConfigurationFile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">loadSceneFromConfigurationFile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-loadSceneFromConfigurationFile-param-configurationFile" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configurationFile</span>, </span>
2.  <span id="sdk-for-flutter-navigate-loadSceneFromConfigurationFile-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously loads a map scene described by a specified file in one of the supported formats.

Any previous map scene config will be replaced.

When loading the same file again, consider to call

    reloadScene()

instead.
</p>

Map features enabled or disabled using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and <a href="sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a> will be reset to defaults for the new scene configuration.

The callback is called on the main thread.

- `configurationFile` Map scheme configuration file. It must contain the whole scene configuration. In case it contains references to other files, they have to be reachable under the paths specified in the main configuration file.

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void loadSceneFromConfigurationFile(String configurationFile, MapSceneLoadSceneCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "MapUpdaterConstructionCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">MapUpdaterConstructionCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">MapUpdaterConstructionCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-mapUpdater" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a></span> <span class="parameter-name">mapUpdater</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync">MapUpdater.fromSdkEngineAsync</a> has been completed.

Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.

- `mapUpdater` Represents a constructed `MapUpdater` object.

</div>

## Implementation

``` dart
typedef MapUpdaterConstructionCallback = void Function(MapUpdater mapUpdater);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


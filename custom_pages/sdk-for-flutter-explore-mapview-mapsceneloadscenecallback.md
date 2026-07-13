---
title: "MapSceneLoadSceneCallback typedef - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapsceneloadscenecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLoadSceneCallback.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">MapSceneLoadSceneCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">MapSceneLoadSceneCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-loadSceneError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maperror">MapError</a>?</span> <span class="parameter-name">loadSceneError</span></span>)</span></span>

</div>

<div class="section desc markdown">

Called on the main thread after

    loadScene()

method finishes loading the scene.
</p>

- `loadSceneError` The load scene error

</div>

## Implementation

``` dart
typedef MapSceneLoadSceneCallback = void Function(MapError? loadSceneError);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

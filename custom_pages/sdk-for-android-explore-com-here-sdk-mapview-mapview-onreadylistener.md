---
title: "MapView.OnReadyListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapView](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapView.OnReadyListener</span>

</div>

<div class="block">

Listener that gets notified when MapView is fully initialized and ready
to handle all operations, which means that map scene is loaded and
drawing surface is ready to render a map. Whenever there is a need to
call any map view related functions directly after the Activity resumes,
onMapViewReady() should be used for this purpose, as it guarantees that
those operations will work. It is not recommended to call map view
functionality directly from Activity 's onResume() . There are few
typical moments in the lifecycle where it's useful to execute map view
related operations: After map is shown for the very first time - use
MapScene.LoadSceneCallback that is passed to
MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback) . After the
Activity is resumed - use OnReadyListener that is registered from within
MapScene.LoadSceneCallback the first time map scene is loaded. Every
time the Activity is resumed, including after the map scene is first
loaded - this combines previous two cases. Use OnReadyListener that is
registered right after MapView is created, but before map scene is
loaded.

</div>

See Also:  
- [](sdk-for-android-explore-com-here-sdk-mapview-mapview#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener))

      MapView.setOnReadyListener(OnReadyListener)

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onMapViewReady()</code></pre></td>
  <td><div class="block">
  Callback to be called when MapView is fully initialized and ready to
  handle all operations.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onMapViewReady()" class="section detail">

    ### onMapViewReady

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapViewReady</span>()

    </div>

    <div class="block">

    Callback to be called when MapView is fully initialized and ready to
    handle all operations.

    </div>

    </div>

  </div>

</div>


---
title: "MapView.OnReadyListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview">MapView</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapView.OnReadyListener</span>

</div>

<div class="block">

Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map. Whenever there is a need to call any map view related functions directly after the Activity resumes, onMapViewReady() should be used for this purpose, as it guarantees that those operations will work. It is not recommended to call map view functionality directly from Activity 's onResume() . There are few typical moments in the lifecycle where it's useful to execute map view related operations: After map is shown for the very first time - use MapScene.LoadSceneCallback that is passed to MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback) . After the Activity is resumed - use OnReadyListener that is registered from within MapScene.LoadSceneCallback the first time map scene is loaded. Every time the Activity is resumed, including after the map scene is first loaded - this combines previous two cases. Use OnReadyListener that is registered right after MapView is created, but before map scene is loaded.

</div>

See Also:  
- [](sdk-for-android-navigate-com-here-sdk-mapview-mapview#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener))

      MapView.setOnReadyListener(OnReadyListener)

  </a>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onMapViewReady ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback to be called when MapView is fully initialized and ready to handle all operations.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onMapViewReady" class="section detail">

    ### onMapViewReady

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapViewReady</span>()

    </div>

    <div class="block">

    Callback to be called when MapView is fully initialized and ready to handle all operations.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


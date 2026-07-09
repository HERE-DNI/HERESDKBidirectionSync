---
title: "MapScene.LoadSceneCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview">MapScene</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapScene.LoadSceneCallback</span>

</div>

<div class="block">

Called on the main thread after loadScene() method finishes loading the scene.

</div>

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

      onLoadScene ( MapError loadSceneError)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called on the main thread after loadScene() method finishes loading the scene.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onLoadScene-com-here-sdk-mapview-MapError" class="section detail">

    ### onLoadScene

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLoadScene</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-maperror" title="enum class in com.here.sdk.mapview">MapError</a> loadSceneError)</span>

    </div>

    <div class="block">

    Called on the main thread after loadScene() method finishes loading the scene.

    </div>

    Parameters:  
    `loadSceneError` -

    The load scene error

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


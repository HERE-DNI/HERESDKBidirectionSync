---
title: "MapView.TakeScreenshotCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
[MapView](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapView.TakeScreenshotCallback</span>

</div>

<div class="block">

Callback to be called on retrieval of screenshot. In case of any error passed result is null.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

      onScreenshotTaken (android.graphics.Bitmap bitmap)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback to be called when screenshot is ready.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-onScreenshotTaken-android-graphics-Bitmap" class="section detail">

    ### onScreenshotTaken

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onScreenshotTaken</span><wbr></wbr><span class="parameters">(@Nullable android.graphics.Bitmap bitmap)</span>

    </div>

    <div class="block">

    Callback to be called when screenshot is ready.

    </div>

    Parameters:  
    `bitmap` - The bitmap containing the screenshot.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


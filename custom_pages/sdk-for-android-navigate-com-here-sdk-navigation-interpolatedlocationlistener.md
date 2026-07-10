---
title: "InterpolatedLocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">InterpolatedLocationListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive interpolated locations. The interpolated locations are only provided between VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase) and VisualNavigator.stopRendering() calls and the application is not running in the background.

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

      onInterpolatedLocationUpdated ( Location location)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new interpolated location is calculated, usually several times per second.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onInterpolatedLocationUpdated-com-here-sdk-core-Location" class="section detail">

    ### onInterpolatedLocationUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onInterpolatedLocationUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span>

    </div>

    <div class="block">

    Called whenever a new interpolated location is calculated, usually several times per second. The interpolated locations are only provided between VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase) and VisualNavigator.stopRendering() calls and the application is not running in the background.

    </div>

    Parameters:  
    `location` -

    The interpolated location.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


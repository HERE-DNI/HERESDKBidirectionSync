---
title: "SpatialAudioCuePanning.SpatialAzimuthCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning-spatialazimuthcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">SpatialAudioCuePanning.SpatialAzimuthCallback</span>

</div>

<div class="block">

Called once startAngularPanning() starts.

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

      onSpatialAzimuthStarted ( SpatialTrajectoryData spatialTrajectoryData)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called once startAngularPanning() starts.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSpatialAzimuthStarted-com-here-sdk-navigation-SpatialTrajectoryData" class="section detail">

    ### onSpatialAzimuthStarted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSpatialAzimuthStarted</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialtrajectorydata" title="class in com.here.sdk.navigation">SpatialTrajectoryData</a> spatialTrajectoryData)</span>

    </div>

    <div class="block">

    Called once startAngularPanning() starts.

    </div>

    Parameters:  
    `spatialTrajectoryData` -

    The angular panning information of the current spatial trajectory.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


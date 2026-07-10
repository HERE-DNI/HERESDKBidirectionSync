---
title: "CameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-areacamerabehavior" title="class in com.here.sdk.navigation">`AreaCameraBehavior`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior" title="class in com.here.sdk.navigation">`AutomotiveCameraBehavior`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-dynamiccamerabehavior" title="class in com.here.sdk.navigation">`DynamicCameraBehavior`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior" title="class in com.here.sdk.navigation">`FixedCameraBehavior`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior" title="class in com.here.sdk.navigation">`SpeedBasedCameraBehavior`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">`TrackingCameraBehavior`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">CameraBehavior</span>

</div>

<div class="block">

Interface used to change implement different camera behaviors.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">`Anchor2D`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getNormalizedPrincipalPoint ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the currently set normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setNormalizedPrincipalPoint ( Anchor2D value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets a normalized principal point to be used during navigation.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getNormalizedPrincipalPoint" class="section detail">

    ### getNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()

    </div>

    <div class="block">

    Gets the currently set normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Returns:  
    The normalized principal point.

    </div>

  - <div id="sdk-for-android-navigate-setNormalizedPrincipalPoint-com-here-sdk-core-Anchor2D" class="section detail">

    ### setNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span>

    </div>

    <div class="block">

    Sets a normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Parameters:  
    `value` -

    The normalized principal point.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


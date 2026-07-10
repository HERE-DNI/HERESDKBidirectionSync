---
title: "TrackingCameraBehavior.ZoomPolicy (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy → com.here.NativeBase com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy → com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.ZoomPolicy</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Defines zoom behavior in different policy settings. Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ZoomPolicy`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      makeFixedZoomPolicy (double zoomLevel)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a zoom policy that always returns a fixed zoom level.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ZoomPolicy`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      makeFunctionalRoadClassZoomPolicy ( TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Instantiates a zoom policy that selects zoom levels based on functional road class.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ZoomPolicy`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      makeSpeedBasedZoomPolicy ( TrackingCameraBehavior.SpeedBasedZoomPolicyOptions options)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Instantiates a zoom policy driven by speed thresholds defined per road classification.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-makeFixedZoomPolicy-double" class="section detail">

    ### makeFixedZoomPolicy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeFixedZoomPolicy</span><wbr></wbr><span class="parameters">(double zoomLevel)</span>

    </div>

    <div class="block">

    Creates a zoom policy that always returns a fixed zoom level.

    </div>

    Parameters:  
    `zoomLevel` -

    The constant zoom level that the policy will return.

    Returns:  
    The ZoomPolicy instance.

    </div>

  - <div id="sdk-for-android-navigate-makeFunctionalRoadClassZoomPolicy-com-here-sdk-navigation-TrackingCameraBehavior-FunctionalRoadClassZoomPolicyOptions" class="section detail">

    ### makeFunctionalRoadClassZoomPolicy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeFunctionalRoadClassZoomPolicy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a> options)</span>

    </div>

    <div class="block">

    Instantiates a zoom policy that selects zoom levels based on functional road class.

    </div>

    Parameters:  
    `options` -

    Configuration mapping road classes to zoom levels, including a default fallback.

    Returns:  
    The ZoomPolicy instance.

    </div>

  - <div id="sdk-for-android-navigate-makeSpeedBasedZoomPolicy-com-here-sdk-navigation-TrackingCameraBehavior-SpeedBasedZoomPolicyOptions" class="section detail">

    ### makeSpeedBasedZoomPolicy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeSpeedBasedZoomPolicy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a> options)</span>

    </div>

    <div class="block">

    Instantiates a zoom policy driven by speed thresholds defined per road classification.

    </div>

    Parameters:  
    `options` -

    Configuration describing the speed thresholds mapping to road classifications.

    Returns:  
    The ZoomPolicy instance.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


---
title: "TrackingCameraBehavior.SpeedBasedZoomPolicyOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions → com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration for computing zoom levels from speed thresholds defined per road classification. For correct default initialization, use TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions() .

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions#delayBetweenThresholdChanges" class="member-name-link"><code>delayBetweenThresholdChanges</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Minimum time interval that must pass before the zoom level is allowed to switch to a new speed threshold.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadclassification" title="enum class in com.here.sdk.navigation">`RoadClassification`</a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.SpeedThreshold`</a>`>>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions#roadClassificationToSpeedThreshold" class="member-name-link"><code>roadClassificationToSpeedThreshold</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines, per road classification, how the zoom level should change in response to different vehicle speeds.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      SpeedBasedZoomPolicyOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-delayBetweenThresholdChanges" class="section detail">

    ### delayBetweenThresholdChanges

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">delayBetweenThresholdChanges</span>

    </div>

    <div class="block">

    Minimum time interval that must pass before the zoom level is allowed to switch to a new speed threshold. If TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions() is not used for TrackingCameraBehavior.SpeedBasedZoomPolicyOptions , it will be null .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-roadClassificationToSpeedThreshold" class="section detail">

    ### roadClassificationToSpeedThreshold

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadclassification" title="enum class in com.here.sdk.navigation">RoadClassification</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a>\>\></span> <span class="element-name">roadClassificationToSpeedThreshold</span>

    </div>

    <div class="block">

    Defines, per road classification, how the zoom level should change in response to different vehicle speeds. If TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions() is not used for TrackingCameraBehavior.SpeedBasedZoomPolicyOptions , it will be an empty map.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### SpeedBasedZoomPolicyOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SpeedBasedZoomPolicyOptions</span>()

    </div>

    <div class="block">

    Creates a new instance. Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


---
title: "SpeedBasedCameraBehavior.ProfileValue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.SpeedBasedCameraBehavior.ProfileValue → com.here.sdk.navigation.SpeedBasedCameraBehavior.ProfileValue

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior" title="class in com.here.sdk.navigation">SpeedBasedCameraBehavior</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">SpeedBasedCameraBehavior.ProfileValue</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A single profile value which indicates the speed range in which it applies to its zoom and tilt configuration.

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

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue#fromMetersPerSecond" class="member-name-link"><code>fromMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Start speed of the range.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue#tiltInDegrees" class="member-name-link"><code>tiltInDegrees</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Tilt configuration.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue#toMetersPerSecond" class="member-name-link"><code>toMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  End speed of the range.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue#zoom" class="member-name-link"><code>zoom</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Zoom configuration.

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

      ProfileValue (double fromMetersPerSecond,
       double toMetersPerSecond, MapMeasure zoom,
       double tiltInDegrees)

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

  - <div id="sdk-for-android-navigate-fromMetersPerSecond" class="section detail">

    ### fromMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">fromMetersPerSecond</span>

    </div>

    <div class="block">

    Start speed of the range.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-toMetersPerSecond" class="section detail">

    ### toMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">toMetersPerSecond</span>

    </div>

    <div class="block">

    End speed of the range.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-zoom" class="section detail">

    ### zoom

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">zoom</span>

    </div>

    <div class="block">

    Zoom configuration. Note: MapMeasure.Kind.SCALE is not supported.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-tiltInDegrees" class="section detail">

    ### tiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">tiltInDegrees</span>

    </div>

    <div class="block">

    Tilt configuration.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-double-com-here-sdk-mapview-MapMeasure-double" class="section detail">

    ### ProfileValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ProfileValue</span><wbr></wbr><span class="parameters">(double fromMetersPerSecond, double toMetersPerSecond, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom, double tiltInDegrees)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `fromMetersPerSecond` -

    Start speed of the range.

    `toMetersPerSecond` -

    End speed of the range.

    `zoom` -

    Zoom configuration. Note: <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind#SCALE">`MapMeasure.Kind.SCALE`</a> is not supported.

    `tiltInDegrees` -

    Tilt configuration.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


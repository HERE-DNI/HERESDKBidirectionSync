---
title: "FixedCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.FixedCameraBehavior → com.here.NativeBase com.here.sdk.navigation.FixedCameraBehavior → com.here.sdk.navigation.FixedCameraBehavior

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">FixedCameraBehavior</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span>

</div>

<div class="block">

Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.

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

      FixedCameraBehavior ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCameraBearingInDegrees ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set fixed bearing.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      getCameraDistanceInMeters ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCameraTiltInDegrees ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set camera tilt with axis parallel to the ground.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">`Anchor2D`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNormalizedPrincipalPoint ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getZoom ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current camera's zoom configuration.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCameraBearingInDegrees ( Double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      setCameraDistanceInMeters (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCameraTiltInDegrees (double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets camera tilt with axis parallel to the ground.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setNormalizedPrincipalPoint ( Anchor2D value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setZoom ( MapMeasure value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current camera's zoom configuration.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### FixedCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">FixedCameraBehavior</span>()

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getCameraDistanceInMeters" class="section detail">

    ### getCameraDistanceInMeters

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraDistanceInMeters</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use [](sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom())

        getZoom()

    </a> instead.
    </p>

    </div>

    </div>

    <div class="block">

    Gets the currently set camera distance to current location. The default value is 150 meters. Camera distance to current location. The default value is 150 meters.

    </div>

    Returns:  
    Camera distance in meters.

    </div>

  - <div id="sdk-for-android-navigate-setCameraDistanceInMeters-double" class="section detail">

    ### setCameraDistanceInMeters

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraDistanceInMeters</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use [](sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom())

        getZoom()

    </a> instead.
    </p>

    </div>

    </div>

    <div class="block">

    Sets the camera distance to current location. The default value is 150 meters. Camera distance to current location. The default value is 150 meters.

    </div>

    Parameters:  
    `value` -

    Camera distance in meters.

    </div>

  - <div id="sdk-for-android-navigate-getZoom" class="section detail">

    ### getZoom

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">getZoom</span>()

    </div>

    <div class="block">

    Gets the current camera's zoom configuration. Camera zoom configuration. The default value is 150 meters. Note: MapMeasure.Kind.SCALE is not supported.

    </div>

    Returns:  
    Zoom configuration. The default value is 150 meters.

    </div>

  - <div id="sdk-for-android-navigate-setZoom-com-here-sdk-mapview-MapMeasure" class="section detail">

    ### setZoom

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoom</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span>

    </div>

    <div class="block">

    Sets the current camera's zoom configuration. Camera zoom configuration. The default value is 150 meters. Note: MapMeasure.Kind.SCALE is not supported.

    </div>

    Parameters:  
    `value` -

    Zoom configuration. The default value is 150 meters.

    </div>

  - <div id="sdk-for-android-navigate-getCameraTiltInDegrees" class="section detail">

    ### getCameraTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraTiltInDegrees</span>()

    </div>

    <div class="block">

    Gets the currently set camera tilt with axis parallel to the ground. The default value is 50 degrees. The default value is 50 degrees.

    </div>

    Returns:  
    Camera tilt with axis parallel to the ground.

    </div>

  - <div id="sdk-for-android-navigate-setCameraTiltInDegrees-double" class="section detail">

    ### setCameraTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraTiltInDegrees</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets camera tilt with axis parallel to the ground. The default value is 50 degrees.

    </div>

    Parameters:  
    `value` -

    Camera tilt with axis parallel to the ground.

    </div>

  - <div id="sdk-for-android-navigate-getCameraBearingInDegrees" class="section detail">

    ### getCameraBearingInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getCameraBearingInDegrees</span>()

    </div>

    <div class="block">

    Gets the currently set fixed bearing. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to null , which means the camera derives the bearing from the Location , so that it points to the direction of travel. If this property is null and the device does not provide bearing, the last known value is used or zero otherwise.

    </div>

    Returns:  
    Camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-setCameraBearingInDegrees-java-lang-Double" class="section detail">

    ### setCameraBearingInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBearingInDegrees</span><wbr></wbr><span class="parameters">(@Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> value)</span>

    </div>

    <div class="block">

    Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to null , which means the camera derives the bearing from the Location , so that it points to the direction of travel. If this property is null and the device does not provide bearing, the last known value is used or zero otherwise.

    </div>

    Parameters:  
    `value` -

    Camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-getNormalizedPrincipalPoint" class="section detail">

    ### getNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()

    </div>

    <div class="block">

    Gets the currently set normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior#getNormalizedPrincipalPoint(">`getNormalizedPrincipalPoint`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

    Returns:  
    The normalized principal point.

    </div>

  - <div id="sdk-for-android-navigate-setNormalizedPrincipalPoint-com-here-sdk-core-Anchor2D" class="section detail">

    ### setNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span>

    </div>

    <div class="block">

    Sets a normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D">`setNormalizedPrincipalPoint`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

    Parameters:  
    `value` -

    The normalized principal point.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


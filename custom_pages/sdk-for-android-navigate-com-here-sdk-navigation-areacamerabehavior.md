---
title: "AreaCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-areacamerabehavior"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.AreaCameraBehavior → com.here.NativeBase com.here.sdk.navigation.AreaCameraBehavior → com.here.sdk.navigation.AreaCameraBehavior

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AreaCameraBehavior</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span>

</div>

<div class="block">

Use this class to show an overview of geo points. By default, the orientation of the camera will be perpendicular to the Earth's surface (ie. looking towards the center of the Earth), while bearing will be towards north. Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

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

      AreaCameraBehavior ()

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

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCameraAnimationDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCameraBearingInDegrees ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current camera bearing.

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

  Gets the current camera tilt.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMaxZoom ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets maximal allowed zoom.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">`Anchor2D`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNormalizedPrincipalPoint ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPrincipalPointAnimationDuration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current principal point animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">`Rectangle2D`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewRectangle ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current view rectangle, if it's set.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisiblePoints ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets configured visible geo points.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isCurrentPositionIncluded ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets whether to include the current position.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCameraAnimationDuration ( Duration value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCameraBearingInDegrees (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets camera bearing.

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

  Sets camera tilt.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCurrentPositionIncluded (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to include the current position.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMaxZoom ( MapMeasure value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets maximal allowed zoom.

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

      setPrincipalPointAnimationDuration ( Duration value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current principal point animation in milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setViewRectangle ( Rectangle2D value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets view rectangle.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisiblePoints ( List < GeoCoordinates > visiblePoints)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the list of geo points to show in the camera view.

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

    ### AreaCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AreaCameraBehavior</span>()

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-setVisiblePoints-java-util-List" class="section detail">

    ### setVisiblePoints

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisiblePoints</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\> visiblePoints)</span>

    </div>

    <div class="block">

    Sets the list of geo points to show in the camera view.

    </div>

    Parameters:  
    `visiblePoints` -

    The list of geo points to visualize. The list can be empty.

    </div>

  - <div id="sdk-for-android-navigate-getVisiblePoints" class="section detail">

    ### getVisiblePoints

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\></span> <span class="element-name">getVisiblePoints</span>()

    </div>

    <div class="block">

    Gets configured visible geo points.

    </div>

    Returns:  
    The list of geo points to show in the camera view. The list can be empty.

    </div>

  - <div id="sdk-for-android-navigate-getViewRectangle" class="section detail">

    ### getViewRectangle

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span class="element-name">getViewRectangle</span>()

    </div>

    <div class="block">

    Gets the current view rectangle, if it's set. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to null . If not set, it uses the viewport bounds of the underlying map view.

    </div>

    Returns:  
    The view rectangle for camera updates.

    </div>

  - <div id="sdk-for-android-navigate-setViewRectangle-com-here-sdk-core-Rectangle2D" class="section detail">

    ### setViewRectangle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewRectangle</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</span>

    </div>

    <div class="block">

    Sets view rectangle. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to null . If not set, it uses the viewport bounds of the underlying map view.

    </div>

    Parameters:  
    `value` -

    The view rectangle for camera updates.

    </div>

  - <div id="sdk-for-android-navigate-getCameraAnimationDuration" class="section detail">

    ### getCameraAnimationDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getCameraAnimationDuration</span>()

    </div>

    <div class="block">

    Gets the current animation duration in milliseconds. If there is an animation, it will last for specified period of time. Defaults to 500 milliseconds, or half a second.

    </div>

    Returns:  
    The duration of camera animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-setCameraAnimationDuration-com-here-time-Duration" class="section detail">

    ### setCameraAnimationDuration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraAnimationDuration</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span>

    </div>

    <div class="block">

    Sets the current animation duration in milliseconds. If there is an animation, it will last for specified period of time. Defaults to 500 milliseconds, or half a second.

    </div>

    Parameters:  
    `value` -

    The duration of camera animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-getPrincipalPointAnimationDuration" class="section detail">

    ### getPrincipalPointAnimationDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getPrincipalPointAnimationDuration</span>()

    </div>

    <div class="block">

    Gets the current principal point animation duration in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

    </div>

    Returns:  
    The duration of principal point animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-setPrincipalPointAnimationDuration-com-here-time-Duration" class="section detail">

    ### setPrincipalPointAnimationDuration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrincipalPointAnimationDuration</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span>

    </div>

    <div class="block">

    Sets the current principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

    </div>

    Parameters:  
    `value` -

    The duration of principal point animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-getMaxZoom" class="section detail">

    ### getMaxZoom

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">getMaxZoom</span>()

    </div>

    <div class="block">

    Gets maximal allowed zoom. Defines maximal zoom level to be applied to enclose geodetic bounding box. Defaults to a MapMeasure with kind MapMeasure.Kind.ZOOM_LEVEL and value 20.0. Note: MapMeasure.Kind.SCALE is not supported.

    </div>

    Returns:  
    Maximal allowed zoom.

    </div>

  - <div id="sdk-for-android-navigate-setMaxZoom-com-here-sdk-mapview-MapMeasure" class="section detail">

    ### setMaxZoom

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaxZoom</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span>

    </div>

    <div class="block">

    Sets maximal allowed zoom. Defines maximal zoom level to be applied to enclose geodetic bounding box. Defaults to a MapMeasure with kind MapMeasure.Kind.ZOOM_LEVEL and value 20.0. Note: MapMeasure.Kind.SCALE is not supported.

    </div>

    Parameters:  
    `value` -

    Maximal allowed zoom.

    </div>

  - <div id="sdk-for-android-navigate-getCameraBearingInDegrees" class="section detail">

    ### getCameraBearingInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraBearingInDegrees</span>()

    </div>

    <div class="block">

    Gets the current camera bearing. The direction in which the camera will point in degrees clockwise, relative to true North. The input should range between \[0, 360\]. Defaults to true North (0 degrees).

    </div>

    Returns:  
    Camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-setCameraBearingInDegrees-double" class="section detail">

    ### setCameraBearingInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBearingInDegrees</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets camera bearing. The direction in which the camera will point in degrees clockwise, relative to true North. The input should range between \[0, 360\]. Defaults to true North (0 degrees).

    </div>

    Parameters:  
    `value` -

    Camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-getCameraTiltInDegrees" class="section detail">

    ### getCameraTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraTiltInDegrees</span>()

    </div>

    <div class="block">

    Gets the current camera tilt. The tilt of the camera relative to the axis perpendicular to the ground. Defaults to 0 degrees, meaning that it will look straight down into the ground.

    </div>

    Returns:  
    Camera tilt in degrees.

    </div>

  - <div id="sdk-for-android-navigate-setCameraTiltInDegrees-double" class="section detail">

    ### setCameraTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraTiltInDegrees</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets camera tilt. The tilt of the camera relative to the axis perpendicular to the ground. Defaults to 0 degrees, meaning that it will look straight down into the ground.

    </div>

    Parameters:  
    `value` -

    Camera tilt in degrees.

    </div>

  - <div id="sdk-for-android-navigate-isCurrentPositionIncluded" class="section detail">

    ### isCurrentPositionIncluded

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCurrentPositionIncluded</span>()

    </div>

    <div class="block">

    Gets whether to include the current position. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to false will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to false or it will try to include the current position. Defaults to false.

    </div>

    Returns:  
    Include current position in camera view.

    </div>

  - <div id="sdk-for-android-navigate-setCurrentPositionIncluded-boolean" class="section detail">

    ### setCurrentPositionIncluded

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrentPositionIncluded</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to include the current position. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to false will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to false or it will try to include the current position. Defaults to false.

    </div>

    Parameters:  
    `value` -

    Include current position in camera view.

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


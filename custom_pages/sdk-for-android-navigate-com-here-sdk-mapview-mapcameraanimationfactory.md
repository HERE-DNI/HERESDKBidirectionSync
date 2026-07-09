---
title: "MapCameraAnimationFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapCameraAnimationFactory → com.here.NativeBase com.here.sdk.mapview.MapCameraAnimationFactory → com.here.sdk.mapview.MapCameraAnimationFactory

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraAnimationFactory</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Factory for creating MapCameraAnimation objects to change map's camera over time.

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

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      createAnimation ( MapCameraKeyframeTrack track)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation for a movement defined by the supplied track .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      createAnimation ( MapCameraUpdate cameraUpdate, Duration duration, Easing easing)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation to gradually update the camera properties within a specified duration from its current values to the ones defined in the cameraUpdate .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      createAnimation ( List < MapCameraKeyframeTrack > tracks)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation for a movement defined by the supplied list of tracks .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      flyTo ( GeoCoordinatesUpdate target,
       double bowFactor, Duration duration)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      flyTo ( GeoCoordinatesUpdate target, GeoOrientationUpdate orientation,
       double bowFactor, Duration duration)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      flyTo ( GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, MapMeasure zoom,
       double bowFactor, Duration duration)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">`MapCameraAnimation`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      flyTo ( GeoCoordinatesUpdate target, MapMeasure zoom,
       double bowFactor, Duration duration)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

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

  - <div id="sdk-for-android-navigate-createAnimation-com-here-sdk-mapview-MapCameraUpdate-com-here-time-Duration-com-here-sdk-animation-Easing" class="section detail">

    ### createAnimation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation to gradually update the camera properties within a specified duration from its current values to the ones defined in the cameraUpdate . MapCameraAnimation instances created from MapCameraUpdateFactory.compositeUpdate(java.util.List\<com.here.sdk.mapview.MapCameraUpdate\>) instances are not supported. An AnimationListener will receive an AnimationState.CANCELLED signal when trying to apply such animations.

    </div>

    Parameters:  
    `cameraUpdate` -

    Update which should be applied to the map camera.

    `duration` -

    Duration of the animation. Negative duration results in no camera change when applied.

    `easing` -

    Easing to apply.

    Returns:  
    MapCameraAnimation instance

    </div>

  - <div id="sdk-for-android-navigate-createAnimation-com-here-sdk-mapview-MapCameraKeyframeTrack" class="section detail">

    ### createAnimation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a> track)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation for a movement defined by the supplied track .

    </div>

    Parameters:  
    `track` -

    The track

    Returns:  
    MapCameraAnimation instance

    </div>

  - <div id="sdk-for-android-navigate-createAnimation-java-util-List" class="section detail">

    ### createAnimation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">createAnimation</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a>\> tracks)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation-instantiationexception" title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation for a movement defined by the supplied list of tracks . Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind. However, the following cases can only be detected at the time when animation is started: Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation. Changing tilt of camera orientation also changes camera look-at distance and camera look-at target. Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0. Changing tilt or bearing of camera look-at orientation also changes camera position. Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.

    </div>

    Parameters:  
    `tracks` -

    The list of tracks

    Returns:  
    MapCameraAnimation instance

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraAnimation.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-flyTo-com-here-sdk-core-GeoCoordinatesUpdate-double-com-here-time-Duration" class="section detail">

    ### flyTo

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target, double bowFactor, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve. The beginning and end of the animation will use the current zoom. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly. The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target. A bow factor of 0 does not change the camera's zoom over time. Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation. The bow factor is clamped to \[-1, +1\]. Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value. Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:  
    MapCameraAnimation instance

    </div>

  - <div id="sdk-for-android-navigate-flyTo-com-here-sdk-core-GeoCoordinatesUpdate-com-here-sdk-core-GeoOrientationUpdate-double-com-here-time-Duration" class="section detail">

    ### flyTo

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation, double bowFactor, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve. The beginning and end of the animation will use the current zoom. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `orientation` -

    The orientation at destination.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly. The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target. A bow factor of 0 does not change the camera's zoom over time. Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation. The bow factor is clamped to \[-1, +1\]. Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value. Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:  
    MapCameraAnimation instance

    </div>

  - <div id="sdk-for-android-navigate-flyTo-com-here-sdk-core-GeoCoordinatesUpdate-com-here-sdk-mapview-MapMeasure-double-com-here-time-Duration" class="section detail">

    ### flyTo

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom, double bowFactor, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve. The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `zoom` -

    The zoom at the end of the animation.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly. The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target. A bow factor of 0 does not affect the camera's zoom over time. Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation. The bow factor is clamped to \[-1, +1\]. Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value. Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:  
    MapCameraAnimation instance

    </div>

  - <div id="sdk-for-android-navigate-flyTo-com-here-sdk-core-GeoCoordinatesUpdate-com-here-sdk-core-GeoOrientationUpdate-com-here-sdk-mapview-MapMeasure-double-com-here-time-Duration" class="section detail">

    ### flyTo

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a></span> <span class="element-name">flyTo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom, double bowFactor, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span>

    </div>

    <div class="block">

    Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve. The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    `orientation` -

    The orientation at destination.

    `zoom` -

    The zoom at the end of the animation.

    `bowFactor` -

    A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly. The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target. A bow factor of 0 does not affect the camera's zoom over time. Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation. The bow factor is clamped to \[-1, +1\]. Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value. Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

    `duration` -

    Duration of the flight. Negative duration results in no camera change when applied.

    Returns:  
    MapCameraAnimation instance

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


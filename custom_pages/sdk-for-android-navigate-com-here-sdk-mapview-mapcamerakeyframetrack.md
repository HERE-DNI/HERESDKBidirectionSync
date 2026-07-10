---
title: "MapCameraKeyframeTrack (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapCameraKeyframeTrack → com.here.NativeBase com.here.sdk.mapview.MapCameraKeyframeTrack → com.here.sdk.mapview.MapCameraKeyframeTrack

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraKeyframeTrack</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode. Can only hold keyframes of a single type.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationerrorcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapCameraKeyframeTrack.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create a MapCameraKeyframeTrack.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapCameraKeyframeTrack.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create MapCameraKeyframeTrack .

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fieldOfView ( List < ScalarKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera field-of-view keyframe track.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-animation-anchor2dkeyframe" title="class in com.here.sdk.animation">`Anchor2DKeyframe`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAnchor2DKeyframes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">`GeoCoordinatesKeyframe`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeoCoordinatesKeyframes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-animation-geoorientationkeyframe" title="class in com.here.sdk.animation">`GeoOrientationKeyframe`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeoOrientationKeyframes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">`KeyframeInterpolationMode`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInterpolationMode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the interpolation mode for the between key frames in the track.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe" title="class in com.here.sdk.animation">`Point2DKeyframe`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPoint2DKeyframes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">`ScalarKeyframe`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getScalarKeyframes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      lookAtDistance ( MapMeasure.Kind distanceKind, List < ScalarKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera look-at distance keyframe track.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

      lookAtDistance ( List < ScalarKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.27.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      lookAtOrientation ( List < GeoOrientationKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera look-at orientation keyframe track.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      lookAtTarget ( List < GeoCoordinatesKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera look-at target keyframe track.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      normalizedPrincipalPoint ( List < Anchor2DKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera principal point keyframe track.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      principalPoint ( List < Point2DKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map camera principal point keyframe track.

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

  - <div id="sdk-for-android-navigate-getScalarKeyframes" class="section detail">

    ### getScalarKeyframes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>\></span> <span class="element-name">getScalarKeyframes</span>()

    </div>

    Returns:  
    a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.

    </div>

  - <div id="sdk-for-android-navigate-getPoint2DKeyframes" class="section detail">

    ### getPoint2DKeyframes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>\></span> <span class="element-name">getPoint2DKeyframes</span>()

    </div>

    Returns:  
    a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.

    </div>

  - <div id="sdk-for-android-navigate-getAnchor2DKeyframes" class="section detail">

    ### getAnchor2DKeyframes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>\></span> <span class="element-name">getAnchor2DKeyframes</span>()

    </div>

    Returns:  
    a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.

    </div>

  - <div id="sdk-for-android-navigate-getGeoCoordinatesKeyframes" class="section detail">

    ### getGeoCoordinatesKeyframes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>\></span> <span class="element-name">getGeoCoordinatesKeyframes</span>()

    </div>

    Returns:  
    a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.

    </div>

  - <div id="sdk-for-android-navigate-getGeoOrientationKeyframes" class="section detail">

    ### getGeoOrientationKeyframes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>\></span> <span class="element-name">getGeoOrientationKeyframes</span>()

    </div>

    Returns:  
    a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.

    </div>

  - <div id="sdk-for-android-navigate-lookAtDistance-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### lookAtDistance

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtDistance</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Use <scalarkeyframe>, Easing, KeyframeInterpolationMode) instead.</scalarkeyframe>

    </div>

    </div>

    <div class="block">

    Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the distance from the map camera to its target.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-lookAtDistance-com-here-sdk-mapview-MapMeasure-Kind-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### lookAtDistance

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtDistance</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> distanceKind, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at. The measure kind of that distance can be specified. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.

    </div>

    Parameters:  
    `distanceKind` -

    The kind of measure of distance between camera and target point.

    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the distance from the map camera to its target.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-lookAtTarget-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### lookAtTarget

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtTarget</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-geocoordinateskeyframe" title="class in com.here.sdk.animation">GeoCoordinatesKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera look-at target keyframe track. It enables animations over the geographical coordinates of the target point that the map camera is looking at. Altitude components of coordinates are ignored.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the map camera target coordinates.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-lookAtOrientation-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### lookAtOrientation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">lookAtOrientation</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-geoorientationkeyframe" title="class in com.here.sdk.animation">GeoOrientationKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera look-at orientation keyframe track. It enables animations over the orientation of the map camera target (bearing and tilt).

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the map camera target orientation.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-principalPoint-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### principalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">principalPoint</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe" title="class in com.here.sdk.animation">Point2DKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera principal point keyframe track. It enables animations on the pixel point where the map camera's target is placed in view coordinates. (0,0) is top left of the viewport, (viewport width, viewport height) is bottom right.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the principal point.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-normalizedPrincipalPoint-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### normalizedPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">normalizedPrincipalPoint</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-anchor2dkeyframe" title="class in com.here.sdk.animation">Anchor2DKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera principal point keyframe track. It enables animations on the point where the map camera's target is placed in normalized view coordinates. (0,0) is top left of the viewport, (1, 1) is bottom right.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the principal point.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-fieldOfView-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode" class="section detail">

    ### fieldOfView

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></span> <span class="element-name">fieldOfView</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-animation-scalarkeyframe" title="class in com.here.sdk.animation">ScalarKeyframe</a>\> keyframes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation">Easing</a> easing, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a> interpolationMode)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></span>

    </div>

    <div class="block">

    Creates a map camera field-of-view keyframe track. It enables animations over the angle of the field of view captured by the map camera in degrees. Values will be clamped to a range from 1 to 150.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    A keyframe track over the map camera field-of-view.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception" title="class in com.here.sdk.mapview">`MapCameraKeyframeTrack.InstantiationException`</a> -

    Indicates an instantiation issue.

    </div>

  - <div id="sdk-for-android-navigate-getInterpolationMode" class="section detail">

    ### getInterpolationMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-animation-keyframeinterpolationmode" title="enum class in com.here.sdk.animation">KeyframeInterpolationMode</a></span> <span class="element-name">getInterpolationMode</span>()

    </div>

    <div class="block">

    Gets the interpolation mode for the between key frames in the track.

    </div>

    Returns:  
    Interpolation mode affects the shape of the spline going through all keyframes.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


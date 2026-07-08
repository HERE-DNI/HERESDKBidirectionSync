---
title: "MapItemKeyFrameTrack (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.animation](sdk-for-android-explore-com-here-sdk-animation-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase
com.here.sdk.animation.MapItemKeyFrameTrack → com.here.NativeBase
com.here.sdk.animation.MapItemKeyFrameTrack →
com.here.sdk.animation.MapItemKeyFrameTrack

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapItemKeyFrameTrack</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Stores keyframes for interpolation of a map item property using a
specific easing function and interpolation mode. The keyframe track
object is used to create animations, see MapMarkerAnimation and
MapPolylineAnimation .

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

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

  <a
  href="sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.animation"><code>MapItemKeyFrameTrack.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create a MapItemKeyFrameTrack .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.animation"><code>MapItemKeyFrameTrack.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create
  MapItemKeyFrameTrack .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  `static `[`MapItemKeyFrameTrack`](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack "class in com.here.sdk.animation")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      moveTo ( List < GeoCoordinatesKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a map item position keyframe track.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`MapItemKeyFrameTrack`](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack "class in com.here.sdk.animation")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      polylineProgress ( List < ScalarKeyframe > keyframes, Easing easing, KeyframeInterpolationMode interpolationMode)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a keyframe track used to animate the progress of a polyline.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-moveTo-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode"
    class="section detail">

    ### moveTo

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapItemKeyFrameTrack](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack "class in com.here.sdk.animation")</span> <span class="element-name">moveTo</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinatesKeyframe](sdk-for-android-explore-com-here-sdk-animation-geocoordinateskeyframe "class in com.here.sdk.animation")\> keyframes,
    @NonNull
    [Easing](sdk-for-android-explore-com-here-sdk-animation-easing "class in com.here.sdk.animation") easing,
    @NonNull
    [KeyframeInterpolationMode](sdk-for-android-explore-com-here-sdk-animation-keyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode)</span>
    throws
    <span class="exceptions">[MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")</span>

    </div>

    <div class="block">

    Creates a map item position keyframe track. It enables animations
    over the geographical coordinates where the map item is positioned.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the map item position changes
    over time.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    MapItemKeyFrameTrack instance.

    Throws:  
    [`MapItemKeyFrameTrack.InstantiationException`](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")

    If the supplied keyframe list is empty or first keyframe duration is
    not 0.

    </div>

  - <div id="sdk-for-android-explore-polylineProgress-java-util-List-com-here-sdk-animation-Easing-com-here-sdk-animation-KeyframeInterpolationMode"
    class="section detail">

    ### polylineProgress

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapItemKeyFrameTrack](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack "class in com.here.sdk.animation")</span> <span class="element-name">polylineProgress</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ScalarKeyframe](sdk-for-android-explore-com-here-sdk-animation-scalarkeyframe "class in com.here.sdk.animation")\> keyframes,
    @NonNull
    [Easing](sdk-for-android-explore-com-here-sdk-animation-easing "class in com.here.sdk.animation") easing,
    @NonNull
    [KeyframeInterpolationMode](sdk-for-android-explore-com-here-sdk-animation-keyframeinterpolationmode "enum class in com.here.sdk.animation") interpolationMode)</span>
    throws
    <span class="exceptions">[MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")</span>

    </div>

    <div class="block">

    Creates a keyframe track used to animate the progress of a polyline.
    Each scalar keyframe specifies the progress property (as passed to
    MapPolyline.setProgress(double) ) at key points of the animation.

    </div>

    Parameters:  
    `keyframes` -

    The list of keyframes that specify how the polyline progress changes
    over time.

    `easing` -

    The easing to apply during keyframe interpolation.

    `interpolationMode` -

    The type of interpolation done between keyframe values.

    Returns:  
    MapItemKeyFrameTrack instance.

    Throws:  
    [`MapItemKeyFrameTrack.InstantiationException`](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")

    If the supplied keyframe list is empty or first keyframe duration is
    not 0.

    </div>

  </div>


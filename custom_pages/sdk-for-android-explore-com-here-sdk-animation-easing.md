---
title: "Easing (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-animation-easing"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.animation](sdk-for-android-explore-com-here-sdk-animation-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.animation.Easing →
com.here.NativeBase com.here.sdk.animation.Easing →
com.here.sdk.animation.Easing

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Easing</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Animation easing representing an easing function to be used during
animations.

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
  href="sdk-for-android-explore-com-here-sdk-animation-easing-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.animation"><code>Easing.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create an Easing .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-animation-easing-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.animation"><code>Easing.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create an Easing .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      Easing ( EasingFunction easingFunction)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of Easing using a predefined easing function.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Easing ( List < Point2D > points)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an instance of customized Easing using a specified number of
  points describing an easing function.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-animation-EasingFunction"
    class="section detail">

    ### Easing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Easing</span><span class="parameters">(@NonNull
    [EasingFunction](sdk-for-android-explore-com-here-sdk-animation-easingfunction "enum class in com.here.sdk.animation") easingFunction)</span>

    </div>

    <div class="block">

    Creates an instance of Easing using a predefined easing function.

    </div>

    Parameters:  
    `easingFunction` -

    Easing function.

    </div>

  - <div id="sdk-for-android-explore-init-java-util-List"
    class="section detail">

    ### Easing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Easing</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")\> points)</span>
    throws
    <span class="exceptions">[Easing.InstantiationException](sdk-for-android-explore-com-here-sdk-animation-easing-instantiationexception "class in com.here.sdk.animation")</span>

    </div>

    <div class="block">

    Creates an instance of customized Easing using a specified number of
    points describing an easing function.

    </div>

    Parameters:  
    `points` -

    List of sampled data points that define an easing function. X
    describes normalized time values in the range \[0, 1\]. Y describes
    normalized animated value changes. Values can fall outside of the
    range \[0, 1\]. During an animation run animated target value is
    multiplied with Y value. In case resulting animated target value
    falls outside of its own supported range it will be clamped to its
    range (e.g. when negative values used for color animation). X values
    must increase monotonically. There must be at least 2 data points
    specified. The first point's X value must be 0, the last point's X
    value must be 1. During an animation run for any given time value X'
    from the animation engine that satisfies the relation X(i) \< X' \<
    X(i+1) for the given X data points the corresponding Y' value will
    be calculated by linearly interpolating between Y(i) and Y(i+1) data
    points. The higher the sampling rate of the easing curve used for
    the data points the more precise the results. In order to achieve
    the same animation precision for animations with different durations
    (shorter vs longer) it is recommended to use a higher sampling rate
    for longer animation duration.

    Throws:  
    [`Easing.InstantiationException`](sdk-for-android-explore-com-here-sdk-animation-easing-instantiationexception "class in com.here.sdk.animation")

    Instantiation error in case of invalid input parameters.

    </div>

  </div>


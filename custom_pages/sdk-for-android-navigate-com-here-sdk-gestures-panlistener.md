---
title: "PanListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-gestures-panlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-gestures-package-summary">com.here.sdk.gestures</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">PanListener</span>

</div>

<div class="block">

Interface for handling pan gestures. Pan gesture occurs when a finger is moving on the screen.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onPan ( GestureState state, Point2D origin, Point2D translation,
       double velocity)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when the pan gesture occurs.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onPan-com-here-sdk-gestures-GestureState-com-here-sdk-core-Point2D-com-here-sdk-core-Point2D-double" class="section detail">

    ### onPan

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPan</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> translation, double velocity)</span>

    </div>

    <div class="block">

    Called when the pan gesture occurs.

    </div>

    Parameters:  
    `state` -

    Determines in which state the gesture is.

    `origin` -

    Position of the touch point relative to the MapView in pixels.

    `translation` -

    Translation offset since the last position in pixels.

    `velocity` -

    Velocity of panning in pixels per millisecond.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


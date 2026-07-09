---
title: "PinchRotateListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-gestures-pinchrotatelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-gestures-package-summary">com.here.sdk.gestures</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">PinchRotateListener</span>

</div>

<div class="block">

Interface for handling pinch rotate gestures. Pinch rotate gesture occurs when two fingers are on the screen and at least one of them moves.

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

      onPinchRotate ( GestureState state, Point2D pinchOrigin, Point2D rotationOrigin,
       double twoFingerDistance, Angle rotation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when the pinch rotate gesture occurs.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onPinchRotate-com-here-sdk-gestures-GestureState-com-here-sdk-core-Point2D-com-here-sdk-core-Point2D-double-com-here-sdk-core-Angle" class="section detail">

    ### onPinchRotate

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPinchRotate</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-gestures-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> pinchOrigin, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> rotationOrigin, double twoFingerDistance, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a> rotation)</span>

    </div>

    <div class="block">

    Called when the pinch rotate gesture occurs.

    </div>

    Parameters:  
    `state` -

    Determines in which state the gesture is.

    `pinchOrigin` -

    Position where the pinch happened relative to the MapView in pixels.

    `rotationOrigin` -

    Position where the rotation happened relative to the MapView in pixels.

    `twoFingerDistance` -

    Distance between the two fingers in pixels.

    `rotation` -

    Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed since the previous gesture update. Clockwise finger rotation gives positive deltas, counter clockwise finger rotation gives negative deltas.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


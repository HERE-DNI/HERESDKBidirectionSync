---
title: "PinchRotateListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-pinchrotatelistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">PinchRotateListener</span>

</div>

<div class="block">

Interface for handling pinch rotate gestures. Pinch rotate gesture
occurs when two fingers are on the screen and at least one of them
moves.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onPinchRotate(GestureState state,
   Point2D pinchOrigin,
   Point2D rotationOrigin,
   double twoFingerDistance,
   Angle rotation)</code></pre></td>
  <td><div class="block">
  Called when the pinch rotate gesture occurs.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onPinchRotate(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double,com.here.sdk.core.Angle)"
    class="section detail">

    ### onPinchRotate

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPinchRotate</span><span class="parameters">(@NonNull
    [GestureState](sdk-for-android-explore-com-here-sdk-gestures-gesturestate "enum class in com.here.sdk.gestures") state,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") pinchOrigin,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") rotationOrigin,
    double twoFingerDistance, @NonNull
    [Angle](sdk-for-android-explore-com-here-sdk-core-angle "class in com.here.sdk.core") rotation)</span>

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

    Position where the rotation happened relative to the MapView in
    pixels.

    `twoFingerDistance` -

    Distance between the two fingers in pixels.

    `rotation` -

    Fingers rotation angle delta. Indicates how much the fingers
    rotation angle has changed since the previous gesture update.
    Clockwise finger rotation gives positive deltas, counter clockwise
    finger rotation gives negative deltas.

    </div>

  </div>

</div>


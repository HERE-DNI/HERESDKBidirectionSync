---
title: "PanListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-panlistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">PanListener</span>

</div>

<div class="block">

Interface for handling pan gestures. Pan gesture occurs when a finger is
moving on the screen.

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
  <td><pre><code>onPan(GestureState state,
   Point2D origin,
   Point2D translation,
   double velocity)</code></pre></td>
  <td><div class="block">
  Called when the pan gesture occurs.
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

  - <div id="onPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double)"
    class="section detail">

    ### onPan

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPan</span><span class="parameters">(@NonNull
    [GestureState](sdk-for-android-explore-com-here-sdk-gestures-gesturestate "enum class in com.here.sdk.gestures") state,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") translation,
    double velocity)</span>

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

</div>


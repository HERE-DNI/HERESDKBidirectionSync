---
title: "LongPressListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-longpresslistener"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">LongPressListener</span>

</div>

<div class="block">

Interface for handling long-press gestures. Long-press gesture occurs
after tapping and holding the finger for a long time on the screen.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onLongPress ( GestureState state, Point2D origin)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when the double long press gesture occurs.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-onLongPress-com-here-sdk-gestures-GestureState-com-here-sdk-core-Point2D"
    class="section detail">

    ### onLongPress

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLongPress</span><span class="parameters">(@NonNull
    [GestureState](sdk-for-android-explore-com-here-sdk-gestures-gesturestate "enum class in com.here.sdk.gestures") state,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Called when the double long press gesture occurs.

    </div>

    Parameters:  
    `state` -

    Determines in which state the gesture is.

    `origin` -

    Position of the touch point relative to the MapView in pixels.

    </div>

  </div>


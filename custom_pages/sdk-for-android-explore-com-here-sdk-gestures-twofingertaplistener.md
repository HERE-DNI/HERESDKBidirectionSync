---
title: "TwoFingerTapListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-twofingertaplistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TwoFingerTapListener</span>

</div>

<div class="block">

Interface for handling two finger tap gestures. Two finger tap gesture
occurs after tapping on the screen with two fingers.

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
  <td><pre><code>onTwoFingerTap(Point2D origin)</code></pre></td>
  <td><div class="block">
  Called when the double-tap gesture occurs.
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

  - <div id="onTwoFingerTap(com.here.sdk.core.Point2D)"
    class="section detail">

    ### onTwoFingerTap

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTwoFingerTap</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Called when the double-tap gesture occurs.

    </div>

    Parameters:  
    `origin` -

    Position halfway between two touch points relative to the MapView in
    pixels.

    </div>

  </div>

</div>


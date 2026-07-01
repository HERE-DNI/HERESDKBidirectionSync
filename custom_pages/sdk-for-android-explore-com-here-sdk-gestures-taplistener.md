---
title: "TapListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-gestures-taplistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.gestures](sdk-for-android-explore-com-here-sdk-gestures-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TapListener</span>

</div>

<div class="block">

Interface for handling tap gestures. Tap gesture occurs after tapping on
the screen.

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
  <td><pre><code>onTap(Point2D origin)</code></pre></td>
  <td><div class="block">
  Called when the tap gesture occurs.
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

  - <div id="onTap(com.here.sdk.core.Point2D)" class="section detail">

    ### onTap

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTap</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Called when the tap gesture occurs.

    </div>

    Parameters:  
    `origin` -

    Position of the touch point relative to the MapView in pixels.

    </div>

  </div>

</div>


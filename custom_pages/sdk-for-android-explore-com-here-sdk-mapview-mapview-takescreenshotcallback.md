---
title: "MapView.TakeScreenshotCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapView](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapView.TakeScreenshotCallback</span>

</div>

<div class="block">

Callback to be called on retrieval of screenshot. In case of any error
passed result is null.

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
  <td><pre><code>onScreenshotTaken(android.graphics.Bitmap bitmap)</code></pre></td>
  <td><div class="block">
  Callback to be called when screenshot is ready.
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

  - <div id="onScreenshotTaken(android.graphics.Bitmap)"
    class="section detail">

    ### onScreenshotTaken

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onScreenshotTaken</span><span class="parameters">(@Nullable
    android.graphics.Bitmap bitmap)</span>

    </div>

    <div class="block">

    Callback to be called when screenshot is ready.

    </div>

    Parameters:  
    `bitmap` - The bitmap containing the screenshot.

    </div>

  </div>

</div>


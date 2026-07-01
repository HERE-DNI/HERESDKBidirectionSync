---
title: "MapCamera.DryCameraUpdateCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcamera-drycameraupdatecallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapCamera](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")

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
</span><span class="element-name type-name-label">MapCamera.DryCameraUpdateCallback</span>

</div>

<div class="block">

Used to report back results of dry update application to camera. Note
that this is a beta release of this feature, so there could be a few
bugs and unexpected behaviors. Related APIs may change for new releases
without a deprecation process.

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
  <td><pre><code>onDryApplyUpdateResult(MapCamera.State cameraState)</code></pre></td>
  <td><div class="block">
  Used to report back results of dry update application to camera.
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

  - <div id="onDryApplyUpdateResult(com.here.sdk.mapview.MapCamera.State)"
    class="section detail">

    ### onDryApplyUpdateResult

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDryApplyUpdateResult</span><span class="parameters">(@Nullable
    [MapCamera.State](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state "class in com.here.sdk.mapview") cameraState)</span>

    </div>

    <div class="block">

    Used to report back results of dry update application to camera.
    Note that this is a beta release of this feature, so there could be
    a few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `cameraState` -

    Map camera state after dry application of update

    </div>

  </div>

</div>


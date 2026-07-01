---
title: "MapCameraListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcameralistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">MapCameraListener</span>

</div>

<div class="block">

Interface for objects that want to get updates whenever the map is
redrawn after camera parameters change.

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
  <td><pre><code>onMapCameraUpdated(MapCamera.State cameraState)</code></pre></td>
  <td><div class="block">
  Called on the main thread after the map is drawn.
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

  - <div id="onMapCameraUpdated(com.here.sdk.mapview.MapCamera.State)"
    class="section detail">

    ### onMapCameraUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapCameraUpdated</span><span class="parameters">(@NonNull
    [MapCamera.State](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state "class in com.here.sdk.mapview") cameraState)</span>

    </div>

    <div class="block">

    Called on the main thread after the map is drawn.

    </div>

    Parameters:  
    `cameraState` -

    Camera parameters at the time the map was drawn.

    </div>

  </div>

</div>


---
title: "MapCameraListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcameralistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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
<div id="sdk-for-android-explore-method-summary"
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

      onMapCameraUpdated(MapCamera.State cameraState)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called on the main thread after the map is drawn.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-onMapCameraUpdated(com.here.sdk.mapview.MapCamera.State)"
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


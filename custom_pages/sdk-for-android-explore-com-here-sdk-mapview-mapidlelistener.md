---
title: "MapIdleListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">MapIdleListener</span>

</div>

<div class="block">

Used to detect when the map becomes idle or busy. Map is considered busy
when its state changes (for example as a result of camera manipulation)
and/or when it requires a redraw (for example, as a result of map data
being downloaded). Map is considered idle when current state is fully
rendered and no further redraws are necessary.

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

      onMapBusy()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when map becomes invalidated and is about to be updated.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onMapIdle()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when map finishes all state updates.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-onMapBusy()"
    class="section detail">

    ### onMapBusy

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapBusy</span>()

    </div>

    <div class="block">

    Called when map becomes invalidated and is about to be updated. One
    or more redraws will happen afterwards, until onMapIdle() is called.

    </div>

    </div>
<div id="sdk-for-android-explore-onMapIdle()"
    class="section detail">

    ### onMapIdle

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapIdle</span>()

    </div>

    <div class="block">

    Called when map finishes all state updates. No state changes or
    redraws will happen aftrwards until onMapBusy() is called.

    </div>

    </div>

  </div>

</div>


---
title: "MapIdleListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

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
  <td><pre><code>onMapBusy()</code></pre></td>
  <td><div class="block">
  Called when map becomes invalidated and is about to be updated.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onMapIdle()</code></pre></td>
  <td><div class="block">
  Called when map finishes all state updates.
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

  - <div id="onMapBusy()" class="section detail">

    ### onMapBusy

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMapBusy</span>()

    </div>

    <div class="block">

    Called when map becomes invalidated and is about to be updated. One
    or more redraws will happen afterwards, until onMapIdle() is called.

    </div>

    </div>

  - <div id="onMapIdle()" class="section detail">

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


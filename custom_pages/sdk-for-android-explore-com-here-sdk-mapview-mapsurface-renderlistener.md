---
title: "MapSurface.RenderListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-mapsurface" title="class in com.here.sdk.mapview">MapSurface</a>

<div class="type-signature">

<span class="modifiers">public static interface </span><span class="element-name type-name-label">MapSurface.RenderListener</span>

</div>

<div class="block">

Listener of MapSurface render events. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

      onFramePrepared ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after each frame is prepared for rendering, before presenting it, from inside the render loop.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onRenderTargetReleased ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called after the render target has been released.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-onFramePrepared" class="section detail">

    ### onFramePrepared

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onFramePrepared</span>()

    </div>

    <div class="block">

    Called after each frame is prepared for rendering, before presenting it, from inside the render loop. Inside, custom rendering can be performed. It is recommended that the execution to be kept to a minimum as this can adversely affect the frame rendering time.

    </div>

    </div>

  - <div id="sdk-for-android-explore-onRenderTargetReleased" class="section detail">

    ### onRenderTargetReleased

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRenderTargetReleased</span>()

    </div>

    <div class="block">

    Called after the render target has been released. Inside, resources associated with any custom rendering can be released.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


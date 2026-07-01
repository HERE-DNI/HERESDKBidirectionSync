---
title: "MapSurface.RenderListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapSurface](sdk-for-android-explore-com-here-sdk-mapview-mapsurface "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapSurface.RenderListener</span>

</div>

<div class="block">

Listener of MapSurface render events. Note: This feature is in BETA
state and thus there can be bugs and unexpected behavior. Related APIs
may change for new releases without a deprecation process.

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
  <td><pre><code>onFramePrepared()</code></pre></td>
  <td><div class="block">
  Called after each frame is prepared for rendering, before presenting it,
  from inside the render loop.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onRenderTargetReleased()</code></pre></td>
  <td><div class="block">
  Called after the render target has been released.
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

  - <div id="onFramePrepared()" class="section detail">

    ### onFramePrepared

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onFramePrepared</span>()

    </div>

    <div class="block">

    Called after each frame is prepared for rendering, before presenting
    it, from inside the render loop. Inside, custom rendering can be
    performed. It is recommended that the execution to be kept to a
    minimum as this can adversely affect the frame rendering time.

    </div>

    </div>

  - <div id="onRenderTargetReleased()" class="section detail">

    ### onRenderTargetReleased

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRenderTargetReleased</span>()

    </div>

    <div class="block">

    Called after the render target has been released. Inside, resources
    associated with any custom rendering can be released.

    </div>

    </div>

  </div>

</div>


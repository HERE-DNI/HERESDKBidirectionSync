---
title: "MapSurface.RenderListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapSurface.RenderListener.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mapsurface" title="class in com.here.sdk.mapview">MapSurface</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapSurface.RenderListener</span></div>
<div class="block">Listener of MapSurface render events.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onFramePrepared()">onFramePrepared</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after each frame is prepared for rendering, before presenting it, from inside the
 render loop.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onRenderTargetReleased()">onRenderTargetReleased</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after the render target has been released.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="onFramePrepared()">
<h3>onFramePrepared</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onFramePrepared</span>()</div>
<div class="block">Called after each frame is prepared for rendering, before presenting it, from inside the
 render loop. Inside, custom rendering can be performed. It is recommended that the
 execution to be kept to a minimum as this can adversely affect the frame rendering time.</div>
</section>
</li>
<li>
<section class="detail" id="onRenderTargetReleased()">
<h3>onRenderTargetReleased</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRenderTargetReleased</span>()</div>
<div class="block">Called after the render target has been released.
 Inside, resources associated with any custom rendering can be released.</div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>

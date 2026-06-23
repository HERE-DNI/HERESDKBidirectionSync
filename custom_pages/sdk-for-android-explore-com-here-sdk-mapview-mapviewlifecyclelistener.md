---
title: "MapViewLifecycleListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapViewLifecycleListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MapViewLifecycleListener</span></div>
<div class="block"><p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
 whose lifecycle needs to be linked with that of a map view.
 </p><p>A configuration change that results in <code>Activity</code> being recreated does not trigger
 an <a href="sdk-for-android-explore-index#onDestroy()"><code>onDestroy()</code></a> call. The listener will be preserved throughout the
 destruction and recreation of the MapView. It is safe to hold and use the <code>MapViewBase</code>
 object passed in <a href="sdk-for-android-explore-index#onAttach(com.here.sdk.mapview.MapViewBase)"><code>onAttach(com.here.sdk.mapview.MapViewBase)</code></a> until <code>onDetach()</code> or <code>onDestroy()</code>
 gets called. However, it is important that the listener <em>does not</em> hold a strong reference
 to an <code>Activity</code>, directly or indirectly (for example by holding a reference to a
 <a href="sdk-for-android-explore-mapview" title="class in com.here.sdk.mapview"><code>MapView</code></a>. A component implementing this interface should interact with the map view
 only through the <code>MapViewBase</code> object passed in <a href="sdk-for-android-explore-index#onAttach(com.here.sdk.mapview.MapViewBase)"><code>onAttach(com.here.sdk.mapview.MapViewBase)</code></a>.
 </p><p>A <code>MapView</code> is using a <a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a>
</p><p>to render its content.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onAttach(com.here.sdk.mapview.MapViewBase)">onAttach</a><wbr/>(<a href="sdk-for-android-explore-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when adding <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to the map view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onDestroy()">onDestroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the map view to which this is attached to is destroyed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onDetach(com.here.sdk.mapview.MapViewBase)">onDetach</a><wbr/>(<a href="sdk-for-android-explore-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when removing <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from the map view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onPause()">onPause</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the map view to which this <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets paused
 (usually when the app goes into background).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onResume()">onResume</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the map view to which this <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets resumed
 (usually when the app goes into foreground).</div>
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
<section class="detail" id="onAttach(com.here.sdk.mapview.MapViewBase)">
<h3>onAttach</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onAttach</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Called when adding <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to the map view. If the map view does not
 have render target attached at the time of adding the listener, then this method will
 be called later, after render target is attached. This means that the map view it
 receives is always fully initialized.
 </p><p>Can be used to implement
 the logic to create and add visual components to the map view.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The map view to attach to.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onDetach(com.here.sdk.mapview.MapViewBase)">
<h3>onDetach</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onDetach</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Called when removing <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from the map view. Can be used to implement
 the logic to remove visual components from the map view and release resources if necessary.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The map view to detach from.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onPause()">
<h3>onPause</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onPause</span>()</div>
<div class="block"><p>Called when the map view to which this <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets paused
 (usually when the app goes into background). This should be used by components that
 perform continuous updates to pause those updates until <a href="sdk-for-android-explore-index#onResume()"><code>onResume()</code></a>
 is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="onResume()">
<h3>onResume</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onResume</span>()</div>
<div class="block"><p>Called when the map view to which this <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets resumed
 (usually when the app goes into foreground). This should be used by components that
 perform continuous updates to resume those updates after a previous call to
 <a href="sdk-for-android-explore-index#onPause()"><code>onPause()</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="onDestroy()">
<h3>onDestroy</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onDestroy</span>()</div>
<div class="block"><p>Called when the map view to which this is attached to is destroyed.
 After this is called, no other <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> method will be invoked.
 This should be used to make sure all resources are freed.</p></div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>

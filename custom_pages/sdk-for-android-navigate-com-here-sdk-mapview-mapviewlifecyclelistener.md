---
title: "MapViewLifecycleListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapViewLifecycleListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">MapViewLifecycleListener</span></div>
<div className="block"><p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
 whose lifecycle needs to be linked with that of a map view.
 A configuration change that results in <code>Activity</code> being recreated does not trigger
 an <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener#onDestroy()"><code>onDestroy()</code></a> call. The listener will be preserved throughout the
 destruction and recreation of the MapView. It is safe to hold and use the <code>MapViewBase</code>
 object passed in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener#onAttach(com.here.sdk.mapview.MapViewBase)"><code>onAttach(com.here.sdk.mapview.MapViewBase)</code></a> until <code>onDetach()</code> or <code>onDestroy()</code>
 gets called. However, it is important that the listener <em>does not</em> hold a strong reference
 to an <code>Activity</code>, directly or indirectly (for example by holding a reference to a
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview"><code>MapView</code></a>. A component implementing this interface should interact with the map view
 only through the <code>MapViewBase</code> object passed in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener#onAttach(com.here.sdk.mapview.MapViewBase)"><code>onAttach(com.here.sdk.mapview.MapViewBase)</code></a>.
 A <code>MapView</code> is using a <a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a>
to render its content.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="onAttach(com.here.sdk.mapview.MapViewBase)">
<h3>onAttach</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onAttach</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div className="block"><p>Called when adding <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to the map view. If the map view does not
 have render target attached at the time of adding the listener, then this method will
 be called later, after render target is attached. This means that the map view it
 receives is always fully initialized.
 Can be used to implement
 the logic to create and add visual components to the map view.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The map view to attach to.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onDetach(com.here.sdk.mapview.MapViewBase)">
<h3>onDetach</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onDetach</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div className="block"><p>Called when removing <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from the map view. Can be used to implement
 the logic to remove visual components from the map view and release resources if necessary.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The map view to detach from.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onPause()">
<h3>onPause</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onPause</span>()</div>
<div className="block"><p>Called when the map view to which this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets paused
 (usually when the app goes into background). This should be used by components that
 perform continuous updates to pause those updates until <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener#onResume()"><code>onResume()</code></a>
 is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="onResume()">
<h3>onResume</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onResume</span>()</div>
<div className="block"><p>Called when the map view to which this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> is attached to gets resumed
 (usually when the app goes into foreground). This should be used by components that
 perform continuous updates to resume those updates after a previous call to
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener#onPause()"><code>onPause()</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="onDestroy()">
<h3>onDestroy</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onDestroy</span>()</div>
<div className="block"><p>Called when the map view to which this is attached to is destroyed.
 After this is called, no other <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> method will be invoked.
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
</div>



</div>
`
}</HTMLBlock>

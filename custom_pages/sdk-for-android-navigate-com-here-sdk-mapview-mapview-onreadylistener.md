---
title: "MapView.OnReadyListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapView.OnReadyListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview">MapView</a></dd>
</dl>
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public static interface </span><span className="element-name type-name-label">MapView.OnReadyListener</span></div>
<div className="block"><p>Listener that gets notified when MapView is fully initialized and ready to handle all
 operations, which means that map scene is loaded and drawing surface is ready to render
 a map.

 Whenever there is a need to call any map view related functions directly after
 the <code>Activity</code> resumes, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener#onMapViewReady()"><code>onMapViewReady()</code></a> should be used for this purpose,
 as it guarantees that those operations will work. It is not recommended to call
 map view functionality directly from <code>Activity</code>'s <code>onResume()</code>.

 There are few typical moments in the lifecycle where it's useful to execute map view
 related operations:
     <ul>
<li>After map is shown for the very first time
             - use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview"><code>MapScene.LoadSceneCallback</code></a> that is passed to
             <a href="sdk-for-android-navigate-mapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a>.</li>
<li>After the Activity is resumed
             - use <code>OnReadyListener</code> that is registered from within
             <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview"><code>MapScene.LoadSceneCallback</code></a> the first time map scene is loaded.</li>
<li>Every time the Activity is resumed, including after the map scene is first loaded
             - this combines previous two cases. Use <code>OnReadyListener</code> that is
             registered right after MapView is created, but before map scene is loaded.</li>
</ul></p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list-long">
<li><a href="sdk-for-android-navigate-mapview#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener)"><code>MapView.setOnReadyListener(OnReadyListener)</code></a></li>
</ul>
</dd>
</dl>
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
<section className="detail" id="onMapViewReady()">
<h3>onMapViewReady</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onMapViewReady</span>()</div>
<div className="block">Callback to be called when MapView is fully initialized and ready to handle all
 operations.</div>
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

---
title: "MapView.OnReadyListener (API Reference)"
slug: "sdk-for-android-navigate-mapview-onreadylistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapView.OnReadyListener.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-mapview" title="class in com.here.sdk.mapview">MapView</a></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapView.OnReadyListener</span></div>
<div class="block"><p>Listener that gets notified when MapView is fully initialized and ready to handle all
 operations, which means that map scene is loaded and drawing surface is ready to render
 a map.

 </p><p>Whenever there is a need to call any map view related functions directly after
 the <code>Activity</code> resumes, <a href="#onMapViewReady()"><code>onMapViewReady()</code></a> should be used for this purpose,
 as it guarantees that those operations will work. It is not recommended to call
 map view functionality directly from <code>Activity</code>'s <code>onResume()</code>.

 </p><p>There are few typical moments in the lifecycle where it's useful to execute map view
 related operations:
     <ul>
<li>After map is shown for the very first time
             - use <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview"><code>MapScene.LoadSceneCallback</code></a> that is passed to
             <a href="sdk-for-android-navigate-mapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a>.</li>
<li>After the Activity is resumed
             - use <code>OnReadyListener</code> that is registered from within
             <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview"><code>MapScene.LoadSceneCallback</code></a> the first time map scene is loaded.</li>
<li>Every time the Activity is resumed, including after the map scene is first loaded
             - this combines previous two cases. Use <code>OnReadyListener</code> that is
             registered right after MapView is created, but before map scene is loaded.</li>
</ul></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="sdk-for-android-navigate-mapview#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener)"><code>MapView.setOnReadyListener(OnReadyListener)</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onMapViewReady()">onMapViewReady</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Callback to be called when MapView is fully initialized and ready to handle all
 operations.</div>
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
<section class="detail" id="onMapViewReady()">
<h3>onMapViewReady</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMapViewReady</span>()</div>
<div class="block">Callback to be called when MapView is fully initialized and ready to handle all
 operations.</div>
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
</div>



</div>
`
}</HTMLBlock>

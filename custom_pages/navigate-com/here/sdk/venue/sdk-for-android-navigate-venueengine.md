---
title: "VenueEngine (API Reference)"
slug: "sdk-for-android-navigate-venueengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueEngine.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


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
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.VenueEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VenueEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>VenueEngine is an add-on to the base map functionality with its
 own content loading and cache.
 VenueEngine gives access to the venue functionality, which allows you
 to load and visualize venues on the map, search content inside venues etc.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.venue.VenueEngineInitCallback)">VenueEngine</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.venue.VenueEngineInitCallback)">VenueEngine</a><wbr/>(<a href="sdk-for-android-navigate-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Releases all internally used resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueMap()">getVenueMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a venue map to visualize venues.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueService()">getVenueService</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the venue service.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(com.here.sdk.core.AuthenticationCallback)">start</a><wbr/>(<a href="sdk-for-android-navigate-core-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Authenticates asynchronously using HERE SDK credentials and uses a result token to start
 the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(java.lang.String)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Authenticates asynchronously using HERE SDK credentials using a token to start
 the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.venue.VenueEngineInitCallback)">
<h3>VenueEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VenueEngine</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span>
            throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>The optional callback that will be triggered when a venue engine initialization
     will be completed. After the initialization, the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> should
     be started using one of its methods or using <a href="#start(java.lang.String)"><code>start(String)</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.venue.VenueEngineInitCallback)">
<h3>VenueEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VenueEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @Nullable
 <a href="sdk-for-android-navigate-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span>
            throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of existing SDKEngine.</p></dd>
<dd><code>callback</code> - <p>The optional callback that will be triggered when a venue engine initialization
     will be completed. After the initialization, the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> should
     be started using one of its methods or using <a href="#start(java.lang.String)"><code>start(String)</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="start(com.here.sdk.core.AuthenticationCallback)">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-core-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</span></div>
<div class="block"><p>Authenticates asynchronously using HERE SDK credentials and uses a result token to start
 the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. An initialization status of the venue service is
 returned to objects registered as <a href="sdk-for-android-navigate-service-venueservicelistener" title="interface in com.here.sdk.venue.service"><code>VenueServiceListener</code></a>. If the
 authentication will fail, the venue service will not be started.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>The optional callback that will be triggered when the authentication will be completed.
     If the authentication fails, the venue service will not be started.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(java.lang.String)">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</span></div>
<div class="block"><p>Authenticates asynchronously using HERE SDK credentials using a token to start
 the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. An initialization status of the venue service is
 returned to objects registered as <a href="sdk-for-android-navigate-service-venueservicelistener" title="interface in com.here.sdk.venue.service"><code>VenueServiceListener</code></a>. If the
 authentication will fail, the venue service will not be started.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>token</code> - <p>SDK project scope token to be used for authentication</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block"><p>Releases all internally used resources. The instance can't be used anymore after calling
 this method.</p></div>
</section>
</li>
<li>
<section class="detail" id="getVenueService()">
<h3>getVenueService</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span class="element-name">getVenueService</span>()</div>
<div class="block"><p>Gets the venue service. This service can be used to load the venue model objects.
 <p>Gets the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. This service
 can be used to load the <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> objects.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The venue service.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueMap()">
<h3>getVenueMap</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a></span> <span class="element-name">getVenueMap</span>()</div>
<div class="block"><p>Gets a venue map to visualize venues.
 <p>Gets a venue map to visualize venues and control the
 state of the venues on the map. You need to start the <a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> to
 be able to load venues.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The venue map.</p></dd>
</dl>
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
</body>
</html>

</div>
`
}</HTMLBlock>

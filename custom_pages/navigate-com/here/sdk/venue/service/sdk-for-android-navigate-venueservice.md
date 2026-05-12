---
title: "VenueService (API Reference)"
slug: "sdk-for-android-navigate-venueservice"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueService.html -->
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
<li><a href="#nested-class-summary">Nested</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.service</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.service.VenueService</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VenueService</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Offers methods to download venues. Use of this
 object does not necessitate Map involvement.
 <p>
 Before loading the venues, initialize the venue service
 with one of the start methods.

 <p>
 The venue service is online only. Even if there is a cached
 venue on the device, the venue service requires an online
 connection to check if the venue is available for the user.</p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-venueservice.venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional features enum</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.service.VenueListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.service.VenueMapListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue map listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.service.VenueServiceListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a service listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueToLoad(int)">addVenueToLoad</a><wbr/>(int venueId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue to the loading queue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueToLoad(java.lang.String)">addVenueToLoad</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue to the loading queue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">VenueServiceInitStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInitStatus()">getInitStatus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an initialization status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLanguage()">getLanguage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an active language in the venue service.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLanguages()">getLanguages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the languages available in the venue service.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInitialized()">isInitialized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if the venue service is initialized.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadOptionalFeatures(java.util.List)">loadOptionalFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venueservice.venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a>&gt; optionalFeatureList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Lets user load optional features for current session.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTopologies()">loadTopologies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Lets user load topologies for current session</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.service.VenueListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a venue listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.service.VenueMapListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a venue map listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.service.VenueServiceListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a service listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHrn(java.lang.String)">setHrn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hrn)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets HRN of platform catalog.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLabeltextPreference(java.util.List)">setLabeltextPreference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; labelTextPref)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets override labelTextPreference for labels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLanguage(java.lang.String)">setLanguage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets an active language.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#stop()">stop</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops the venue service.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="stop()">
<h3>stop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()</div>
<div class="block"><p>Stops the venue service.</p></div>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.service.VenueServiceListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span></div>
<div class="block"><p>Adds a service listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The service listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.service.VenueServiceListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span></div>
<div class="block"><p>Removes a service listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The service listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.service.VenueListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span></div>
<div class="block"><p>Adds a venue listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.service.VenueListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span></div>
<div class="block"><p>Removes a venue listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.service.VenueMapListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span></div>
<div class="block"><p>Adds a venue map listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue map listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.service.VenueMapListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span></div>
<div class="block"><p>Removes a venue map listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue map listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInitStatus()">
<h3>getInitStatus</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">VenueServiceInitStatus</a></span> <span class="element-name">getInitStatus</span>()</div>
<div class="block"><p>Gets an initialization status.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The initialization status.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInitialized()">
<h3>isInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInitialized</span>()</div>
<div class="block"><p>Checks if the venue service is initialized.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if the venue service is initialized and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVenueToLoad(int)">
<h3>addVenueToLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueToLoad</span><wbr/><span class="parameters">(int venueId)</span></div>
<div class="block"><p>Adds a venue to the loading queue.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The id of the venue to load.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVenueToLoad(java.lang.String)">
<h3>addVenueToLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueToLoad</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div class="block"><p>Adds a venue to the loading queue.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The id of the venue to load.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHrn(java.lang.String)">
<h3>setHrn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHrn</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hrn)</span></div>
<div class="block"><p>Sets HRN of platform catalog.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hrn</code> - <p>The HRN of platform catalog.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLabeltextPreference(java.util.List)">
<h3>setLabeltextPreference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLabeltextPreference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; labelTextPref)</span></div>
<div class="block"><p>Sets override labelTextPreference for labels.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>labelTextPref</code> - <p>The list of string override labelTextPreference.
     <p>
     "OCCUPANT_NAMES" - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348

     <p>
     "SPACE_NAME" - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348

     <p>
     "SPACE_TYPE_NAME" - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348

     <p>
     "SPACE_CATEGORY_NAME" - To display only space categories on map as a label text. Example: SAFETY for id 7348

     <p>
     "INTERNAL_ADDRESS" - To display only internal addresses on map as a label text. Example: 51/D for id 7348</p></p></p></p></p></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadTopologies()">
<h3>loadTopologies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadTopologies</span>()</div>
<div class="block"><p>Lets user load topologies for current session</p></div>
</section>
</li>
<li>
<section class="detail" id="loadOptionalFeatures(java.util.List)">
<h3>loadOptionalFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadOptionalFeatures</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venueservice.venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a>&gt; optionalFeatureList)</span></div>
<div class="block"><p>Lets user load optional features for current session.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionalFeatureList</code> - <p>The list of optional feature enum VenueOptionalFeature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLanguages()">
<h3>getLanguages</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getLanguages</span>()</div>
<div class="block"><p>Gets the languages available in the venue service.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The languages available in the venue service.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLanguage</span>()</div>
<div class="block"><p>Gets an active language in the venue service.
 <p>The venue service will try to load
 a venue with a translation in the active language. If such translation doesn't
 exist, a venue will be loaded in its default language.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The active language.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLanguage(java.lang.String)">
<h3>setLanguage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLanguage</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets an active language.
 <p>The venue service will try to load
 a venue with a translation in the active language. If such translation doesn't
 exist, a venue will be loaded in its default language.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The active language.</p></dd>
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

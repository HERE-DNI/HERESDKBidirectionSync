---
title: "VenueMap (API Reference)"
slug: "sdk-for-android-navigate-venuemap"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueMap.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.control.VenueMap</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VenueMap</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Connects a map with venues. When the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> is started,
 venues can be seen on the map as interactive models. The user can switch drawings and levels,
 change a visual style of geometries and related labels inside the venue etc.
 After constructing the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>, listeners
 for relevant events should be added to the object. <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> is an add-on to
 the base map functionality with its own content loading and cache. For this reason, in certain
 situations there may be a small delay before the venue is visible.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueDrawingSelectionListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a drawing selection listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueInfoListListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a listener to handle the completion of the asynchronous venue info list retrieval.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueLevelSelectionListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a level selection listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueLifecycleListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue lifecycle listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueMapLifecycleListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue map lifecycle listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.here.sdk.venue.control.VenueSelectionListener)">add</a><wbr/>(<a href="sdk-for-android-navigate-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a venue selection listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueAsync(int)">addVenueAsync</a><wbr/>(int venueId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">addVenueAsync</a><wbr/>(int venueId,
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueAsync(java.lang.String)">addVenueAsync</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">addVenueAsync</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cancelVenueSelection()">cancelVenueSelection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Attempts to cancel venue loading and selection
 that may currently be in progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCrosswalk(com.here.sdk.core.GeoCoordinates)">getCrosswalk</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to find a <a href="sdk-for-android-navigate-data-crosswalk" title="class in com.here.sdk.venue.data"><code>Crosswalk</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometry(com.here.sdk.core.GeoCoordinates)">getGeometry</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to find a <a href="sdk-for-android-navigate-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedVenue()">getSelectedVenue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTopology(com.here.sdk.core.GeoCoordinates)">getTopology</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to find a <a href="sdk-for-android-navigate-data-venuetopology" title="class in com.here.sdk.venue.data"><code>VenueTopology</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenue(com.here.sdk.core.GeoCoordinates)">getVenue</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to find a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> at the specified geographic coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueInfoList()">getVenueInfoList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueInfoList(com.here.sdk.venue.control.VenueLoadErrorCallback)">getVenueInfoList</a><wbr/>(<a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueInfoListAsync()">getVenueInfoListAsync</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueInfoListAsync(com.here.sdk.venue.control.VenueLoadErrorCallback)">getVenueInfoListAsync</a><wbr/>(<a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVenueService()">getVenueService</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the venue service.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueDrawingSelectionListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a drawing selection listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueInfoListListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a listener for the asynchronous venue info list retrieval.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueLevelSelectionListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a level selection listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueLifecycleListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a venue lifecycle listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueMapLifecycleListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a venue map lifecycle listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.here.sdk.venue.control.VenueSelectionListener)">remove</a><wbr/>(<a href="sdk-for-android-navigate-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a venue selection listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeVenue(com.here.sdk.venue.control.Venue)">removeVenue</a><wbr/>(<a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> from the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectVenueAsync(int)">selectVenueAsync</a><wbr/>(int venueId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">selectVenueAsync</a><wbr/>(int venueId,
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectVenueAsync(java.lang.String)">selectVenueAsync</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">selectVenueAsync</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectedVenue(com.here.sdk.venue.control.Venue)">setSelectedVenue</a><wbr/>(<a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</div>
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
<section class="detail" id="addVenueAsync(int)">
<h3>addVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr/><span class="parameters">(int venueId)</span></div>
<div class="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVenueAsync(java.lang.String)">
<h3>addVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div class="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>addVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr/><span class="parameters">(int venueId,
 @NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and add.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>addVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 @NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and add.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeVenue(com.here.sdk.venue.control.Venue)">
<h3>removeVenue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeVenue</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span></div>
<div class="block"><p>Removes a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> from the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The venue to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectVenueAsync(int)">
<h3>selectVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr/><span class="parameters">(int venueId)</span></div>
<div class="block"><p>Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and select.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectVenueAsync(java.lang.String)">
<h3>selectVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div class="block"><p>Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and select.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>selectVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr/><span class="parameters">(int venueId,
 @NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and select.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>selectVenueAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 @NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>Downloads a <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and select.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelVenueSelection()">
<h3>cancelVenueSelection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">cancelVenueSelection</span>()</div>
<div class="block"><p>Attempts to cancel venue loading and selection
 that may currently be in progress.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if a venue was about to load and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenue(com.here.sdk.core.GeoCoordinates)">
<h3>getVenue</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span class="element-name">getVenue</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div class="block"><p>Tries to find a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> at the specified geographic coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where a venue is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Venue or <code>null</code> if there is no venue at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometry(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span class="element-name">getGeometry</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div class="block"><p>Tries to find a <a href="sdk-for-android-navigate-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the geometry is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Geometry or <code>null</code> if there is no geometry at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueLifecycleListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span></div>
<div class="block"><p>Adds a venue lifecycle listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueLifecycleListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span></div>
<div class="block"><p>Removes a venue lifecycle listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueMapLifecycleListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span></div>
<div class="block"><p>Adds a venue map lifecycle listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueMapLifecycleListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span></div>
<div class="block"><p>Removes a venue map lifecycle listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueSelectionListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span></div>
<div class="block"><p>Adds a venue selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueSelectionListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span></div>
<div class="block"><p>Removes a venue selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueDrawingSelectionListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span></div>
<div class="block"><p>Adds a drawing selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueDrawingSelectionListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span></div>
<div class="block"><p>Removes a drawing selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueLevelSelectionListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span></div>
<div class="block"><p>Adds a level selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueLevelSelectionListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span></div>
<div class="block"><p>Removes a level selection listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.here.sdk.venue.control.VenueInfoListListener)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span></div>
<div class="block"><p>Adds a listener to handle the completion of the asynchronous venue info list retrieval.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.here.sdk.venue.control.VenueInfoListListener)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span></div>
<div class="block"><p>Removes a listener for the asynchronous venue info list retrieval.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueInfoList()">
<h3>getVenueInfoList</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</span> <span class="element-name">getVenueInfoList</span>()</div>
<div class="block"><p>The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>returns the list of object of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueInfoList(com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>getVenueInfoList</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</span> <span class="element-name">getVenueInfoList</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>returns the list of object of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueInfoListAsync()">
<h3>getVenueInfoListAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getVenueInfoListAsync</span>()</div>
<div class="block"><p>The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.
 Downloads the list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> asynchronously.</p></div>
</section>
</li>
<li>
<section class="detail" id="getVenueInfoListAsync(com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>getVenueInfoListAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getVenueInfoListAsync</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div class="block"><p>The list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.
 Downloads the list of <a href="sdk-for-android-navigate-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> asynchronously.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback to receive the list of venue info if successful.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTopology(com.here.sdk.core.GeoCoordinates)">
<h3>getTopology</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></span> <span class="element-name">getTopology</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div class="block"><p>Tries to find a <a href="sdk-for-android-navigate-data-venuetopology" title="class in com.here.sdk.venue.data"><code>VenueTopology</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the topology is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Topology or <code>null</code> if there is no topology at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCrosswalk(com.here.sdk.core.GeoCoordinates)">
<h3>getCrosswalk</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></span> <span class="element-name">getCrosswalk</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div class="block"><p>Tries to find a <a href="sdk-for-android-navigate-data-crosswalk" title="class in com.here.sdk.venue.data"><code>Crosswalk</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the crosswalk is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Crosswalk or <code>null</code> if there is no crosswalk at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueService()">
<h3>getVenueService</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span class="element-name">getVenueService</span>()</div>
<div class="block"><p>Gets the venue service.
 <p>It can be used to search and get the <a href="sdk-for-android-navigate-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> objects.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>VenueService</code> object.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedVenue()">
<h3>getSelectedVenue</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span class="element-name">getSelectedVenue</span>()</div>
<div class="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.
 <p>Use <code>null</code> to deselect the venue.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The selected venue or <code>null</code> if no venue is selected.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedVenue(com.here.sdk.venue.control.Venue)">
<h3>setSelectedVenue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedVenue</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> value)</span></div>
<div class="block"><p>Sets the selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.
 <p>Use <code>null</code> to deselect the venue.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected venue or <code>null</code> if no venue is selected.</p></dd>
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

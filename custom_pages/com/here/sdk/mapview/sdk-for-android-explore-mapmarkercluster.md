---
title: "MapMarkerCluster (API Reference)"
slug: "sdk-for-android-explore-mapmarkercluster"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarkerCluster.html -->
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
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapMarkerCluster</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMarkerCluster</span>
<span class="extends-implements">extends <a href="../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
 them in a small area.
 <p>The markers that are close to each other are replaced by a single cluster marker. Cluster groups
 are generated based on geographical distance between objects, not based on screen space collision.
 Hence it is possible, that cluster markers can overlap.
 <p>The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
 map, add it to the scene using <a href="MapScene.html#addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)"><code>MapScene.addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)</code></a>. The display of a cluster is only
 guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
 that mostly affects clusters which are visually large and cover a sizeable part of the viewport.
 <p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p></p></p></p></div>
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
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MapMarkerCluster.CounterStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a></code></div>
<div class="col-last even-row-color">
<div class="block">Styling options for a marker cluster which is represented by the marker count as a text.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MapMarkerCluster.Grouping.html" title="class in com.here.sdk.mapview">MapMarkerCluster.Grouping</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Represents a group of map markers belonging to a cluster.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MapMarkerCluster.ImageStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a></code></div>
<div class="col-last even-row-color">
<div class="block">This class specifies the visual appearance of a cluster marker.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle)">MapMarkerCluster</a><wbr/>(<a href="MapMarkerCluster.ImageStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of a map marker cluster which is represented as an image.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle)">MapMarkerCluster</a><wbr/>(<a href="MapMarkerCluster.ImageStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle,
 <a href="MapMarkerCluster.CounterStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a> counterStyle)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of a map marker cluster which is represented as an image along with a counter
 showing how many markers are actually grouped under particular cluster icon.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarker(com.here.sdk.mapview.MapMarker)">addMapMarker</a><wbr/>(<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map marker to this cluster.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarkers(java.util.List)">addMapMarkers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a list of map markers to this cluster.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMarkers()">getMarkers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of map markers which currently belong to this cluster.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpacity()">getOpacity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current opacity of the marker cluster image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapMarkers()">removeAllMapMarkers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all map markers from this cluster.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarker(com.here.sdk.mapview.MapMarker)">removeMapMarker</a><wbr/>(<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a> marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map marker from this cluster.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarkers(java.util.List)">removeMapMarkers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a list of map markers from this cluster.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpacity(double)">setOpacity</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the opacity of the marker cluster image.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMarkerCluster.ImageStyle)">
<h3>MapMarkerCluster</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarkerCluster</span><wbr/><span class="parameters">(@NonNull
 <a href="MapMarkerCluster.ImageStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle)</span></div>
<div class="block"><p>Creates a new instance of a map marker cluster which is represented as an image.
 <p>Any modification to object passed as <code>imageStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageStyle</code> - <p>The visual representation for the cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle)">
<h3>MapMarkerCluster</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarkerCluster</span><wbr/><span class="parameters">(@NonNull
 <a href="MapMarkerCluster.ImageStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle,
 @NonNull
 <a href="MapMarkerCluster.CounterStyle.html" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a> counterStyle)</span></div>
<div class="block"><p>Creates a new instance of a map marker cluster which is represented as an image along with a counter
 showing how many markers are actually grouped under particular cluster icon.
 <p>Any modification to <code>imageStyle</code> or <code>counterStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageStyle</code> - <p>Describes the visual appearance of cluster icon.</p></dd>
<dd><code>counterStyle</code> - <p>Describes the appearance of marker count label.</p></dd>
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
<section class="detail" id="addMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>addMapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div class="block"><p>Adds a map marker to this cluster. Adding a marker which is already part of the cluster or
 which was already added to the map scene has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapMarkers(java.util.List)">
<h3>addMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div class="block"><p>Adds a list of map markers to this cluster.
 <p>Markers which are already part of the cluster or
 which were already added to the map scene will be ignored.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>removeMapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div class="block"><p>Removes a map marker from this cluster.
 <p>Removing a marker which is not part of this cluster has no effect.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarkers(java.util.List)">
<h3>removeMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div class="block"><p>Removes a list of map markers from this cluster.
 <p>Removing markers which are not part of this cluster has no effect.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapMarkers()">
<h3>removeAllMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers</span>()</div>
<div class="block"><p>Removes all map markers from this cluster.</p></div>
</section>
</li>
<li>
<section class="detail" id="getMarkers()">
<h3>getMarkers</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a>&gt;</span> <span class="element-name">getMarkers</span>()</div>
<div class="block"><p>Returns the list of map markers which currently belong to this cluster.
 <p>Modifying the list has no effect on the marker cluster.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of map markers which currently belong to this cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()</div>
<div class="block"><p>Gets the current opacity of the marker cluster image.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the opacity of the marker cluster image.
 <p>Provided value is clamped in range [0.0, 1.0]. Default value is 1.0 which means marker cluster
 is displayed with the default opacity of the image.
 <p>Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.
 <p>Markers part of cluster will use their respective opacity when not displayed as a cluster icon.</p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.</p></dd>
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

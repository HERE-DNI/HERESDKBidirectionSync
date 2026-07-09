---
title: "MapMarkerCluster (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMarkerCluster.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapMarkerCluster</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapMarkerCluster</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
 them in a small area.
 The markers that are close to each other are replaced by a single cluster marker. Cluster groups
 are generated based on geographical distance between objects, not based on screen space collision.
 Hence it is possible, that cluster markers can overlap.
 The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
 map, add it to the scene using <a href="sdk-for-android-navigate-mapscene#addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)"><code>MapScene.addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)</code></a>. The display of a cluster is only
 guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
 that mostly affects clusters which are visually large and cover a sizeable part of the viewport.
 Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-counterstyle" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a></code></div>
<div className="col-last even-row-color">
<div className="block">Styling options for a marker cluster which is represented by the marker count as a text.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-grouping" title="class in com.here.sdk.mapview">MapMarkerCluster.Grouping</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Represents a group of map markers belonging to a cluster.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-imagestyle" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a></code></div>
<div className="col-last even-row-color">
<div className="block">This class specifies the visual appearance of a cluster marker.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle)">MapMarkerCluster</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-imagestyle" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of a map marker cluster which is represented as an image.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle)">MapMarkerCluster</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-imagestyle" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-counterstyle" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a> counterStyle)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of a map marker cluster which is represented as an image along with a counter
 showing how many markers are actually grouped under particular cluster icon.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMarkerCluster.ImageStyle)">
<h3>MapMarkerCluster</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarkerCluster</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-imagestyle" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle)</span></div>
<div className="block"><p>Creates a new instance of a map marker cluster which is represented as an image.
 Any modification to object passed as <code>imageStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>imageStyle</code> - <p>The visual representation for the cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle)">
<h3>MapMarkerCluster</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarkerCluster</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-imagestyle" title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a> imageStyle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-counterstyle" title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a> counterStyle)</span></div>
<div className="block"><p>Creates a new instance of a map marker cluster which is represented as an image along with a counter
 showing how many markers are actually grouped under particular cluster icon.
 Any modification to <code>imageStyle</code> or <code>counterStyle</code> after creation of <code>MapMarkerCluster</code> does not have any effect.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="addMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>addMapMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarker</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div className="block"><p>Adds a map marker to this cluster. Adding a marker which is already part of the cluster or
 which was already added to the map scene has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapMarkers(java.util.List)">
<h3>addMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarkers</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div className="block"><p>Adds a list of map markers to this cluster.
 Markers which are already part of the cluster or
 which were already added to the map scene will be ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>removeMapMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarker</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div className="block"><p>Removes a map marker from this cluster.
 Removing a marker which is not part of this cluster has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarkers(java.util.List)">
<h3>removeMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarkers</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div className="block"><p>Removes a list of map markers from this cluster.
 Removing markers which are not part of this cluster has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapMarkers()">
<h3>removeAllMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapMarkers</span>()</div>
<div className="block"><p>Removes all map markers from this cluster.</p></div>
</section>
</li>
<li>
<section className="detail" id="getMarkers()">
<h3>getMarkers</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt;</span> <span className="element-name">getMarkers</span>()</div>
<div className="block"><p>Returns the list of map markers which currently belong to this cluster.
 Modifying the list has no effect on the marker cluster.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of map markers which currently belong to this cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getOpacity</span>()</div>
<div className="block"><p>Gets the current opacity of the marker cluster image.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOpacity</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the opacity of the marker cluster image.
 Provided value is clamped in range [0.0, 1.0]. Default value is 1.0 which means marker cluster
 is displayed with the default opacity of the image.
 Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.
 Markers part of cluster will use their respective opacity when not displayed as a cluster icon.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>

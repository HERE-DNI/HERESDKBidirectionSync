---
title: "Venue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venue"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Venue.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.control.Venue</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Venue</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Controls the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> inside the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> object.
 The venue controls the selection of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> and the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>
 of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>. It provides the possibility to customize styles for the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a>.
 Objects of this class can only be created using methods
 <a href="sdk-for-android-navigate-venuemap#addVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.addVenueAsync(String, VenueLoadErrorCallback)</code></a> and <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a>.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getSelectedDrawing()">getSelectedDrawing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getSelectedLevel()">getSelectedLevel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getSelectedLevelIndex()">getSelectedLevelIndex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> in the level array
 of the related <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getSelectedLevelZIndex()">getSelectedLevelZIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the Z index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getVenueModel()">getVenueModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> controlled by this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#getVenueStyle()">getVenueStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style"><code>VenueStyle</code></a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 controlled by this object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#isTopologyVisible()">isTopologyVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current status of topology visibility.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle,com.here.sdk.venue.style.VenueLabelStyle)">setCustomStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt; geometries,
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style,
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuelabelstyle" title="class in com.here.sdk.venue.style">VenueLabelStyle</a> labelStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom style for geometries and related labels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">setCustomStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt; topologies,
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom style for topologies.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setCustomStyleToCrosswalk(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">setCustomStyleToCrosswalk</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt; crosswalks,
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom style for crosswalk.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setSelectedDrawing(com.here.sdk.venue.data.VenueDrawing)">setSelectedDrawing</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setSelectedLevel(com.here.sdk.venue.data.VenueLevel)">setSelectedLevel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setSelectedLevelIndex(int)">setSelectedLevelIndex</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified index from the level array
 of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> as selected.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setSelectedLevelZIndex(int)">setSelectedLevelZIndex</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified Z index as selected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venue#setTopologyVisible(boolean)">setTopologyVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the topology visibility.</div>
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
<section class="detail" id="setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle,com.here.sdk.venue.style.VenueLabelStyle)">
<h3>setCustomStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyle</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt; geometries,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuelabelstyle" title="class in com.here.sdk.venue.style">VenueLabelStyle</a> labelStyle)</span></div>
<div class="block"><p>Sets a custom style for geometries and related labels.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometries</code> - <p>The list of geometries to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
<dd><code>labelStyle</code> - <p>The style for geometry labels, or <code>null</code> to reset the label style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">
<h3>setCustomStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyle</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt; topologies,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span></div>
<div class="block"><p>Sets a custom style for topologies.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>topologies</code> - <p>The list of topologies to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomStyleToCrosswalk(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">
<h3>setCustomStyleToCrosswalk</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyleToCrosswalk</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt; crosswalks,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span></div>
<div class="block"><p>Sets a custom style for crosswalk.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>crosswalks</code> - <p>The list of crosswalk to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueModel()">
<h3>getVenueModel</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a></span> <span class="element-name">getVenueModel</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> controlled by this object.
 It can be used to get the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 belonging to this object, like a building or a complex of buildings.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> controlled by this object.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVenueStyle()">
<h3>getVenueStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a></span> <span class="element-name">getVenueStyle</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style"><code>VenueStyle</code></a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 controlled by this object.
 It can be used to get the style of the venue. Contains the information about
 the geometry and label styles available for the venue.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style"><code>VenueStyle</code></a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
     controlled by this object.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedDrawing()">
<h3>getSelectedDrawing</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getSelectedDrawing</span>()</div>
<div class="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>.
 Only the selected drawing will be visible as active on the map. All others will be
 hidden or displayed without details, depending on the implementation of the renderer.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The selected drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedDrawing(com.here.sdk.venue.data.VenueDrawing)">
<h3>setSelectedDrawing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedDrawing</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> value)</span></div>
<div class="block"><p>Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected drawing will be visible as active on the map. All others will be
 hidden or displayed without details, depending on the implementation of the renderer.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedLevel()">
<h3>getSelectedLevel</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a></span> <span class="element-name">getSelectedLevel</span>()</div>
<div class="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected level will be visible as active on the map. All others will be
 hidden or displayed without details, depending on a renderer implementation.
 If the level doesn't belong to the currently selected drawing, it can not be selected.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The selected level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedLevel(com.here.sdk.venue.data.VenueLevel)">
<h3>setSelectedLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> value)</span></div>
<div class="block"><p>Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected level will be visible as active on the map. All others will be
 hidden or displayed without details, depending on a renderer implementation.
 If the level doesn't belong to the currently selected drawing, it can not be selected.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedLevelZIndex()">
<h3>getSelectedLevelZIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSelectedLevelZIndex</span>()</div>
<div class="block"><p>Gets the Z index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.
 Z index 0 represents the ground level, negative values represent
 underground levels, positive values - levels above the ground.
 Z index can also be taken from <a href="sdk-for-android-navigate-venuelevel#getZIndex()"><code>VenueLevel.getZIndex()</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedLevelZIndex(int)">
<h3>setSelectedLevelZIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevelZIndex</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified Z index as selected.
 Z index 0 represents the ground level, negative values represent
 underground levels, positive values - levels above the ground.
 Z index can also be taken from <a href="sdk-for-android-navigate-venuelevel#getZIndex()"><code>VenueLevel.getZIndex()</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedLevelIndex()">
<h3>getSelectedLevelIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSelectedLevelIndex</span>()</div>
<div class="block"><p>Gets the index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> in the level array
 of the related <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>. The level array can be taken from
 <a href="sdk-for-android-navigate-venuedrawing#getLevels()"><code>VenueDrawing.getLevels()</code></a>.
 Unlike the Z index, it can't have a negative value.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected from the level array
     of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedLevelIndex(int)">
<h3>setSelectedLevelIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevelIndex</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified index from the level array
 of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> as selected.
 Unlike the Z index, it can't have a negative value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected from the level array
     of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTopologyVisible()">
<h3>isTopologyVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTopologyVisible</span>()</div>
<div class="block"><p>Gets the current status of topology visibility.
 It can be used to check the status of topology visibility.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Returns true if topology is visible.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTopologyVisible(boolean)">
<h3>setTopologyVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTopologyVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets the topology visibility.
 It can be used to check the status of topology visibility.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Returns true if topology is visible.</p></dd>
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
`
}</HTMLBlock>

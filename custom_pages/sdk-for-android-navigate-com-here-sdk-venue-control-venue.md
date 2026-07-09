---
title: "Venue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venue"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Venue.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.control.Venue</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Venue</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Controls the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> inside the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> object.
 The venue controls the selection of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> and the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>
 of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>. It provides the possibility to customize styles for the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a>.
 Objects of this class can only be created using methods
 <a href="sdk-for-android-navigate-venuemap#addVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.addVenueAsync(String, VenueLoadErrorCallback)</code></a> and <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle,com.here.sdk.venue.style.VenueLabelStyle)">
<h3>setCustomStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCustomStyle</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt; geometries,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuelabelstyle" title="class in com.here.sdk.venue.style">VenueLabelStyle</a> labelStyle)</span></div>
<div className="block"><p>Sets a custom style for geometries and related labels.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometries</code> - <p>The list of geometries to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
<dd><code>labelStyle</code> - <p>The style for geometry labels, or <code>null</code> to reset the label style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCustomStyle(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">
<h3>setCustomStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCustomStyle</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt; topologies,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span></div>
<div className="block"><p>Sets a custom style for topologies.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>topologies</code> - <p>The list of topologies to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCustomStyleToCrosswalk(java.util.List,com.here.sdk.venue.style.VenueGeometryStyle)">
<h3>setCustomStyleToCrosswalk</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCustomStyleToCrosswalk</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt; crosswalks,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span></div>
<div className="block"><p>Sets a custom style for crosswalk.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>crosswalks</code> - <p>The list of crosswalk to apply the new style.</p></dd>
<dd><code>style</code> - <p>The style for geometries, or <code>null</code> to reset the style to default.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueModel()">
<h3>getVenueModel</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a></span> <span className="element-name">getVenueModel</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> controlled by this object.
 It can be used to get the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 belonging to this object, like a building or a complex of buildings.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> controlled by this object.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueStyle()">
<h3>getVenueStyle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a></span> <span className="element-name">getVenueStyle</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style"><code>VenueStyle</code></a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 controlled by this object.
 It can be used to get the style of the venue. Contains the information about
 the geometry and label styles available for the venue.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style"><code>VenueStyle</code></a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
     controlled by this object.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSelectedDrawing()">
<h3>getSelectedDrawing</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span className="element-name">getSelectedDrawing</span>()</div>
<div className="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>.
 Only the selected drawing will be visible as active on the map. All others will be
 hidden or displayed without details, depending on the implementation of the renderer.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The selected drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSelectedDrawing(com.here.sdk.venue.data.VenueDrawing)">
<h3>setSelectedDrawing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSelectedDrawing</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> value)</span></div>
<div className="block"><p>Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected drawing will be visible as active on the map. All others will be
 hidden or displayed without details, depending on the implementation of the renderer.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSelectedLevel()">
<h3>getSelectedLevel</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a></span> <span className="element-name">getSelectedLevel</span>()</div>
<div className="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected level will be visible as active on the map. All others will be
 hidden or displayed without details, depending on a renderer implementation.
 If the level doesn't belong to the currently selected drawing, it can not be selected.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The selected level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSelectedLevel(com.here.sdk.venue.data.VenueLevel)">
<h3>setSelectedLevel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSelectedLevel</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> value)</span></div>
<div className="block"><p>Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> from the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.
 Only the selected level will be visible as active on the map. All others will be
 hidden or displayed without details, depending on a renderer implementation.
 If the level doesn't belong to the currently selected drawing, it can not be selected.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSelectedLevelZIndex()">
<h3>getSelectedLevelZIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSelectedLevelZIndex</span>()</div>
<div className="block"><p>Gets the Z index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.
 Z index 0 represents the ground level, negative values represent
 underground levels, positive values - levels above the ground.
 Z index can also be taken from <a href="sdk-for-android-navigate-venuelevel#getZIndex()"><code>VenueLevel.getZIndex()</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSelectedLevelZIndex(int)">
<h3>setSelectedLevelZIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSelectedLevelZIndex</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified Z index as selected.
 Z index 0 represents the ground level, negative values represent
 underground levels, positive values - levels above the ground.
 Z index can also be taken from <a href="sdk-for-android-navigate-venuelevel#getZIndex()"><code>VenueLevel.getZIndex()</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSelectedLevelIndex()">
<h3>getSelectedLevelIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSelectedLevelIndex</span>()</div>
<div className="block"><p>Gets the index of the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> in the level array
 of the related <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>. The level array can be taken from
 <a href="sdk-for-android-navigate-venuedrawing#getLevels()"><code>VenueDrawing.getLevels()</code></a>.
 Unlike the Z index, it can't have a negative value.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected from the level array
     of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSelectedLevelIndex(int)">
<h3>setSelectedLevelIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSelectedLevelIndex</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> with the specified index from the level array
 of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> as selected.
 Unlike the Z index, it can't have a negative value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selected from the level array
     of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isTopologyVisible()">
<h3>isTopologyVisible</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTopologyVisible</span>()</div>
<div className="block"><p>Gets the current status of topology visibility.
 It can be used to check the status of topology visibility.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Returns true if topology is visible.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTopologyVisible(boolean)">
<h3>setTopologyVisible</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTopologyVisible</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Sets the topology visibility.
 It can be used to check the status of topology visibility.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>

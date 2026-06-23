---
title: "GPXTrackWriter (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GPXTrackWriter.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.GPXTrackWriter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GPXTrackWriter</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div class="block"><p>Writes GPX track points to <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.
 The instance of the class should be added as a listener to the
 <code>LocationEngine</code> for GPX track recording.
 Appends the new location to the back segment of the track whenever the listener is called.
 The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.
 </p><p>Use case examples:
 </p><p>A user wants to create and save a new <a href="sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> with one <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>:
 - create <a href="sdk-for-android-navigate-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> and add it as a location listener to <code>LocationEngine</code>.
 - set user parameters to <a href="sdk-for-android-navigate-index#getTrack()"><code>getTrack()</code></a> (e.g. <a href="sdk-for-android-navigate-gpxtrack#getName()"><code>GPXTrack.getName()</code></a> or <a href="sdk-for-android-navigate-gpxtrack#getDescription()"><code>GPXTrack.getDescription()</code></a>).
 - when writing is completed, create a new <a href="sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> with a list of one <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a> and save the document via <a href="sdk-for-android-navigate-gpxdocument#save(java.lang.String)"><code>GPXDocument.save(java.lang.String)</code></a>.
 </p><p>A user wants to modify and save <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a> in the existing <a href="sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a>:
 - load <a href="sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> from a file by the relevant constructor.
 - create <a href="sdk-for-android-navigate-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with the required track in the list <a href="sdk-for-android-navigate-gpxdocument#getTracks()"><code>GPXDocument.getTracks()</code></a>,
 add the created instance as a location listener to <code>LocationEngine</code>.
 - when writing is completed, save the document via <a href="sdk-for-android-navigate-gpxdocument#save(java.lang.String)"><code>GPXDocument.save(java.lang.String)</code></a>.
 </p><p>The <code>GPXDocument</code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">GPXTrackWriter</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of GPXTrackWriter with an empty track inside.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.navigation.GPXTrack)">GPXTrackWriter</a><wbr/>(<a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> track)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of <a href="sdk-for-android-navigate-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrack()">getTrack</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the GPX track into which GPX track points are written.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called each time a new location is available.</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>GPXTrackWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GPXTrackWriter</span>()</div>
<div class="block"><p>Creates a new instance of GPXTrackWriter with an empty track inside.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.GPXTrack)">
<h3>GPXTrackWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GPXTrackWriter</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> track)</span></div>
<div class="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.
 Use this constructor to append locations to an existing track.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>track</code> - <p>GPX track.</p></dd>
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
<section class="detail" id="getTrack()">
<h3>getTrack</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a></span> <span class="element-name">getTrack</span>()</div>
<div class="block"><p>Gets the GPX track into which GPX track points are written.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>GPX track into which GPX track points are written.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>location</code> - <p>Current location.</p></dd>
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

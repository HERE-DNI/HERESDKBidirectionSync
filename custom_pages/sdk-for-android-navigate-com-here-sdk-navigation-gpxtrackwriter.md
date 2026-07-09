---
title: "GPXTrackWriter (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GPXTrackWriter.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.GPXTrackWriter</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GPXTrackWriter</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div className="block"><p>Writes GPX track points to <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.
 The instance of the class should be added as a listener to the
 <code>LocationEngine</code> for GPX track recording.
 Appends the new location to the back segment of the track whenever the listener is called.
 The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.
 Use case examples:
 A user wants to create and save a new <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> with one <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>:
 - create <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> and add it as a location listener to <code>LocationEngine</code>.
 - set user parameters to <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter#getTrack()"><code>getTrack()</code></a> (e.g. <a href="sdk-for-android-navigate-gpxtrack#getName()"><code>GPXTrack.getName()</code></a> or <a href="sdk-for-android-navigate-gpxtrack#getDescription()"><code>GPXTrack.getDescription()</code></a>).
 - when writing is completed, create a new <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> with a list of one <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a> and save the document via <a href="sdk-for-android-navigate-gpxdocument#save(java.lang.String)"><code>GPXDocument.save(java.lang.String)</code></a>.
 A user wants to modify and save <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a> in the existing <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a>:
 - load <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> from a file by the relevant constructor.
 - create <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with the required track in the list <a href="sdk-for-android-navigate-gpxdocument#getTracks()"><code>GPXDocument.getTracks()</code></a>,
 add the created instance as a location listener to <code>LocationEngine</code>.
 - when writing is completed, save the document via <a href="sdk-for-android-navigate-gpxdocument#save(java.lang.String)"><code>GPXDocument.save(java.lang.String)</code></a>.
 The <code>GPXDocument</code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter#%3Cinit%3E()">GPXTrackWriter</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of GPXTrackWriter with an empty track inside.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter#%3Cinit%3E(com.here.sdk.navigation.GPXTrack)">GPXTrackWriter</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> track)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.</div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>GPXTrackWriter</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GPXTrackWriter</span>()</div>
<div className="block"><p>Creates a new instance of GPXTrackWriter with an empty track inside.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.GPXTrack)">
<h3>GPXTrackWriter</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GPXTrackWriter</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> track)</span></div>
<div className="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a> with <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation"><code>GPXTrack</code></a>.
 Use this constructor to append locations to an existing track.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getTrack()">
<h3>getTrack</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a></span> <span className="element-name">getTrack</span>()</div>
<div className="block"><p>Gets the GPX track into which GPX track points are written.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>GPX track into which GPX track points are written.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onLocationUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
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
</div>



</div>
`
}</HTMLBlock>

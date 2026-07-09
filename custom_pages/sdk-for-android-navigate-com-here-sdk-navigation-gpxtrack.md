---
title: "GPXTrack (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GPXTrack.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.GPXTrack</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GPXTrack</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Single track from the <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a>. Can be used as an input to the <a href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator" title="class in com.here.sdk.navigation"><code>LocationSimulator</code></a>.
 Can be created and modified via <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a>.</p></div>
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
<section className="detail" id="getLocations()">
<h3>getLocations</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a>&gt;</span> <span className="element-name">getLocations</span>()</div>
<div className="block"><p>Provides a list of all stored track points converted to a <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a> object.
 See <a href="https://www.topografix.com/GPX/1/1/#type_wptType">type_wptType</a> for more details on the <code>wptType</code> format that is used for a track point.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a> objects.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getName()">
<h3>getName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getName</span>()</div>
<div className="block"><p>Gets the value of the name of the element in the trkType. If nothing was set before, defaults to an empty string.
 Can be overridden by the user. If nothing was set before, defaults to an empty string.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The value of the name of the element in the trkType.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setName</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Sets the value of the name of the element in the trkType. Can be overridden by the user. Defaults to an empty string.
 Can be overridden by the user. If nothing was set before, defaults to an empty string.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The value of the name of the element in the trkType.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDescription()">
<h3>getDescription</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getDescription</span>()</div>
<div className="block"><p>Gets the value of the description of the element in the trkType. If nothing was set before, defaults to an empty string.
 Can be overridden by the user. If nothing was set before, defaults to an empty string.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The value of the description of the element in the trkType.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDescription</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Sets the value of the description of the element in the trkType. Can be overridden by the user. Defaults to an empty string.
 Can be overridden by the user. If nothing was set before, defaults to an empty string.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The value of the description of the element in the trkType.</p></dd>
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

---
title: "GeoCoordinatesUpdate (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoCoordinatesUpdate.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.GeoCoordinatesUpdate</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoCoordinatesUpdate</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents geographical coordinates in 3D space.
 Unlike <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core"><code>GeoCoordinates</code></a>, its members can be undefined, allowing for APIs
 that update only the specified parts of geo coordinates.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#altitude">altitude</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional altitude in meters.</div>
</div>
<div className="col-first odd-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#latitude">latitude</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional latitude in degrees.</div>
</div>
<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#longitude">longitude</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional longitude in degrees.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">GeoCoordinatesUpdate</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a GeoCoordinatesUpdate from GeoCoordinates</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#%3Cinit%3E(java.lang.Double,java.lang.Double)">GeoCoordinatesUpdate</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> latitude,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> longitude)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a GeoCoordinatesUpdate from the provided latitude and
 longitude values.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate#%3Cinit%3E(java.lang.Double,java.lang.Double,java.lang.Double)">GeoCoordinatesUpdate</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> latitude,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> longitude,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> altitude)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
 and alt values.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="latitude">
<h3>latitude</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">latitude</span></div>
<div className="block"><p>Optional latitude in degrees.</p></div>
</section>
</li>
<li>
<section className="detail" id="longitude">
<h3>longitude</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">longitude</span></div>
<div className="block"><p>Optional longitude in degrees.</p></div>
</section>
</li>
<li>
<section className="detail" id="altitude">
<h3>altitude</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">altitude</span></div>
<div className="block"><p>Optional altitude in meters.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.Double,java.lang.Double)">
<h3>GeoCoordinatesUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoCoordinatesUpdate</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> latitude,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> longitude)</span></div>
<div className="block"><p>Constructs a GeoCoordinatesUpdate from the provided latitude and
 longitude values.
 Corrects values of latitude and longitude if they exceed the ranges.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to <code>null</code>.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.Double,java.lang.Double,java.lang.Double)">
<h3>GeoCoordinatesUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoCoordinatesUpdate</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> latitude,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> longitude,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> altitude)</span></div>
<div className="block"><p>Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
 and alt values.
 Corrects values of latitude and longitude if they exceed the ranges.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to <code>null</code>.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to <code>null</code>.</p></dd>
<dd><code>altitude</code> - <p>Altitude in meters. NaN value is converted to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>GeoCoordinatesUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoCoordinatesUpdate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Constructs a GeoCoordinatesUpdate from GeoCoordinates</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>GeoCoordinates to construct GeoCoordinatesUpdate.</p></dd>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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

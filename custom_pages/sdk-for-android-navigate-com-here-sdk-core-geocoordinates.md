---
title: "GeoCoordinates (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geocoordinates"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoCoordinates.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.GeoCoordinates</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoCoordinates</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents geographical coordinates in 3D space.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#altitude">altitude</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional altitude in meters.</div>
</div>
<div className="col-first odd-row-color"><code>final double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#latitude">latitude</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Latitude in degrees.</div>
</div>
<div className="col-first even-row-color"><code>final double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#longitude">longitude</a></code></div>
<div className="col-last even-row-color">
<div className="block">Longitude in degrees.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#%3Cinit%3E(double,double)">GeoCoordinates</a><wbr/>(double latitude,
 double longitude)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a GeoCoordinates from the provided latitude and longitude values.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#%3Cinit%3E(double,double,double)">GeoCoordinates</a><wbr/>(double latitude,
 double longitude,
 double altitude)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.</div>
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
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">latitude</span></div>
<div className="block"><p>Latitude in degrees.</p></div>
</section>
</li>
<li>
<section className="detail" id="longitude">
<h3>longitude</h3>
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">longitude</span></div>
<div className="block"><p>Longitude in degrees.</p></div>
</section>
</li>
<li>
<section className="detail" id="altitude">
<h3>altitude</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">altitude</span></div>
<div className="block"><p>Optional altitude in meters.
 By convention, on iOS devices, altitude is set as meters relative to the
 mean sea level.
 On Android devices, altitude is set as meters relative to the WGS 84
 reference ellipsoid.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,double,double)">
<h3>GeoCoordinates</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoCoordinates</span><wbr/><span className="parameters">(double latitude,
 double longitude,
 double altitude)</span></div>
<div className="block"><p>Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.
 Corrects values of lat and long if they exceed the ranges.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to 0.0.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to 0.0.</p></dd>
<dd><code>altitude</code> - <p>Altitude in meters. NaN value is converted to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double,double)">
<h3>GeoCoordinates</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoCoordinates</span><wbr/><span className="parameters">(double latitude,
 double longitude)</span></div>
<div className="block"><p>Constructs a GeoCoordinates from the provided latitude and longitude values.
 Corrects values of latitude and longitude if they exceed the ranges.
 Altitude set to <code>null</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to 0.0.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to 0.0.</p></dd>
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
<li>
<section className="detail" id="distanceTo(com.here.sdk.core.GeoCoordinates)">
<h3>distanceTo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceTo</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</span></div>
<div className="block"><p>Computes distance (in meters) along the great circle between two coordinates.
 This method ignores altitude of both points.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Coordinates of the point to which the distance is computed.</p></dd>
<dt>Returns:</dt>
<dd><p>distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="interpolate(com.here.sdk.core.GeoCoordinates,double)">
<h3>interpolate</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">interpolate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> towardCoords,
 double factor)</span></div>
<div className="block"><p>Computes the coordinates of the interpolated location along the great circle between
 the two coordinates.
 The interpolation factor is clamped to the range <code>[0.0, 1.0]</code> where <code>0.0</code> identifies this
 <code>GeoCoordinates</code> and <code>1.0</code> indicates the other coordinates.
 The ratio between the distance to the interpolated coordinates and the distance to the other
 coordinates is approximately equal to the interpolation factor. When both coordinates have
 the altitude, then the altitude is interpolated as well; <code>null</code> otherwise.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>towardCoords</code> - <p>Coordinates of the point to which the interpolation is directed.</p></dd>
<dd><code>factor</code> - <p>The interpolation factor</p></dd>
<dt>Returns:</dt>
<dd><p>interpolated coordinates</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromString(java.lang.String)">
<h3>fromString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">fromString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</span></div>
<div className="block"><p>Constructs GeoCoordinates from the provided string in specified format.
 Corrects values of lat and long if they exceed the ranges.
 If the latitude value is out of range of [-90.0, 90.0] it's clamped to that range.
 If the longitude value is out of range of [-180.0, 180.0] it's replaced with a value
 within the range, representing effectively the same meridian.
 Examples: <code>53.43762,-13.65468</code>.
 <code>49°59'56.948"N, 15°48'22.989"E</code>
<code>50d4m17.698N 14d24m2.826E</code>
<code>49.9991522N, 150.8063858E</code>
<code>40°26′47″N 79°58′36″W</code></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - <p>String representing GeoCoordinates in one of supported formats.</p></dd>
<dt>Returns:</dt>
<dd><p>Created GeoCoordinates, or 'null' if string was not in appropriate format.</p></dd>
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

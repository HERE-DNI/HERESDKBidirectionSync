---
title: "Property (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-property"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Property.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.data.Property</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Property</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Holds information of varying types, such as Boolean, Integer, String. Properties are used
 in <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a> to describe this objects.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-property-propertytype" title="enum class in com.here.sdk.venue.data">Property.PropertyType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Types of properties.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getType()">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property-propertytype" title="enum class in com.here.sdk.venue.data">Property.PropertyType</a></span> <span className="element-name">getType</span>()</div>
<div className="block"><p>Gets a type of the property.
 It can be used to get type of property.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The type of the property.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isBool()">
<h3>isBool</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isBool</span>()</div>
<div className="block"><p>Gets the property as a Boolean value.
 Converts the value of the property to a boolean.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Boolean value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInt()">
<h3>getInt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getInt</span>()</div>
<div className="block"><p>Gets the property as an Integer value.
 Converts the value of the property to a Integer.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Integer value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getString()">
<h3>getString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getString</span>()</div>
<div className="block"><p>Gets the property as a String value.
 Converts the value of the property to a boolean.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The String value.</p></dd>
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

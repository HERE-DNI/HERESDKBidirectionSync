---
title: "GeoPlace (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-geoplace"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoPlace.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.GeoPlace</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoPlace</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>GeoPlace struct represents a location object:
 such as a country, a city, a point of interest (POI) etc.
 It can be used for PersonalPlace creation, in order to provide search on custom places.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search">Address</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#address">address</a></code></div>
<div className="col-last even-row-color">
<div className="block">Address of the place
 Note: Address can have default value when no data is available.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-businessdetails" title="class in com.here.sdk.search">BusinessDetails</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#business">business</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Business details
 Note: BusinessDetails can have default value when no data is available.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#categories">categories</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of corresponding categories
 Note: This list can be empty when no data is available.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-externalid" title="class in com.here.sdk.core">ExternalID</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#externalIDs">externalIDs</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Allows the client to set the id in their own system.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-locationdetails" title="class in com.here.sdk.search">LocationDetails</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#location">location</a></code></div>
<div className="col-last even-row-color">
<div className="block">Geographical details
 Note: Can be <code>null</code> when retrieved from a suggestion's place property.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#title">title</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The localized title for the resource.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-placetype" title="enum class in com.here.sdk.search">PlaceType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#type">type</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies place type.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-webdetails" title="class in com.here.sdk.search">WebDetails</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#web">web</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Contains info and direct web links to corresponding items.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-geoplace#%3Cinit%3E()">GeoPlace</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<section className="detail" id="title">
<h3>title</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">title</span></div>
<div className="block"><p>The localized title for the resource.
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="externalIDs">
<h3>externalIDs</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-externalid" title="class in com.here.sdk.core">ExternalID</a>&gt;</span> <span className="element-name">externalIDs</span></div>
<div className="block"><p>Allows the client to set the id in their own system.
 The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-placetype" title="enum class in com.here.sdk.search">PlaceType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Specifies place type.</p></div>
</section>
</li>
<li>
<section className="detail" id="categories">
<h3>categories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span className="element-name">categories</span></div>
<div className="block"><p>List of corresponding categories
 Note: This list can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="address">
<h3>address</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search">Address</a></span> <span className="element-name">address</span></div>
<div className="block"><p>Address of the place
 Note: Address can have default value when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="location">
<h3>location</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-locationdetails" title="class in com.here.sdk.search">LocationDetails</a></span> <span className="element-name">location</span></div>
<div className="block"><p>Geographical details
 Note: Can be <code>null</code> when retrieved from a suggestion's place property.</p></div>
</section>
</li>
<li>
<section className="detail" id="business">
<h3>business</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-businessdetails" title="class in com.here.sdk.search">BusinessDetails</a></span> <span className="element-name">business</span></div>
<div className="block"><p>Business details
 Note: BusinessDetails can have default value when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="web">
<h3>web</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-webdetails" title="class in com.here.sdk.search">WebDetails</a></span> <span className="element-name">web</span></div>
<div className="block"><p>Contains info and direct web links to corresponding items.
 Note: WebDetails can have default value when no data is available.</p></div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>GeoPlace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoPlace</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
<section className="detail" id="makeMyPlace(java.lang.String,com.here.sdk.core.GeoCoordinates)">
<h3>makeMyPlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-geoplace" title="class in com.here.sdk.search">GeoPlace</a></span> <span className="element-name">makeMyPlace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Creates a new instance of this class. All other properties will keep their default value
 and all properties containing lists will contain empty lists.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>title</code> - <p>The title.</p></dd>
<dd><code>coordinates</code> - <p>The coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>An instance of <a href="sdk-for-android-navigate-com-here-sdk-search-geoplace" title="class in com.here.sdk.search"><code>GeoPlace</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getID()">
<h3>getID</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getID</span>()</div>
<div className="block"><p>Allow the client to access GeoPlace id.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The place id.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isMyPlace()">
<h3>isMyPlace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isMyPlace</span>()</div>
<div className="block"><p>Allow the client to access info about is it my place or not.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if it is my place, <code>false</code> otherwise.</p></dd>
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

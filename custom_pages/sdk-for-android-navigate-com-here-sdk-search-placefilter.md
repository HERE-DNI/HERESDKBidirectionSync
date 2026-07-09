---
title: "PlaceFilter (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-placefilter"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PlaceFilter.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.PlaceFilter</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PlaceFilter</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The filter options to specify a place.
 Consists of fuel, truck and EV options.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter-ev" title="class in com.here.sdk.search">PlaceFilter.Ev</a></code></div>
<div className="col-last even-row-color">
<div className="block">Constraints that are applicable on the places of category EV station.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-placefilter-ev" title="class in com.here.sdk.search">PlaceFilter.Ev</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter#ev">ev</a></code></div>
<div className="col-last even-row-color">
<div className="block">Constraints that are applicable on the places of category EV station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-fueltype" title="enum class in com.here.sdk.transport">FuelType</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter#fuelTypes">fuelTypes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of <a href="sdk-for-android-navigate-com-here-sdk-transport-fueltype" title="enum class in com.here.sdk.transport"><code>FuelType</code></a> elements that should be used to find only
 the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results that support all of them.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-truckclass" title="enum class in com.here.sdk.transport">TruckClass</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter#truckClass">truckClass</a></code></div>
<div className="col-last even-row-color">
<div className="block">Should be used to find only the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results with minimum supported <a href="sdk-for-android-navigate-com-here-sdk-transport-truckclass" title="enum class in com.here.sdk.transport"><code>TruckClass</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckfueltype" title="enum class in com.here.sdk.transport">TruckFuelType</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter#truckFuelTypes">truckFuelTypes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of <a href="sdk-for-android-navigate-com-here-sdk-transport-truckfueltype" title="enum class in com.here.sdk.transport"><code>TruckFuelType</code></a> elements that should be used to find only
 the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results that support all of them.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placefilter#%3Cinit%3E()">PlaceFilter</a>()</code></div>
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
<section className="detail" id="fuelTypes">
<h3>fuelTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-fueltype" title="enum class in com.here.sdk.transport">FuelType</a>&gt;</span> <span className="element-name">fuelTypes</span></div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-transport-fueltype" title="enum class in com.here.sdk.transport"><code>FuelType</code></a> elements that should be used to find only
 the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results that support all of them.
 This filter is available to use with the <code>SearchEngine</code> and
 <code>OfflineSearchEngine</code> (only available for the Navigate license), however <code>OfflineSearchEngine</code>
 supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
 <code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
 <code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckFuelTypes">
<h3>truckFuelTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckfueltype" title="enum class in com.here.sdk.transport">TruckFuelType</a>&gt;</span> <span className="element-name">truckFuelTypes</span></div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-transport-truckfueltype" title="enum class in com.here.sdk.transport"><code>TruckFuelType</code></a> elements that should be used to find only
 the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results that support all of them.
 Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckClass">
<h3>truckClass</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckclass" title="enum class in com.here.sdk.transport">TruckClass</a></span> <span className="element-name">truckClass</span></div>
<div className="block"><p>Should be used to find only the <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search"><code>FuelStation</code></a> search results with minimum supported <a href="sdk-for-android-navigate-com-here-sdk-transport-truckclass" title="enum class in com.here.sdk.transport"><code>TruckClass</code></a>.
 This filter is only available to use with the <code>SearchEngine</code>.
 The <code>OfflineSearchEngine</code> (only available for the Navigate license) does not apply this filter.
 <a href="sdk-for-android-navigate-truckclass#LIGHT_CLASS"><code>TruckClass.LIGHT_CLASS</code></a> is not accepted in the filter.
 Otherwise will result in <a href="sdk-for-android-navigate-searcherror#INVALID_TRUCK_CLASS"><code>SearchError.INVALID_TRUCK_CLASS</code></a>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="ev">
<h3>ev</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-placefilter-ev" title="class in com.here.sdk.search">PlaceFilter.Ev</a></span> <span className="element-name">ev</span></div>
<div className="block"><p>Constraints that are applicable on the places of category EV station.</p></div>
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
<h3>PlaceFilter</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PlaceFilter</span>()</div>
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

---
title: "AddressQuery (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-addressquery"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AddressQuery.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.AddressQuery</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AddressQuery</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The options to specify an address query. A <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery#query"><code>query</code></a> can consist of parts of an address or full addresses,
 optionally comma separated. <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search"><code>AddressQuery</code></a> should only be used to search for parts of the address,
 excluding the POI name. For example, "Invalidenstraße 116, Berlin, Germany" is appropriate, whereas
 "HERE, Invalidenstraße 116, Berlin, Germany" is not. To be able to include the POI name, use
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search"><code>TextQuery</code></a> instead. <a href="sdk-for-android-navigate-searchoptions#languageCode"><code>SearchOptions.languageCode</code></a> specifies the language of the
 <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery#query"><code>query</code></a> and determines the preferred language of the results.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#areaCenter">areaCenter</a></code></div>
<div className="col-last even-row-color">
<div className="block">Geographical coordinates of the center around which to provide the most relevant places.</div>
</div>
<div className="col-first odd-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#countries">countries</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A list of countries that the query is applied in.</div>
</div>
<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#query">query</a></code></div>
<div className="col-last even-row-color">
<div className="block">Desired address query to search.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#%3Cinit%3E(java.lang.String)">AddressQuery</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an AddressQuery from the provided text query.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#%3Cinit%3E(java.lang.String,com.here.sdk.core.GeoCoordinates)">AddressQuery</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs an AddressQuery from the provided text query and geographical coordinates.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-addressquery#%3Cinit%3E(java.lang.String,com.here.sdk.core.GeoCoordinates,java.util.List)">AddressQuery</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt; countries)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an AddressQuery from the provided text query, geographical coordinates and the
 list of countries the query is applied in.</div>
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
<section className="detail" id="query">
<h3>query</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">query</span></div>
<div className="block"><p>Desired address query to search.</p></div>
</section>
</li>
<li>
<section className="detail" id="areaCenter">
<h3>areaCenter</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">areaCenter</span></div>
<div className="block"><p>Geographical coordinates of the center around which to provide the most relevant places.
 For Offline Search null value will result in <a href="sdk-for-android-navigate-searcherror#INVALID_AREA"><code>SearchError.INVALID_AREA</code></a></p></div>
</section>
</li>
<li>
<section className="detail" id="countries">
<h3>countries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</span> <span className="element-name">countries</span></div>
<div className="block"><p>A list of countries that the query is applied in.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></div>
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
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.core.GeoCoordinates)">
<h3>AddressQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AddressQuery</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div className="block"><p>Constructs an AddressQuery from the provided text query and geographical coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired query to search.</p></dd>
<dd><code>areaCenter</code> - <p>Geographical coordinates of the center around which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.core.GeoCoordinates,java.util.List)">
<h3>AddressQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AddressQuery</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt; countries)</span></div>
<div className="block"><p>Constructs an AddressQuery from the provided text query, geographical coordinates and the
 list of countries the query is applied in.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired query to search.</p></dd>
<dd><code>areaCenter</code> - <p>Geographical coordinates of the center around which to provide the most relevant places.</p></dd>
<dd><code>countries</code> - <p>A list of countries that the query is applied in.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String)">
<h3>AddressQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AddressQuery</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> query)</span></div>
<div className="block"><p>Constructs an AddressQuery from the provided text query.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired query to search.</p></dd>
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

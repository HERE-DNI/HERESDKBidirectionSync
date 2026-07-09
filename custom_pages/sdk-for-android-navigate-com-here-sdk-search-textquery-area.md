---
title: "TextQuery.Area (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-textquery-area"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TextQuery.Area.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.TextQuery.Area</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TextQuery.Area</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Area to perform search on.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter">areaCenter</a></code></div>
<div className="col-last even-row-color">
<div className="block">Geographic coordinates of the center around which to provide the most relevant places.</div>
</div>
<div className="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#boxArea">boxArea</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Geographic rectangle area in which to provide the most relevant places.</div>
</div>
<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#circleArea">circleArea</a></code></div>
<div className="col-last even-row-color">
<div className="block">Geographic circle area in which to provide the most relevant places.</div>
</div>
<div className="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#corridorArea">corridorArea</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Geographic corridor area in which to provide the most relevant places.</div>
</div>
<div className="col-first even-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#countries">countries</a></code></div>
<div className="col-last even-row-color">
<div className="block">A list of countries that the query is applied in.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#%3Cinit%3E(com.here.sdk.core.GeoBox)">Area</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#%3Cinit%3E(com.here.sdk.core.GeoCircle)">Area</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">Area</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#%3Cinit%3E(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)">Area</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#%3Cinit%3E(java.util.List,com.here.sdk.core.GeoCoordinates)">Area</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt; countries,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
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
<section className="detail" id="areaCenter">
<h3>areaCenter</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">areaCenter</span></div>
<div className="block"><p>Geographic coordinates of the center around which to provide the most relevant places.
 For Offline Search, one of <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter"><code>areaCenter</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#boxArea"><code>boxArea</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#circleArea"><code>circleArea</code></a> has to be set,
 otherwise it will result in <a href="sdk-for-android-navigate-searcherror#INVALID_AREA"><code>SearchError.INVALID_AREA</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="boxArea">
<h3>boxArea</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">boxArea</span></div>
<div className="block"><p>Geographic rectangle area in which to provide the most relevant places.
 For Offline Search, one of <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter"><code>areaCenter</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#boxArea"><code>boxArea</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#circleArea"><code>circleArea</code></a> has to be set,
 otherwise it will result in <a href="sdk-for-android-navigate-searcherror#INVALID_AREA"><code>SearchError.INVALID_AREA</code></a>.
 Also, for Offline Search, search in a given <code>GeoBox</code> restricts the results to only POIs.</p></div>
</section>
</li>
<li>
<section className="detail" id="circleArea">
<h3>circleArea</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a></span> <span className="element-name">circleArea</span></div>
<div className="block"><p>Geographic circle area in which to provide the most relevant places.
 For Offline Search, one of <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter"><code>areaCenter</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#boxArea"><code>boxArea</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#circleArea"><code>circleArea</code></a> has to be set,
 otherwise it will result in <a href="sdk-for-android-navigate-searcherror#INVALID_AREA"><code>SearchError.INVALID_AREA</code></a>.
 Also, for Offline Search, search in a given <code>GeoCircle</code> restricts the results to only POIs.</p></div>
</section>
</li>
<li>
<section className="detail" id="corridorArea">
<h3>corridorArea</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></span> <span className="element-name">corridorArea</span></div>
<div className="block"><p>Geographic corridor area in which to provide the most relevant places.
 The contained polyline and half-width define the area that will be used in a search query.
 When used with SearchEngine, the polyline is compressed and sent.
 More complex polylines with large amounts of coordinates and with smaller
 half-width may have the less relevant part removed, such as the one far away from the
 search center. This usually makes no difference, because there will be enough POIs near
 the search center. For use cases where it is important to search the entire polyline,
 half-width can be increased or not set.
 For example: Route between New York and Chicago with half-width 800 will be added to request
 without removing the far away part, but route of the same length (around 360km) between
 Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.
 When <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#corridorArea"><code>corridorArea</code></a> is provided,
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter"><code>areaCenter</code></a> has to be within it, otherwise
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area#areaCenter"><code>areaCenter</code></a> is ignored when searching.
 For Offline Search, search in a given <code>GeoCorridor</code> restricts the results to only POIs.</p></div>
</section>
</li>
<li>
<section className="detail" id="countries">
<h3>countries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</span> <span className="element-name">countries</span></div>
<div className="block"><p>A list of countries that the query is applied in.
 Not supported in <code>OfflineSearchEngine</code> (which is only available for the Navigate license).</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>Area</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Area</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the center around which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoBox)">
<h3>Area</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Area</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.
 For Offline Search, search in a given <code>GeoBox</code> restricts the results to only POIs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>boxArea</code> - <p>Geographic rectangle area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCircle)">
<h3>Area</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Area</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.
 For Offline Search, search in a given <code>GeoCircle</code> restricts the results to only POIs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>circleArea</code> - <p>Geographic circle area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)">
<h3>Area</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Area</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.
 The given corridor and center define the area that will be used in the search query.
 When used with SearchEngine, the polyline is compressed and sent.
 More complex polylines with large amounts of coordinates and with smaller
 half-width may have the less relevant part removed, such as the one far away from the
 search center. This usually makes no difference, because there will be enough POIs near
 the search center. For use cases where it is important to search the entire polyline,
 half-width can be increased or not set.
 For example: Route between New York and Chicago with half-width 800 will be added to request
 without removing the far away part, but route of the same length (around 360km) between
 Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.
 The area center has to be within the corridor, otherwise it is ignored.
 For Offline Search, search in a given <code>GeoCorridor</code> restricts the results to only POIs.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>corridorArea</code> - <p>Geographic corridor area in which to provide the most relevant places.</p></dd>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the prioritized area center.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,com.here.sdk.core.GeoCoordinates)">
<h3>Area</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Area</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt; countries,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.
 The given list of countries and center define the area that will be used in the search query.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>countries</code> - <p>A list of countries that the query is applied in.</p></dd>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the prioritized area center.</p></dd>
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

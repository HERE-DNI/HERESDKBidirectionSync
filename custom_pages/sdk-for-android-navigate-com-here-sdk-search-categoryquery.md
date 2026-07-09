---
title: "CategoryQuery (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-categoryquery"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CategoryQuery.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.CategoryQuery</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CategoryQuery</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The options to specify a query by categories.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a></code></div>
<div className="col-last even-row-color">
<div className="block">Area to perform search on.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#area">area</a></code></div>
<div className="col-last even-row-color">
<div className="block">Area in which to provide the most relevant places.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#categories">categories</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of categories to be included.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#excludeCategories">excludeCategories</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of categories and subcategories to be excluded.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#excludeChains">excludeChains</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of chains to be excluded.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#excludeFoodTypes">excludeFoodTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of food types to be excluded.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#filter">filter</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Full-text filter on POI names/titles.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#includeChains">includeChains</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of chains to be included.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#includeFoodTypes">includeFoodTypes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of food types to be included.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-placefilter" title="class in com.here.sdk.search">PlaceFilter</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#placeFilter">placeFilter</a></code></div>
<div className="col-last even-row-color">
<div className="block">The filter options to specify a place in query.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#%3Cinit%3E(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category,
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#%3Cinit%3E(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#%3Cinit%3E(java.util.List,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-categoryquery#%3Cinit%3E(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div className="col-last odd-row-color">
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
<section className="detail" id="categories">
<h3>categories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span className="element-name">categories</span></div>
<div className="block"><p>List of categories to be included.
 A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.categories</code>,
 but none are in <code>CategoryQuery.excludeCategories</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section className="detail" id="excludeCategories">
<h3>excludeCategories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span className="element-name">excludeCategories</span></div>
<div className="block"><p>List of categories and subcategories to be excluded.
 A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.excludeCategories</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 categories have been included in <code>CategoryQuery.categories</code>.
 In short, an exclusion will always win over an inclusion.
 This is especially useful for excluding specific subcategories from the main category.</p></div>
</section>
</li>
<li>
<section className="detail" id="includeChains">
<h3>includeChains</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>&gt;</span> <span className="element-name">includeChains</span></div>
<div className="block"><p>List of chains to be included.
 A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.includeChains</code>,
 but none are in <code>CategoryQuery.excludeChains</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section className="detail" id="excludeChains">
<h3>excludeChains</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>&gt;</span> <span className="element-name">excludeChains</span></div>
<div className="block"><p>List of chains to be excluded.
 A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.excludeChains</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 chains have been included in <code>CategoryQuery.includeChains</code>.
 In short, an exclusion will always win over an inclusion.</p></div>
</section>
</li>
<li>
<section className="detail" id="includeFoodTypes">
<h3>includeFoodTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span className="element-name">includeFoodTypes</span></div>
<div className="block"><p>List of food types to be included.
 A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.includeFoodTypes</code>,
 but none are in <code>CategoryQuery.excludeFoodTypes</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section className="detail" id="excludeFoodTypes">
<h3>excludeFoodTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span className="element-name">excludeFoodTypes</span></div>
<div className="block"><p>List of food types to be excluded.
 A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.excludeFoodTypes</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 food types have been included in <code>CategoryQuery.includeFoodTypes</code>.
 In short, an exclusion will always win over an inclusion.</p></div>
</section>
</li>
<li>
<section className="detail" id="filter">
<h3>filter</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">filter</span></div>
<div className="block"><p>Full-text filter on POI names/titles.
 Results with a partial match are included in the response.
 By default the value is set to null
 and results will be based on other parameters provided.</p></div>
</section>
</li>
<li>
<section className="detail" id="placeFilter">
<h3>placeFilter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-placefilter" title="class in com.here.sdk.search">PlaceFilter</a></span> <span className="element-name">placeFilter</span></div>
<div className="block"><p>The filter options to specify a place in query.
 Consists of fuel and truck options.</p></div>
</section>
</li>
<li>
<section className="detail" id="area">
<h3>area</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a></span> <span className="element-name">area</span></div>
<div className="block"><p>Area in which to provide the most relevant places.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CategoryQuery</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>Category for query</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CategoryQuery</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>categories</code> - <p>List of categories.</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CategoryQuery</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>Category for query</p></dd>
<dd><code>filter</code> - <p>Full-text filter on POI names/titles.
     Results with a partial match are included in the response.</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CategoryQuery</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div className="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>categories</code> - <p>List of categories.</p></dd>
<dd><code>filter</code> - <p>Full-text filter on POI names/titles.
     Results with a partial match are included in the response.</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
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

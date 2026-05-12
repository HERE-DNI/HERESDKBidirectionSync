---
title: "CategoryQuery (API Reference)"
slug: "sdk-for-android-explore-categoryquery"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CategoryQuery.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.search.CategoryQuery</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">CategoryQuery</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The options to specify a query by categories.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a></code></div>
<div class="col-last even-row-color">
<div class="block">Area to perform search on.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#area">area</a></code></div>
<div class="col-last even-row-color">
<div class="block">Area in which to provide the most relevant places.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#categories">categories</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of categories to be included.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#excludeCategories">excludeCategories</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of categories and subcategories to be excluded.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceChain.html" title="class in com.here.sdk.search">PlaceChain</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#excludeChains">excludeChains</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of chains to be excluded.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceFoodType.html" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#excludeFoodTypes">excludeFoodTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of food types to be excluded.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#filter">filter</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Full-text filter on POI names/titles.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceChain.html" title="class in com.here.sdk.search">PlaceChain</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#includeChains">includeChains</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of chains to be included.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceFoodType.html" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#includeFoodTypes">includeFoodTypes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of food types to be included.</div>
</div>
<div class="col-first even-row-color"><code><a href="PlaceFilter.html" title="class in com.here.sdk.search">PlaceFilter</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#placeFilter">placeFilter</a></code></div>
<div class="col-last even-row-color">
<div class="block">The filter options to specify a place in query.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a> category,
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.List,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">CategoryQuery</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="categories">
<h3>categories</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span class="element-name">categories</span></div>
<div class="block"><p>List of categories to be included.
 A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.categories</code>,
 but none are in <code>CategoryQuery.excludeCategories</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section class="detail" id="excludeCategories">
<h3>excludeCategories</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span class="element-name">excludeCategories</span></div>
<div class="block"><p>List of categories and subcategories to be excluded.
 A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.excludeCategories</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 categories have been included in <code>CategoryQuery.categories</code>.
 In short, an exclusion will always win over an inclusion.
 This is especially useful for excluding specific subcategories from the main category.</p></div>
</section>
</li>
<li>
<section class="detail" id="includeChains">
<h3>includeChains</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceChain.html" title="class in com.here.sdk.search">PlaceChain</a>&gt;</span> <span class="element-name">includeChains</span></div>
<div class="block"><p>List of chains to be included.
 A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.includeChains</code>,
 but none are in <code>CategoryQuery.excludeChains</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section class="detail" id="excludeChains">
<h3>excludeChains</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceChain.html" title="class in com.here.sdk.search">PlaceChain</a>&gt;</span> <span class="element-name">excludeChains</span></div>
<div class="block"><p>List of chains to be excluded.
 A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.excludeChains</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 chains have been included in <code>CategoryQuery.includeChains</code>.
 In short, an exclusion will always win over an inclusion.</p></div>
</section>
</li>
<li>
<section class="detail" id="includeFoodTypes">
<h3>includeFoodTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceFoodType.html" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span class="element-name">includeFoodTypes</span></div>
<div class="block"><p>List of food types to be included.
 A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.includeFoodTypes</code>,
 but none are in <code>CategoryQuery.excludeFoodTypes</code>, that place will be included in the response.</p></div>
</section>
</li>
<li>
<section class="detail" id="excludeFoodTypes">
<h3>excludeFoodTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceFoodType.html" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span class="element-name">excludeFoodTypes</span></div>
<div class="block"><p>List of food types to be excluded.
 A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.excludeFoodTypes</code>,
 that place will not be included in the response, regardless of whether any of its assigned
 food types have been included in <code>CategoryQuery.includeFoodTypes</code>.
 In short, an exclusion will always win over an inclusion.</p></div>
</section>
</li>
<li>
<section class="detail" id="filter">
<h3>filter</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">filter</span></div>
<div class="block"><p>Full-text filter on POI names/titles.
 Results with a partial match are included in the response.
 By default the value is set to null
 and results will be based on other parameters provided.</p></div>
</section>
</li>
<li>
<section class="detail" id="placeFilter">
<h3>placeFilter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PlaceFilter.html" title="class in com.here.sdk.search">PlaceFilter</a></span> <span class="element-name">placeFilter</span></div>
<div class="block"><p>The filter options to specify a place in query.
 Consists of fuel and truck options.</p></div>
</section>
</li>
<li>
<section class="detail" id="area">
<h3>area</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a></span> <span class="element-name">area</span></div>
<div class="block"><p>Area in which to provide the most relevant places.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr/><span class="parameters">(@NonNull
 <a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a> category,
 @NonNull
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>Category for query</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>categories</code> - <p>List of categories.</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr/><span class="parameters">(@NonNull
 <a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a> category,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>Category for query</p></dd>
<dd><code>filter</code> - <p>Full-text filter on POI names/titles.
     Results with a partial match are included in the response.</p></dd>
<dd><code>area</code> - <p>Area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)">
<h3>CategoryQuery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="CategoryQuery.Area.html" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

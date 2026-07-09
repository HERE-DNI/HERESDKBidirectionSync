---
title: "SearchInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-searchinterface"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SearchInterface.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchengine" title="class in com.here.sdk.search">OfflineSearchEngine</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-search-searchengine" title="class in com.here.sdk.search">SearchEngine</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">SearchInterface</span></div>
<div className="block"><p>Provides the interface for the online and offline
 search engines.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByText</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous text query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="sdk-for-android-navigate-com-here-sdk-search-textquery-area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.
 The returned places are sorted by relevance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByAddress</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByAddress</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous address query search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 This is the same type of search as forward geocoding, except that more data is returned
 than just the geographic coordinates of a given address. Note that an address can
 belong to more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> result, although all found places will
 share the same geographic coordinates.
 The returned places are sorted by relevance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired free-form address query text to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCategory</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByCategory</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous category search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 A list containing at least one <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search"><code>PlaceCategory</code></a> must be provided
 as part of the <code>query</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Query with list of desired categories.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous search for <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.
 This is the same search type as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search"><code>Address</code></a> related to the given coordinates.
 Note that more than one <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> can be related to the given coordinates.
 The returned places are sorted by relevance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates where to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPlaceId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByPlaceId</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>The id of place to search.</p></dd>
<dd><code>languageCode</code> - <p>The preferred language for the search results. When unset or unsupported language is chosen,
     results will be returned in their local language.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPickedPlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">searchByPickedPlace</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.
 If <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a> data is obtained from the offline map, it may happen that the newer version
 that is used by the online service represented by <code>SearchEngine</code> no longer contains the
 related POI. In that case, <a href="sdk-for-android-navigate-searcherror#NO_RESULTS_FOUND"><code>SearchError.NO_RESULTS_FOUND</code></a> error is reported.
 When that happens, you may try to obtain the POI from the offline map by calling
 <code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>pickedPlace</code> - <p>The content picked from map.</p></dd>
<dd><code>languageCode</code> - <p>The preferred language for the search result. When unset or unsupported language is chosen,
     result will be returned in the local language.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">
<h3>suggestByText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">suggestByText</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span></div>
<div className="block"><p>Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.
 Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
 <code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
 Complete details can be obtained by searching with <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>query</code> - <p>Desired text query to search.</p></dd>
<dd><code>options</code> - <p>Search options.</p></dd>
<dd><code>callback</code> - <p>Callback which receives the result on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
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

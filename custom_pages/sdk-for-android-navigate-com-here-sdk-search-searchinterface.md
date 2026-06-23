---
title: "SearchInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-searchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SearchInterface.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-offlinesearchengine" title="class in com.here.sdk.search">OfflineSearchEngine</a></code>, <code><a href="sdk-for-android-navigate-searchengine" title="class in com.here.sdk.search">SearchEngine</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">SearchInterface</span></div>
<div class="block"><p>Provides the interface for the online and offline
 search engines.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByAddress</a><wbr/>(<a href="sdk-for-android-navigate-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous address query search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCategory</a><wbr/>(<a href="sdk-for-android-navigate-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous category search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPickedPlace</a><wbr/>(<a href="sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous search for a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">searchByPlaceId</a><wbr/>(<a href="sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 <a href="sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous search for a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">searchByText</a><wbr/>(<a href="sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous text query search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="sdk-for-android-navigate-textquery.area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">suggestByText</a><wbr/>(<a href="sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 <a href="sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous text query search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances within a given <a href="sdk-for-android-navigate-textquery.area" title="class in com.here.sdk.search"><code>TextQuery.Area</code></a>.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
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
<section class="detail" id="searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByAddress</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByAddress</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous address query search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 This is the same type of search as forward geocoding, except that more data is returned
 than just the geographic coordinates of a given address. Note that an address can
 belong to more than one <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> result, although all found places will
 share the same geographic coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
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
<section class="detail" id="searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCategory</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCategory</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous category search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances.
 A list containing at least one <a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search"><code>PlaceCategory</code></a> must be provided
 as part of the <code>query</code>.</p></div>
<dl class="notes">
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
<section class="detail" id="searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)">
<h3>searchByCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> instances based on the given
 geographic coordinates.
 This is the same search type as reverse geocoding, except that more data is returned
 than just the <a href="sdk-for-android-navigate-address" title="class in com.here.sdk.search"><code>Address</code></a> related to the given coordinates.
 Note that more than one <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> can be related to the given coordinates.
 The returned places are sorted by relevance.</p></div>
<dl class="notes">
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
<section class="detail" id="searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPlaceId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPlaceId</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query,
 @Nullable
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on its ID and
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>.</p></div>
<dl class="notes">
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
<section class="detail" id="searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)">
<h3>searchByPickedPlace</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPickedPlace</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace,
 @Nullable
 <a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode,
 @NonNull
 <a href="sdk-for-android-navigate-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous search for a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> based on the content found in <a href="sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a>.
 If <a href="sdk-for-android-navigate-pickedplace" title="class in com.here.sdk.core"><code>PickedPlace</code></a> data is obtained from the offline map, it may happen that the newer version
 that is used by the online service represented by <code>SearchEngine</code> no longer contains the
 related POI. In that case, <a href="sdk-for-android-navigate-searcherror#NO_RESULTS_FOUND"><code>SearchError.NO_RESULTS_FOUND</code></a> error is reported.
 When that happens, you may try to obtain the POI from the offline map by calling
 <code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div>
<dl class="notes">
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
<section class="detail" id="suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)">
<h3>suggestByText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggestByText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-textquery" title="class in com.here.sdk.search">TextQuery</a> query,
 @NonNull
 <a href="sdk-for-android-navigate-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span></div>
<div class="block"><p>Performs an asynchronous request to suggest places for text queries and
 returns suggestions sorted by relevance.
 </p><p>Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
 <code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
 Complete details can be obtained by searching with <a href="sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>

---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/SearchEngine///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/SearchEngine</div>
<div class="cover">
<h1 class="cover">Search<wbr/>Engine</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface</div><p class="paragraph">The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications. It enables to search for HERE points of interests, forward and reverse geocode addresses and geographic coordinates from the HERE map and search for suggested addresses or place candidates based on incomplete or misspelled queries.</p><p class="paragraph">It also allows to search along a given /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-polyline set inside a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor as part of a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query.</p><p class="paragraph">The SearchEngine API requires an online connection to execute the requests.</p><p class="paragraph"><strong>Note:</strong> All methods are provided in two flavors. One uses a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback and the other uses a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended: The later adds a <code class="lang-kotlin">ResponseDetails</code> result type that provides the <code class="lang-kotlin">requestId</code> of a search request and a <code class="lang-kotlin">correlationId</code> to identify multiple, related queries. This may be useful for debug purposes.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="SearchEngine" data-filterable-set=":modules:dokkaHtml/release" data-name="-1670208669%2FConstructors%2F1617540583" id="-1670208669%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-engine</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace">constructor(sdkEngine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine)</div><div class="brief"><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-349511385%2FClasslikes%2F1617540583" id="-349511385%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="search" data-filterable-set=":modules:dokkaHtml/release" data-name="-338114179%2FFunctions%2F1617540583" id="-338114179%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(circle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(circle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-circle, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to search for places based on given circular spatial filter. This is the same process as reverse geocoding, except that more data is returned than just the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address that belongs to given coordinates. Note that coordinates can belong to more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place result. Provides candidate places sorted by relevance and located inside the radius of filter.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to search for places based on given geographic coordinates. This is the same process as reverse geocoding, except that more data is returned than just the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address that belongs to given coordinates. Note that coordinates can belong to more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place result. Provides candidate places sorted by relevance.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to search for places based on a given address. This is the same process as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place result, although all found places will share the same geographic coordinates. Provides candidate places sorted by relevance.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to do a category search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. A list containing at least one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-category must be provided as part of the com.here.sdk.search.SearchEngine.search.query.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-query, languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code?, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to search for a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place based on its ID and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to do a text query search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. Optionally, search along a polyline, such as a route, by specifying a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-corridor. Provides candidate places sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByAddress" data-filterable-set=":modules:dokkaHtml/release" data-name="789273805%2FFunctions%2F1617540583" id="789273805%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-address</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-address(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous address query search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByCategory" data-filterable-set=":modules:dokkaHtml/release" data-name="1100759367%2FFunctions%2F1617540583" id="1100759367%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-category</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-category(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-category-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous category search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances. A list containing at least one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-category must be provided as part of the com.here.sdk.search.SearchInterface.searchByCategory.query.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByCoordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="392752499%2FFunctions%2F1617540583" id="392752499%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-coordinates(coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-address related to the given coordinates. Note that more than one /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place can be related to the given coordinates. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByPickedPlace" data-filterable-set=":modules:dokkaHtml/release" data-name="564167413%2FFunctions%2F1617540583" id="564167413%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-picked-place</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-picked-place(pickedPlace: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place, languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code?, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place based on the content found in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-picked-place data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <code class="lang-kotlin">SearchEngine</code> no longer contains the related POI. In that case, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error-n-o-r-e-s-u-l-t-s-f-o-u-n-d error is reported. When that happens, you may try to obtain the POI from the offline map by calling <code class="lang-kotlin">OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByPlaceId" data-filterable-set=":modules:dokkaHtml/release" data-name="-2083382274%2FFunctions%2F1617540583" id="-2083382274%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-place-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-place-id(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-query, languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code?, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-id-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous search for a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place based on its ID and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="searchByText" data-filterable-set=":modules:dokkaHtml/release" data-name="629253609%2FFunctions%2F1617540583" id="629253609%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-search-by-text(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous text query search for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place instances within a given /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query-area. The returned places are sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="sendRequest" data-filterable-set=":modules:dokkaHtml/release" data-name="-926256173%2FFunctions%2F1617540583" id="-926256173%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-send-request</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-send-request(href: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-send-request(href: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request by using the given href. The href value can be obtained from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggestion objects, which are the result of successful call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-suggest. Currently supports only /v1/discover path. Provides candidate places sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setCustomOption" data-filterable-set=":modules:dokkaHtml/release" data-name="-1085321711%2FFunctions%2F1617540583" id="-1085321711%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-custom-option</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-custom-option(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-error?</div><div class="brief"><p class="paragraph">Sets a custom option for search backend queries. This allows more control over the behavior of the search algorithm. Name has the format <endpoint_name>.<option_name>, for example "discover.show". Values can be combined for the same name by using a comma, for example "truck,fuel". The custom option is applied only for the endpoint that is specified as prefix in <code class="lang-kotlin">name</code>. Some of the supported name/value options are:</option_name></endpoint_name></p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setEVInterface" data-filterable-set=":modules:dokkaHtml/release" data-name="-739463985%2FFunctions%2F1617540583" id="-739463985%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-e-v-interface</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-set-e-v-interface(evcpInterface: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-search-interface)</div><div class="brief"><p class="paragraph">Sets the EV interface through which search will interact with EVCP3. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="suggest" data-filterable-set=":modules:dokkaHtml/release" data-name="686877340%2FFunctions%2F1617540583" id="686877340%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-suggest</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-suggest(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggest-callback-extended): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to suggest places for text queries and returns candidate suggestions sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="suggestByText" data-filterable-set=":modules:dokkaHtml/release" data-name="-158036071%2FFunctions%2F1617540583" id="-158036071%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-suggest-by-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open external override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-engine-suggest-by-text(query: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-text-query, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-suggest-callback): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>

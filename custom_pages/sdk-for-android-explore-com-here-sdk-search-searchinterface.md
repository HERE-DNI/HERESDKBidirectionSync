---
title: "SearchInterface (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-searchinterface"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Known Implementing Classes:  
[`SearchEngine`](sdk-for-android-explore-com-here-sdk-search-searchengine "class in com.here.sdk.search")

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">SearchInterface</span>

</div>

<div class="block">

Provides the interface for the online and offline search engines.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByAddress ( AddressQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous address query search for Place instances.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByCategory ( CategoryQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous category search for Place instances.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByCoordinates ( GeoCoordinates coordinates, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous search for Place instances based on the given geographic coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByPickedPlace ( PickedPlace pickedPlace, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous search for a Place based on the content found in PickedPlace .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByPlaceId ( PlaceIdQuery query, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous search for a Place based on its ID and LanguageCode .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      searchByText ( TextQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous text query search for Place instances within a given TextQuery.Area .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      suggestByText ( TextQuery query, SearchOptions options, SuggestCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-searchByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByText

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByText</span><wbr></wbr><span class="parameters">(@NonNull [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous text query search for Place instances within a given TextQuery.Area . The returned places are sorted by relevance.

    </div>

    Parameters:  
    `query` -

    Desired free-form text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByAddress-com-here-sdk-search-AddressQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByAddress

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByAddress</span><wbr></wbr><span class="parameters">(@NonNull [AddressQuery](sdk-for-android-explore-com-here-sdk-search-addressquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous address query search for Place instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one Place result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.

    </div>

    Parameters:  
    `query` -

    Desired free-form address query text to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByCategory-com-here-sdk-search-CategoryQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByCategory

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByCategory</span><wbr></wbr><span class="parameters">(@NonNull [CategoryQuery](sdk-for-android-explore-com-here-sdk-search-categoryquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous category search for Place instances. A list containing at least one PlaceCategory must be provided as part of the query .

    </div>

    Parameters:  
    `query` -

    Query with list of desired categories.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByCoordinates-com-here-sdk-core-GeoCoordinates-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByCoordinates</span><wbr></wbr><span class="parameters">(@NonNull [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates, @NonNull [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for Place instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the Address related to the given coordinates. Note that more than one Place can be related to the given coordinates. The returned places are sorted by relevance.

    </div>

    Parameters:  
    `coordinates` -

    The coordinates where to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByPlaceId-com-here-sdk-search-PlaceIdQuery-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback" class="section detail">

    ### searchByPlaceId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByPlaceId</span><wbr></wbr><span class="parameters">(@NonNull [PlaceIdQuery](sdk-for-android-explore-com-here-sdk-search-placeidquery "class in com.here.sdk.search") query, @Nullable [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-com-here-sdk-search-placeidsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on its ID and LanguageCode .

    </div>

    Parameters:  
    `query` -

    The id of place to search.

    `languageCode` -

    The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByPickedPlace-com-here-sdk-core-PickedPlace-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback" class="section detail">

    ### searchByPickedPlace

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByPickedPlace</span><wbr></wbr><span class="parameters">(@NonNull [PickedPlace](sdk-for-android-explore-com-here-sdk-core-pickedplace "class in com.here.sdk.core") pickedPlace, @Nullable [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-com-here-sdk-search-placeidsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on the content found in PickedPlace . If PickedPlace data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by SearchEngine no longer contains the related POI. In that case, SearchError.NO_RESULTS_FOUND error is reported. When that happens, you may try to obtain the POI from the offline map by calling OfflineSearchEngine.searchByPickedPlace , only available for the Navigate license.

    </div>

    Parameters:  
    `pickedPlace` -

    The content picked from map.

    `languageCode` -

    The preferred language for the search result. When unset or unsupported language is chosen, result will be returned in the local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-suggestByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SuggestCallback" class="section detail">

    ### suggestByText

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">suggestByText</span><wbr></wbr><span class="parameters">(@NonNull [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options, @NonNull [SuggestCallback](sdk-for-android-explore-com-here-sdk-search-suggestcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance. Note that while OfflineSearchEngine includes as many details as are available, SearchEngine includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with PlaceIdQuery .

    </div>

    Parameters:  
    `query` -

    Desired text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


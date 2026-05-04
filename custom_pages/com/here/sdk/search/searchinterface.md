---
title: "SearchInterface (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsearchinterface"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface SearchInterface

All Known Implementing Classes:
[`SearchEngine`](sdk-for-android-explore-api-reference-latestsearchengine "class in com.here.sdk.search")

------------------------------------------------------------------------
public interface SearchInterface
Provides the interface for the online and offline search engines.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByAddress](#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback))`(`[`AddressQuery`](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous address query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByCategory](#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback))`(`[`CategoryQuery`](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous category search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByCoordinates](#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances based on the given geographic coordinates.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByPickedPlace](#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback))`(`[`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core")` pickedPlace, `[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")` languageCode, `[`PlaceIdSearchCallback`](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on the content found in [`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByPlaceId](#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback))`(`[`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search")` query, `[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")` languageCode, `[`PlaceIdSearchCallback`](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on its ID and [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [searchByText](#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback))`(`[`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous text query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances within a given [`TextQuery.Area`](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [suggestByText](#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback))`(`[`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SuggestCallback`](sdk-for-android-explore-api-reference-latestsuggestcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

## Method Details

### searchByText

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByText(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous text query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances within a given [`TextQuery.Area`](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search"). The returned places are sorted by relevance.
Parameters:
    `query` -

    Desired free-form text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### searchByAddress

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByAddress(@NonNull [AddressQuery](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous address query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.
Parameters:
    `query` -

    Desired free-form address query text to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### searchByCategory

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByCategory(@NonNull [CategoryQuery](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous category search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. A list containing at least one [`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search") must be provided as part of the `query`.
Parameters:
    `query` -

    Query with list of desired categories.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### searchByCoordinates

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") related to the given coordinates. Note that more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") can be related to the given coordinates. The returned places are sorted by relevance.
Parameters:
    `coordinates` -

    The coordinates where to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### searchByPlaceId

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByPlaceId(@NonNull [PlaceIdQuery](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search") query, @Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on its ID and [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core").
Parameters:
    `query` -

    The id of place to search.

    `languageCode` -

    The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### searchByPickedPlace

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByPickedPlace(@NonNull [PickedPlace](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core") pickedPlace, @Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on the content found in [`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core"). If [`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core") data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by `SearchEngine` no longer contains the related POI. In that case, [`SearchError.NO_RESULTS_FOUND`](sdk-for-android-explore-api-reference-latestsearcherror#NO_RESULTS_FOUND) error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.
Parameters:
    `pickedPlace` -

    The content picked from map.

    `languageCode` -

    The preferred language for the search result. When unset or unsupported language is chosen, result will be returned in the local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### suggestByText

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") suggestByText(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SuggestCallback](sdk-for-android-explore-api-reference-latestsuggestcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

    Note that while `OfflineSearchEngine` includes as many details as are available, `SearchEngine` includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with [`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search").
Parameters:
    `query` -

    Desired text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

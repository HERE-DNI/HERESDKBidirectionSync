---
title: "SearchEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsearchengine"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SearchEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.search.SearchEngine
All Implemented Interfaces:
[`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

------------------------------------------------------------------------
public final class SearchEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [SearchInterface](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")
The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications. It enables to search for HERE points of interests, forward and reverse geocode addresses and geographic coordinates from the HERE map and search for suggested addresses or place candidates based on incomplete or misspelled queries.

It also allows to search along a given [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") set inside a [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") as part of a [`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search").

The SearchEngine API requires an online connection to execute the requests.

**Note:** All methods are provided in two flavors. One uses a [`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") and the other uses a [`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search"): The later adds a `ResponseDetails` result type that provides the `requestId` of a search request and a `correlationId` to identify multiple, related queries. This may be useful for debug purposes.

## Constructor Summary

Constructors

Constructor

  Description

  [SearchEngine](#%3Cinit%3E())`()`

Creates a new instance of this class.

[SearchEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine)`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback))`(`[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` circle, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to search for places based on given circular spatial filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.core.GeoCircle,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended))`(`[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` circle, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to search for places based on given circular spatial filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to search for places based on given geographic coordinates.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended))`(`[`AddressQuery`](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to search for places based on a given address.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended))`(`[`CategoryQuery`](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to do a category search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallbackExtended))`(`[`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search")` query, `[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")` languageCode, `[`PlaceIdSearchCallbackExtended`](sdk-for-android-explore-api-reference-latestplaceidsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on its ID and [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [search](#search(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallbackExtended))`(`[`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to do a text query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances.

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

  [sendRequest](#sendRequest(java.lang.String,com.here.sdk.search.SearchCallback))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` href, `[`SearchCallback`](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request by using the given href.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [sendRequest](#sendRequest(java.lang.String,com.here.sdk.search.SearchCallbackExtended))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` href, `[`SearchCallbackExtended`](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request by using the given href.

[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")

  [setCustomOption](#setCustomOption(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Sets a custom option for search backend queries.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [suggest](#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended))`(`[`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SuggestCallbackExtended`](sdk-for-android-explore-api-reference-latestsuggestcallbackextended "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to suggest places for text queries and returns candidate suggestions sorted by relevance.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [suggestByText](#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback))`(`[`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")` query, `[`SearchOptions`](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")` options, `[`SuggestCallback`](sdk-for-android-explore-api-reference-latestsuggestcallback "interface in com.here.sdk.search")` callback)`

Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### SearchEngine

public SearchEngine() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine)" class="section detail">

### SearchEngine

public SearchEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Parameters:
    `sdkEngine` -

    Instance of an existing SDKEngine.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to do a text query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. Optionally, search along a polyline, such as a route, by specifying a [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core"). Provides candidate places sorted by relevance.
Parameters:
    `query` -

    Desired free-form text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [AddressQuery](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to search for places based on a given address. This is the same process as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result, although all found places will share the same geographic coordinates. Provides candidate places sorted by relevance.
Parameters:
    `query` -

    Desired free-form address query text to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [PlaceIdQuery](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search") query, @Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallbackExtended](sdk-for-android-explore-api-reference-latestplaceidsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on its ID and [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core").
Parameters:
    `query` -

    The id of place to search.

    `languageCode` -

    The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to search for places based on given geographic coordinates. This is the same process as reverse geocoding, except that more data is returned than just the [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") that belongs to given coordinates. Note that coordinates can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result. Provides candidate places sorted by relevance.
Parameters:
    `coordinates` -

    The coordinates where to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circle, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to search for places based on given circular spatial filter. This is the same process as reverse geocoding, except that more data is returned than just the [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") that belongs to given coordinates. Note that coordinates can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result. Provides candidate places sorted by relevance and located inside the radius of filter.
Parameters:
    `circle` -

    The coordinates where to search and radius of the circular spatial filter. Passed in form of [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core").

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circle, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to search for places based on given circular spatial filter. This is the same process as reverse geocoding, except that more data is returned than just the [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") that belongs to given coordinates. Note that coordinates can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result. Provides candidate places sorted by relevance and located inside the radius of filter.
Parameters:
    `circle` -

    The coordinates where to search and radius of the circular spatial filter. Passed in form of [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core").

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### sendRequest

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") sendRequest(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous request by using the given href. The href value can be obtained from [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") objects, which are the result of successful call to [`suggest(com.here.sdk.search.TextQuery, com.here.sdk.search.SearchOptions, com.here.sdk.search.SuggestCallbackExtended)`](#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)). Currently supports only /v1/discover path. Provides candidate places sorted by relevance.
Parameters:
    `href` -

    The direct link.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### sendRequest

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") sendRequest(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request by using the given href. The href value can be obtained from [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") objects, which are the result of successful call to [`suggest(com.here.sdk.search.TextQuery, com.here.sdk.search.SearchOptions, com.here.sdk.search.SuggestCallbackExtended)`](#suggest(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallbackExtended)). Currently supports only /v1/discover path. Provides candidate places sorted by relevance.
Parameters:
    `href` -

    The direct link.

    `callback` -

    Callback which receives result on the main thread.

    Returns:
    Handle that will be used to manipulate execution of the task.

### search

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") search(@NonNull [CategoryQuery](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to do a category search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. A list containing at least one [`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search") must be provided as part of the `query`.
Parameters:
    `query` -

    Query with list of desired categories.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### suggest

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") suggest(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SuggestCallbackExtended](sdk-for-android-explore-api-reference-latestsuggestcallbackextended "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to suggest places for text queries and returns candidate suggestions sorted by relevance.
Parameters:
    `query` -

    Desired text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### setCustomOption

@Nullable public [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") setCustomOption(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Sets a custom option for search backend queries. This allows more control over the behavior of the search algorithm. Name has the format \<endpoint_name\>.\<option_name\>, for example "discover.show". Values can be combined for the same name by using a comma, for example "truck,fuel". The custom option is applied only for the endpoint that is specified as prefix in `name`. Some of the supported name/value options are:

    - name = "revgeocode.with", value = "unnamedStreets" enables the retrieval of access points on unnamed streets.
    - name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "truck" enables retreival of truck amenities. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated in callbacks.
    - name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "fuel" enables retreival of fuel station details. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated in callbacks.
    - name = "lookup.show" or "discover.show" or "browse.show", value = "ev" enables retreival of EV charging station details.
    - name = "lookup.show" or "discover.show" or "browse.show", value = "eMobilityServiceProviders" enables retreival of e-Mobility Service Providers details.
    - name = "lookup.show" or "discover.show" or "browse.show", value = "tripadvisor" adds images, ratings, and editorials from Tripadvisor (TM). **Note:** Only clients with a license with TripAdvisor for rich content will actually get it. If this licence is missing, TripAdvisor rich content will be missing, with no error reported. This content is only added to top 10 search results. If more results are returned, they will be missing rich TripAdvisor content.
    - name = "lookup.datasets" or "discover.datasets" or "browse.datasets" or "autosuggest.datasets", value = \<your_dataset_hrn\> enables ingesting and searching of private POIs. **Note:** Only participants of the search customization can get access from HERE to use this feature, otherwise, a [`SearchError.INVALID_CUSTOM_OPTION_FORMAT`](sdk-for-android-explore-api-reference-latestsearcherror#INVALID_CUSTOM_OPTION_FORMAT) will be propagated in callbacks.
    - name = "discover.ranking" or "browse.ranking", value = "excursionDistance" enables balanced distribution of results for search in `GeoCorridor`. Constraint: using this parameter when searching an area that is not a `GeoCorridor` generates an error [`SearchError.BAD_REQUEST`](sdk-for-android-explore-api-reference-latestsearcherror#BAD_REQUEST). **Note:** It is recommended to use [`SearchOptions.distributedResults`](sdk-for-android-explore-api-reference-latestsearchoptions#distributedResults) instead. For a complete list of available endpoints, parameter names and their valid values, refer to [HERE Geocoding & Search API v7](https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html). **Note:** It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.
Parameters:
    `name` -

    Option name in the format \<endpoint_name\>.\<option_name\>, for example "discover.show".

    `value` -

    Option value.

    Returns:
    Error in case when setting the option fails.

### searchByText

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByText(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous text query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances within a given [`TextQuery.Area`](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search"). The returned places are sorted by relevance.
Specified by:
    [`searchByText`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByAddress(@NonNull [AddressQuery](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous address query search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.
Specified by:
    [`searchByAddress`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByCategory(@NonNull [CategoryQuery](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous category search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances. A list containing at least one [`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search") must be provided as part of the `query`.
Specified by:
    [`searchByCategory`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") related to the given coordinates. Note that more than one [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") can be related to the given coordinates. The returned places are sorted by relevance.
Specified by:
    [`searchByCoordinates`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByPlaceId(@NonNull [PlaceIdQuery](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search") query, @Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on its ID and [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core").
Specified by:
    [`searchByPlaceId`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") searchByPickedPlace(@NonNull [PickedPlace](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core") pickedPlace, @Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode, @NonNull [PlaceIdSearchCallback](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous search for a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") based on the content found in [`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core"). If [`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core") data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by `SearchEngine` no longer contains the related POI. In that case, [`SearchError.NO_RESULTS_FOUND`](sdk-for-android-explore-api-reference-latestsearcherror#NO_RESULTS_FOUND) error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.
Specified by:
    [`searchByPickedPlace`](sdk-for-android-explore-api-reference-latestsearchinterface#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") suggestByText(@NonNull [TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") query, @NonNull [SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search") options, @NonNull [SuggestCallback](sdk-for-android-explore-api-reference-latestsuggestcallback "interface in com.here.sdk.search") callback)

    Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

    Note that while `OfflineSearchEngine` includes as many details as are available, `SearchEngine` includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with [`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search").
Specified by:
    [`suggestByText`](sdk-for-android-explore-api-reference-latestsearchinterface#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)) in interface [`SearchInterface`](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")

    Parameters:
    `query` -

    Desired text query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

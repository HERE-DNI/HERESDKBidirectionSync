---
title: "SearchEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-searchengine"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.search.SearchEngine →
com.here.NativeBase com.here.sdk.search.SearchEngine →
com.here.sdk.search.SearchEngine

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
[`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SearchEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")
implements
[SearchInterface](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")</span>

</div>

<div class="block">

The SearchEngine API unlocks the search, geocoding and suggesting
capabilities of HERE services to provide developers with unmatched
flexibility to create differentiating location-enabled applications. It
enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and
search for suggested addresses or place candidates based on incomplete
or misspelled queries. It also allows to search along a given
GeoPolyline set inside a GeoCorridor as part of a TextQuery . The
SearchEngine API requires an online connection to execute the requests.
Note: All methods are provided in two flavors. One uses a SearchCallback
and the other uses a SearchCallbackExtended : The later adds a
ResponseDetails result type that provides the requestId of a search
request and a correlationId to identify multiple, related queries. This
may be useful for debug purposes.

</div>

</div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      SearchEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SearchEngine ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( GeoCircle circle, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for places based on given
  circular spatial filter.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( GeoCircle circle, SearchOptions options, SearchCallbackExtended callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for places based on given
  circular spatial filter.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( GeoCoordinates coordinates, SearchOptions options, SearchCallbackExtended callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for places based on given
  geographic coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( AddressQuery query, SearchOptions options, SearchCallbackExtended callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for places based on a given
  address.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( CategoryQuery query, SearchOptions options, SearchCallbackExtended callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to do a category search for Place
  instances.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( PlaceIdQuery query, LanguageCode languageCode, PlaceIdSearchCallbackExtended callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for a Place based on its ID
  and LanguageCode .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( TextQuery query, SearchOptions options, SearchCallbackExtended callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to do a text query search for Place
  instances.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByAddress ( AddressQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous address query search for Place instances.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByCategory ( CategoryQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous category search for Place instances.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByCoordinates ( GeoCoordinates coordinates, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for Place instances based on the given
  geographic coordinates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByPickedPlace ( PickedPlace pickedPlace, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for a Place based on the content found
  in PickedPlace .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByPlaceId ( PlaceIdQuery query, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for a Place based on its ID and
  LanguageCode .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByText ( TextQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous text query search for Place instances within
  a given TextQuery.Area .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      sendRequest ( String href, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request by using the given href.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      sendRequest ( String href, SearchCallbackExtended callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request by using the given href.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`SearchError`](sdk-for-android-explore-com-here-sdk-search-searcherror "enum class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomOption ( String name, String value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom option for search backend queries.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEVInterface ( EVSearchInterface evcpInterface)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the EV interface through which search will interact with EVCP3.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      suggest ( TextQuery query, SearchOptions options, SuggestCallbackExtended callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to suggest places for text queries
  and returns candidate suggestions sorted by relevance.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      suggestByText ( TextQuery query, SearchOptions options, SuggestCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to suggest places for text queries
  and returns suggestions sorted by relevance.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### SearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SearchEngine</span>()
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine"
    class="section detail">

    ### SearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SearchEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-search-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to do a text query search for Place
    instances. Optionally, search along a polyline, such as a route, by
    specifying a GeoCorridor . Provides candidate places sorted by
    relevance.

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

  - <div id="sdk-for-android-explore-search-com-here-sdk-search-AddressQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [AddressQuery](sdk-for-android-explore-com-here-sdk-search-addressquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for places based on a
    given address. This is the same process as forward geocoding, except
    that more data is returned than just the geographic coordinates of a
    given address. Note that an address can belong to more than one
    Place result, although all found places will share the same
    geographic coordinates. Provides candidate places sorted by
    relevance.

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

  - <div id="sdk-for-android-explore-search-com-here-sdk-search-PlaceIdQuery-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [PlaceIdQuery](sdk-for-android-explore-com-here-sdk-search-placeidquery "class in com.here.sdk.search") query,
    @Nullable
    [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode,
    @NonNull
    [PlaceIdSearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-placeidsearchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for a Place based on its
    ID and LanguageCode .

    </div>

    Parameters:  
    `query` -

    The id of place to search.

    `languageCode` -

    The preferred language for the search results. When unset or
    unsupported language is chosen, results will be returned in their
    local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-search-com-here-sdk-core-GeoCoordinates-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for places based on given
    geographic coordinates. This is the same process as reverse
    geocoding, except that more data is returned than just the Address
    that belongs to given coordinates. Note that coordinates can belong
    to more than one Place result. Provides candidate places sorted by
    relevance.

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

  - <div id="sdk-for-android-explore-search-com-here-sdk-core-GeoCircle-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") circle,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for places based on given
    circular spatial filter. This is the same process as reverse
    geocoding, except that more data is returned than just the Address
    that belongs to given coordinates. Note that coordinates can belong
    to more than one Place result. Provides candidate places sorted by
    relevance and located inside the radius of filter.

    </div>

    Parameters:  
    `circle` -

    The coordinates where to search and radius of the circular spatial
    filter. Passed in form of
    [`GeoCircle`](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core").

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-explore-search-com-here-sdk-core-GeoCircle-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") circle,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for places based on given
    circular spatial filter. This is the same process as reverse
    geocoding, except that more data is returned than just the Address
    that belongs to given coordinates. Note that coordinates can belong
    to more than one Place result. Provides candidate places sorted by
    relevance and located inside the radius of filter.

    </div>

    Parameters:  
    `circle` -

    The coordinates where to search and radius of the circular spatial
    filter. Passed in form of
    [`GeoCircle`](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core").

    `options` -

    Search options.

    `callback` -

    Callback which receives result on the main thread.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-explore-sendRequest-java-lang-String-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### sendRequest

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">sendRequest</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> href,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request by using the given href. The href
    value can be obtained from Suggestion objects, which are the result
    of successful call to suggest(com.here.sdk.search.TextQuery,
    com.here.sdk.search.SearchOptions,
    com.here.sdk.search.SuggestCallbackExtended) . Currently supports
    only /v1/discover path. Provides candidate places sorted by
    relevance.

    </div>

    Parameters:  
    `href` -

    The direct link.

    `callback` -

    Callback which receives result on the main thread.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-explore-sendRequest-java-lang-String-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### sendRequest

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">sendRequest</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> href,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request by using the given href. The href
    value can be obtained from Suggestion objects, which are the result
    of successful call to suggest(com.here.sdk.search.TextQuery,
    com.here.sdk.search.SearchOptions,
    com.here.sdk.search.SuggestCallbackExtended) . Currently supports
    only /v1/discover path. Provides candidate places sorted by
    relevance.

    </div>

    Parameters:  
    `href` -

    The direct link.

    `callback` -

    Callback which receives result on the main thread.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-explore-search-com-here-sdk-search-CategoryQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallbackExtended"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    [CategoryQuery](sdk-for-android-explore-com-here-sdk-search-categoryquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallbackExtended](sdk-for-android-explore-com-here-sdk-search-searchcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to do a category search for Place
    instances. A list containing at least one PlaceCategory must be
    provided as part of the query .

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

  - <div id="sdk-for-android-explore-suggest-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SuggestCallbackExtended"
    class="section detail">

    ### suggest

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">suggest</span><span class="parameters">(@NonNull
    [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SuggestCallbackExtended](sdk-for-android-explore-com-here-sdk-search-suggestcallbackextended "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to suggest places for text queries
    and returns candidate suggestions sorted by relevance.

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

  - <div id="sdk-for-android-explore-setCustomOption-java-lang-String-java-lang-String"
    class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[SearchError](sdk-for-android-explore-com-here-sdk-search-searcherror "enum class in com.here.sdk.search")</span> <span class="element-name">setCustomOption</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets a custom option for search backend queries. This allows more
    control over the behavior of the search algorithm. Name has the
    format \<endpoint_name\>.\<option_name\>, for example
    "discover.show". Values can be combined for the same name by using a
    comma, for example "truck,fuel". The custom option is applied only
    for the endpoint that is specified as prefix in name . Some of the
    supported name/value options are: name = "revgeocode.with", value =
    "unnamedStreets" enables the retrieval of access points on unnamed
    streets. name = "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show", value = "truck" enables
    retreival of truck amenities. Note: Only participants of the
    closed-alpha group can get access from HERE to use this feature,
    otherwise, a SearchError.FORBIDDEN will be propagated in callbacks.
    name = "lookup.show" or "discover.show" or "autosuggest.show" or
    "browse.show", value = "fuel" enables retreival of fuel station
    details. Note: Only participants of the closed-alpha group can get
    access from HERE to use this feature, otherwise, a
    SearchError.FORBIDDEN will be propagated in callbacks. name =
    "lookup.show" or "discover.show" or "browse.show", value = "ev"
    enables retreival of EV charging station details. name =
    "lookup.show" or "discover.show" or "browse.show", value =
    "eMobilityServiceProviders" enables retreival of e-Mobility Service
    Providers details. name = "lookup.show" or "discover.show" or
    "browse.show", value = "tripadvisor" adds images, ratings, and
    editorials from Tripadvisor (TM). Note: Only clients with a license
    with TripAdvisor for rich content will actually get it. If this
    licence is missing, TripAdvisor rich content will be missing, with
    no error reported. This content is only added to top 10 search
    results. If more results are returned, they will be missing rich
    TripAdvisor content. name = "lookup.datasets" or "discover.datasets"
    or "browse.datasets" or "autosuggest.datasets", value =
    \<your_dataset_hrn\> enables ingesting and searching of private
    POIs. Note: Only participants of the search customization can get
    access from HERE to use this feature, otherwise, a
    SearchError.INVALID_CUSTOM_OPTION_FORMAT will be propagated in
    callbacks. name = "discover.ranking" or "browse.ranking", value =
    "excursionDistance" enables balanced distribution of results for
    search in GeoCorridor . Constraint: using this parameter when
    searching an area that is not a GeoCorridor generates an error
    SearchError.BAD_REQUEST . Note: It is recommended to use
    SearchOptions.distributedResults instead. For a complete list of
    available endpoints, parameter names and their valid values, refer
    to HERE Geocoding & Search API v7 . Note: It's easy to set a wrong
    option that makes queries invalid, so make sure you read and
    understand the backend documentation.

    </div>

    Parameters:  
    `name` -

    Option name in the format \<endpoint_name\>.\<option_name\>, for
    example "discover.show".

    `value` -

    Option value.

    Returns:  
    Error in case when setting the option fails.

    </div>

  - <div id="sdk-for-android-explore-setEVInterface-com-here-sdk-search-EVSearchInterface"
    class="section detail">

    ### setEVInterface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEVInterface</span><span class="parameters">(@NonNull
    [EVSearchInterface](sdk-for-android-explore-com-here-sdk-search-evsearchinterface "interface in com.here.sdk.search") evcpInterface)</span>

    </div>

    <div class="block">

    Sets the EV interface through which search will interact with EVCP3.
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `evcpInterface` -

    The EV search interface implementation.

    </div>

  - <div id="sdk-for-android-explore-searchByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### searchByText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByText</span><span class="parameters">(@NonNull
    [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous text query search for Place instances
    within a given TextQuery.Area . The returned places are sorted by
    relevance.

    </div>

    Specified by:  
    [`searchByText`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

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

  - <div id="sdk-for-android-explore-searchByAddress-com-here-sdk-search-AddressQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### searchByAddress

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByAddress</span><span class="parameters">(@NonNull
    [AddressQuery](sdk-for-android-explore-com-here-sdk-search-addressquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous address query search for Place instances.
    This is the same type of search as forward geocoding, except that
    more data is returned than just the geographic coordinates of a
    given address. Note that an address can belong to more than one
    Place result, although all found places will share the same
    geographic coordinates. The returned places are sorted by relevance.

    </div>

    Specified by:  
    [`searchByAddress`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

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

  - <div id="sdk-for-android-explore-searchByCategory-com-here-sdk-search-CategoryQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### searchByCategory

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByCategory</span><span class="parameters">(@NonNull
    [CategoryQuery](sdk-for-android-explore-com-here-sdk-search-categoryquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous category search for Place instances. A list
    containing at least one PlaceCategory must be provided as part of
    the query .

    </div>

    Specified by:  
    [`searchByCategory`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

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

  - <div id="sdk-for-android-explore-searchByCoordinates-com-here-sdk-core-GeoCoordinates-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback"
    class="section detail">

    ### searchByCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SearchCallback](sdk-for-android-explore-com-here-sdk-search-searchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for Place instances based on the
    given geographic coordinates. This is the same search type as
    reverse geocoding, except that more data is returned than just the
    Address related to the given coordinates. Note that more than one
    Place can be related to the given coordinates. The returned places
    are sorted by relevance.

    </div>

    Specified by:  
    [`searchByCoordinates`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

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

  - <div id="sdk-for-android-explore-searchByPlaceId-com-here-sdk-search-PlaceIdQuery-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback"
    class="section detail">

    ### searchByPlaceId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByPlaceId</span><span class="parameters">(@NonNull
    [PlaceIdQuery](sdk-for-android-explore-com-here-sdk-search-placeidquery "class in com.here.sdk.search") query,
    @Nullable
    [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode,
    @NonNull
    [PlaceIdSearchCallback](sdk-for-android-explore-com-here-sdk-search-placeidsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on its ID and
    LanguageCode .

    </div>

    Specified by:  
    [`searchByPlaceId`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

    Parameters:  
    `query` -

    The id of place to search.

    `languageCode` -

    The preferred language for the search results. When unset or
    unsupported language is chosen, results will be returned in their
    local language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-searchByPickedPlace-com-here-sdk-core-PickedPlace-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback"
    class="section detail">

    ### searchByPickedPlace

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">searchByPickedPlace</span><span class="parameters">(@NonNull
    [PickedPlace](sdk-for-android-explore-com-here-sdk-core-pickedplace "class in com.here.sdk.core") pickedPlace,
    @Nullable
    [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode,
    @NonNull
    [PlaceIdSearchCallback](sdk-for-android-explore-com-here-sdk-search-placeidsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on the content
    found in PickedPlace . If PickedPlace data is obtained from the
    offline map, it may happen that the newer version that is used by
    the online service represented by SearchEngine no longer contains
    the related POI. In that case, SearchError.NO_RESULTS_FOUND error is
    reported. When that happens, you may try to obtain the POI from the
    offline map by calling OfflineSearchEngine.searchByPickedPlace ,
    only available for the Navigate license.

    </div>

    Specified by:  
    [`searchByPickedPlace`](sdk-for-android-explore-com-here-sdk-search-searchinterface#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

    Parameters:  
    `pickedPlace` -

    The content picked from map.

    `languageCode` -

    The preferred language for the search result. When unset or
    unsupported language is chosen, result will be returned in the local
    language.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-suggestByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SuggestCallback"
    class="section detail">

    ### suggestByText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">suggestByText</span><span class="parameters">(@NonNull
    [TextQuery](sdk-for-android-explore-com-here-sdk-search-textquery "class in com.here.sdk.search") query,
    @NonNull
    [SearchOptions](sdk-for-android-explore-com-here-sdk-search-searchoptions "class in com.here.sdk.search") options,
    @NonNull
    [SuggestCallback](sdk-for-android-explore-com-here-sdk-search-suggestcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to suggest places for text queries
    and returns suggestions sorted by relevance. Note that while
    OfflineSearchEngine includes as many details as are available,
    SearchEngine includes only the information that is relevant for
    autosuggest use cases. Complete details can be obtained by searching
    with PlaceIdQuery .

    </div>

    Specified by:  
    [`suggestByText`](sdk-for-android-explore-com-here-sdk-search-searchinterface#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback)) in
    interface [`SearchInterface`](sdk-for-android-explore-com-here-sdk-search-searchinterface "interface in com.here.sdk.search")

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


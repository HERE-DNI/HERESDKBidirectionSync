---
title: "OfflineSearchEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-offlinesearchengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.search.OfflineSearchEngine → com.here.NativeBase com.here.sdk.search.OfflineSearchEngine → com.here.sdk.search.OfflineSearchEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">OfflineSearchEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">SearchInterface</a></span>

</div>

<div class="block">

The OfflineSearchEngine works without internet and unlocks the search and geocoding capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications. It provides the same interfaces as the SearchEngine, but the results may slightly differ as the results are taken from already downloaded map data instead of initiating a new request to a HERE backend service. This way the data may be, for example, older compared to the data you may receive when using the SearchEngine. On the other hand, this class provides results faster as no online connection is necessary. In comparison to the SearchEngine, there are a few limitations: The IDs of POIs are different and may differ among different map versions. The implementation is different and the resources are limited, so the results can differ. OfflineSearchEngine sometimes doesn't return the requested number of results. Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data. However, cached data may be incomplete, which can result in searches returning partial or incomplete information. Therefore, it is recommended to use persistent map data. Make sure that at least LayerConfiguration.Feature.OFFLINE_SEARCH is enabled. For EV rich attributes also enable LayerConfiguration.Feature.EV , for truck rich attributes also enable LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES , for fuel station rich attributes also enable LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES in SDKOptions.layerConfiguration .

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      OfflineSearchEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      OfflineSearchEngine ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      attach ( MyPlaces dataSource, OnTaskCompleted callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Attach data source into SearchEngine instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search ( StructuredQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to search for places.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByAddress ( AddressQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous address query search for Place instances.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByCategory ( CategoryQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous category search for Place instances.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByCoordinates ( GeoCoordinates coordinates, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for Place instances based on the given geographic coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByPickedPlace ( PickedPlace pickedPlace, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for a Place based on the content found in PickedPlace .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByPlaceId ( PlaceIdQuery query, LanguageCode languageCode, PlaceIdSearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous search for a Place based on its ID and LanguageCode .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      searchByText ( TextQuery query, SearchOptions options, SearchCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous text query search for Place instances within a given TextQuery.Area .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-error" title="enum class in com.here.sdk.search">`OfflineSearchIndex.Error`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setIndexOptions ( SDKNativeEngine sdkEngine, OfflineSearchIndex.Options options, OfflineSearchIndexListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Enables or disables indexing.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      suggest ( StructuredQuery query, SearchOptions options, SuggestCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to suggest places for a StructuredQuery built with address elements and returns candidate suggestions sorted by relevance.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      suggestByText ( TextQuery query, SearchOptions options, SuggestCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### OfflineSearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">OfflineSearchEngine</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### OfflineSearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">OfflineSearchEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-attach-com-here-sdk-search-MyPlaces-com-here-sdk-core-threading-OnTaskCompleted" class="section detail">

    ### attach

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">attach</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-myplaces" title="class in com.here.sdk.search">MyPlaces</a> dataSource, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span>

    </div>

    <div class="block">

    Attach data source into SearchEngine instance. Places from MyPlaces ranked the same way as places from default source. New data source replaces old one. Note: Only OfflineSearchEngine supports search over MyPlaces.

    </div>

    Parameters:  
    `dataSource` -

    The data source.

    `callback` -

    The callback to be called when task is completed.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-search-com-here-sdk-search-StructuredQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">search</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to search for places. The user submits a StructuredQuery that returns places adhering to the constraints provided in StructuredQuery . For example, when user wants results of type street for a text query Invalidenstraße in Berlin , it can be searched by preparing StructuredQuery providing StructuredQuery.query as Invalidenstraße , StructuredQuery.areaCenter , StructuredQuery.AddressElements.country as Germany , StructuredQuery.AddressElements.city as Berlin and StructuredQuery.ResultType as STREET . The results will be presented only from the given geographical area. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `query` -

    Desired structured query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-suggest-com-here-sdk-search-StructuredQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SuggestCallback" class="section detail">

    ### suggest

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggest</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-structuredquery" title="class in com.here.sdk.search">StructuredQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to suggest places for a StructuredQuery built with address elements and returns candidate suggestions sorted by relevance. For example, when user wants suggestions of type street for a text query Invalidenstraße in Berlin , it can be searched by preparing StructuredQuery providing StructuredQuery.query as Invalidenstraße , StructuredQuery.areaCenter , StructuredQuery.AddressElements.country as Germany , StructuredQuery.AddressElements.city as Berlin and StructuredQuery.ResultType as STREET . The suggestions will be presented only from the given geographical area. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `query` -

    Desired structured query to search.

    `options` -

    Search options.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-setIndexOptions-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-search-OfflineSearchIndex-Options-com-here-sdk-search-OfflineSearchIndexListener" class="section detail">

    ### setIndexOptions

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a></span> <span class="element-name">setIndexOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindex-options" title="class in com.here.sdk.search">OfflineSearchIndex.Options</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-offlinesearchindexlistener" title="interface in com.here.sdk.search">OfflineSearchIndexListener</a> listener)</span>

    </div>

    <div class="block">

    Enables or disables indexing. When indexing is enabled, HERE SDK will create a detailed index over persistent map data and update it as needed. A detailed index enables finding data faster and over entire persistent map. Creating an index takes time, but usually no more than a few seconds up to a couple of minutes, depending on persistent map size. As the feature is improved, the indexing time will improve. Also please note that this is a heavy processing task. The stored index increases the space taken by offline maps by around 2-5%. This may also improve in future versions. Indexing is disabled by default. If you want it enabled, make sure to call setIndexOptions with OfflineSearchIndex.Options.enabled as true before any operations in MapDownloader or MapUpdater that modify the persistent map. Calling setIndexOptions may also create or remove map index to match the previously installed map regions. If the matching index for installed map regions is found, then indexing is skipped. While a new index is being created, OfflineSearchEngine functionality can still be used. However, without a valid index in place yet, it operates as though indexing is disabled. If SDKNativeEngine is disposed during indexing (for example, by closing the app), the indexing is cancelled. Recreating SDKNativeEngine and enabling indexing will ensure that index is created. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `sdkEngine` -

    Indexing is enabled and disabled per SDKNativeEngine instance. The index is created inside the related <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath">`SDKOptions.persistentMapStoragePath`</a>.

    `options` -

    Sets indexing options.

    `listener` -

    The listener that will receive updates about indexing process. When `OfflineSearchIndex.Options.enabled` is true, SDK would store listener and the listener will receive updates about indexing progress every time it is performed. When `OfflineSearchIndex.Options.enabled` is false, SDK would report indexing removal progress to the listener one last time and remove storage of listener.

    Returns:  
    An error in case there was one. It's `null` if the indexing listener could be configured successfully.

    </div>

  - <div id="sdk-for-android-navigate-searchByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByText

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByText</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous text query search for Place instances within a given TextQuery.Area . The returned places are sorted by relevance.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback">`searchByText`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-searchByAddress-com-here-sdk-search-AddressQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByAddress

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByAddress</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery" title="class in com.here.sdk.search">AddressQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous address query search for Place instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one Place result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByAddress(com.here.sdk.search.AddressQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback">`searchByAddress`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-searchByCategory-com-here-sdk-search-CategoryQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByCategory

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCategory</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous category search for Place instances. A list containing at least one PlaceCategory must be provided as part of the query .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByCategory(com.here.sdk.search.CategoryQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback">`searchByCategory`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-searchByCoordinates-com-here-sdk-core-GeoCoordinates-com-here-sdk-search-SearchOptions-com-here-sdk-search-SearchCallback" class="section detail">

    ### searchByCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByCoordinates</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchcallback" title="interface in com.here.sdk.search">SearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for Place instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the Address related to the given coordinates. Note that more than one Place can be related to the given coordinates. The returned places are sorted by relevance.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByCoordinates(com.here.sdk.core.GeoCoordinates,com.here.sdk.search.SearchOptions,com.here.sdk.search.SearchCallback">`searchByCoordinates`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-searchByPlaceId-com-here-sdk-search-PlaceIdQuery-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback" class="section detail">

    ### searchByPlaceId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPlaceId</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search">PlaceIdQuery</a> query, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on its ID and LanguageCode .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByPlaceId(com.here.sdk.search.PlaceIdQuery,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback">`searchByPlaceId`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-searchByPickedPlace-com-here-sdk-core-PickedPlace-com-here-sdk-core-LanguageCode-com-here-sdk-search-PlaceIdSearchCallback" class="section detail">

    ### searchByPickedPlace

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">searchByPickedPlace</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-pickedplace" title="class in com.here.sdk.core">PickedPlace</a> pickedPlace, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-placeidsearchcallback" title="interface in com.here.sdk.search">PlaceIdSearchCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous search for a Place based on the content found in PickedPlace . If PickedPlace data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by SearchEngine no longer contains the related POI. In that case, SearchError.NO_RESULTS_FOUND error is reported. When that happens, you may try to obtain the POI from the offline map by calling OfflineSearchEngine.searchByPickedPlace , only available for the Navigate license.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#searchByPickedPlace(com.here.sdk.core.PickedPlace,com.here.sdk.core.LanguageCode,com.here.sdk.search.PlaceIdSearchCallback">`searchByPickedPlace`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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

  - <div id="sdk-for-android-navigate-suggestByText-com-here-sdk-search-TextQuery-com-here-sdk-search-SearchOptions-com-here-sdk-search-SuggestCallback" class="section detail">

    ### suggestByText

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">suggestByText</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-searchoptions" title="class in com.here.sdk.search">SearchOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-search-suggestcallback" title="interface in com.here.sdk.search">SuggestCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance. Note that while OfflineSearchEngine includes as many details as are available, SearchEngine includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with PlaceIdQuery .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface#suggestByText(com.here.sdk.search.TextQuery,com.here.sdk.search.SearchOptions,com.here.sdk.search.SuggestCallback">`suggestByText`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-search-searchinterface" title="interface in com.here.sdk.search">`SearchInterface`</a>

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


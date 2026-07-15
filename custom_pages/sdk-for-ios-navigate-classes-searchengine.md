---
title: "SearchEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-searchengine"
---

# SearchEngine

<div class="declaration">

<div class="language">

``` highlight
public class SearchEngine : SearchInterface
```

``` highlight
extension SearchEngine: NativeBase
```

``` highlight
extension SearchEngine: Hashable
```

</div>

</div>

The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications. It enables to search for HERE points of interests, forward and reverse geocode addresses and geographic coordinates from the HERE map and search for suggested addresses or place candidates based on incomplete or misspelled queries.

It also allows to search along a given <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a> set inside a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a> as part of a <a href="sdk-for-ios-navigate-structs-textquery">`TextQuery`</a>.

The SearchEngine API requires an online connection to execute the requests.

**Note:** All methods are provided in two flavors. One uses a <a href="sdk-for-ios-navigate-search#/s:7heresdk23SearchCompletionHandlera">`SearchCompletionHandler`</a> and the other uses a <a href="sdk-for-ios-navigate-search#/s:7heresdk31SearchExtendedCompletionHandlera">`SearchExtendedCompletionHandler`</a>: The later adds a <a href="sdk-for-ios-navigate-structs-responsedetails">`ResponseDetails`</a> result type that provides the `requestId` of a search request and a `correlationId` to identify multiple, related queries. This may be useful for debug purposes.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>Instance of an existing SDKEngine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      searchByText(_: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous text query search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances within a given <a href="sdk-for-ios-navigate-structs-textquery-area">`TextQuery.Area`</a>. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByText ( _ query : TextQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired free-form text query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      searchByAddress(_: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous address query search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByAddress ( _ query : AddressQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired free-form address query text to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      searchByCategory(_: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous category search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances. A list containing at least one <a href="sdk-for-ios-navigate-classes-placecategory">`PlaceCategory`</a> must be provided as part of the

      searchByCategory(...).query

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByCategory ( _ query : CategoryQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Query with list of desired categories.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      searchByCoordinates(_: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the <a href="sdk-for-ios-navigate-structs-address">`Address`</a> related to the given coordinates. Note that more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> can be related to the given coordinates. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByCoordinates ( _ coordinates : GeoCoordinates , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The coordinates where to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      searchByPlaceId(_: languageCode: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> based on its ID and <a href="sdk-for-ios-navigate-enums-languagecode">`LanguageCode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByPlaceId ( _ query : PlaceIdQuery , languageCode : LanguageCode ?, completion : @escaping PlaceIdSearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>The id of place to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>languageCode</code></em><code> </code></td>
  <td><div>
  <p>The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      searchByPickedPlace(_: languageCode: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> based on the content found in <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a>. If <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by `SearchEngine` no longer contains the related POI. In that case, <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">`SearchError.noResultsFound`</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func searchByPickedPlace ( _ pickedPlace : PickedPlace , languageCode : LanguageCode ?, completion : @escaping PlaceIdSearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>pickedPlace</code></em><code> </code></td>
  <td><div>
  <p>The content picked from map.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>languageCode</code></em><code> </code></td>
  <td><div>
  <p>The preferred language for the search result. When unset or unsupported language is chosen, result will be returned in the local language.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      suggestByText(_: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

  Note that while <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> includes as many details as are available, `SearchEngine` includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func suggestByText ( _ query : TextQuery , options : SearchOptions , completion : @escaping SuggestCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired text query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(textQuery: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to do a text query search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances. Optionally, search along a polyline, such as a route, by specifying a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a>. Provides candidate places sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( textQuery query : TextQuery , options : SearchOptions , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired free-form text query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(addressQuery: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for places based on a given address. This is the same process as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result, although all found places will share the same geographic coordinates. Provides candidate places sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( addressQuery query : AddressQuery , options : SearchOptions , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired free-form address query text to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(placeIdQuery: languageCode: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> based on its ID and <a href="sdk-for-ios-navigate-enums-languagecode">`LanguageCode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( placeIdQuery query : PlaceIdQuery , languageCode : LanguageCode ?, completion : @escaping PlaceIdSearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>The id of place to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>languageCode</code></em><code> </code></td>
  <td><div>
  <p>The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(coordinates: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for places based on given geographic coordinates. This is the same process as reverse geocoding, except that more data is returned than just the <a href="sdk-for-ios-navigate-structs-address">`Address`</a> that belongs to given coordinates. Note that coordinates can belong to more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result. Provides candidate places sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( coordinates : GeoCoordinates , options : SearchOptions , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The coordinates where to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(circle: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for places based on given circular spatial filter. This is the same process as reverse geocoding, except that more data is returned than just the <a href="sdk-for-ios-navigate-structs-address">`Address`</a> that belongs to given coordinates. Note that coordinates can belong to more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result. Provides candidate places sorted by relevance and located inside the radius of filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( circle : GeoCircle , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>circle</code></em><code> </code></td>
  <td><div>
  <p>The coordinates where to search and radius of the circular spatial filter. Passed in form of <a href="sdk-for-ios-navigate-structs-geocircle"><code>GeoCircle</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(circle: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for places based on given circular spatial filter. This is the same process as reverse geocoding, except that more data is returned than just the <a href="sdk-for-ios-navigate-structs-address">`Address`</a> that belongs to given coordinates. Note that coordinates can belong to more than one <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result. Provides candidate places sorted by relevance and located inside the radius of filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( circle : GeoCircle , options : SearchOptions , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>circle</code></em><code> </code></td>
  <td><div>
  <p>The coordinates where to search and radius of the circular spatial filter. Passed in form of <a href="sdk-for-ios-navigate-structs-geocircle"><code>GeoCircle</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      sendRequest(href: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request by using the given href. The href value can be obtained from <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> objects, which are the result of successful call to

      SearchEngine.suggest(...)

  . Currently supports only /v1/discover path. Provides candidate places sorted by relevance.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func sendRequest ( href : String , completion : @escaping SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>href</code></em><code> </code></td>
  <td><div>
  <p>The direct link.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      sendRequest(href: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request by using the given href. The href value can be obtained from <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> objects, which are the result of successful call to

      SearchEngine.suggest(...)

  . Currently supports only /v1/discover path. Provides candidate places sorted by relevance.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func sendRequest ( href : String , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>href</code></em><code> </code></td>
  <td><div>
  <p>The direct link.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      search(categoryQuery: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to do a category search for <a href="sdk-for-ios-navigate-classes-place">`Place`</a> instances. A list containing at least one <a href="sdk-for-ios-navigate-classes-placecategory">`PlaceCategory`</a> must be provided as part of the

      SearchEngine.search(CategoryQuery, SearchOptions, SearchExtendedCompletionHandler).query

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( categoryQuery query : CategoryQuery , options : SearchOptions , completion : @escaping SearchExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Query with list of desired categories.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      suggest(textQuery: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to suggest places for text queries and returns candidate suggestions sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func suggest ( textQuery query : TextQuery , options : SearchOptions , completion : @escaping SuggestExtendedCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired text query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Search options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      setCustomOption(name: value: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom option for search backend queries. This allows more control over the behavior of the search algorithm. Name has the format <endpoint_name>.<option_name>, for example “discover.show”. Values can be combined for the same name by using a comma, for example “truck,fuel”. The custom option is applied only for the endpoint that is specified as prefix in `name`. Some of the supported name/value options are:</option_name></endpoint_name>

  - name = “revgeocode.with”, value = “unnamedStreets” enables the retrieval of access points on unnamed streets.
  - name = “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”, value = “truck” enables retreival of truck amenities. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated in callbacks.
  - name = “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”, value = “fuel” enables retreival of fuel station details. **Note:** Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated in callbacks.
  - name = “lookup.show” or “discover.show” or “browse.show”, value = “ev” enables retreival of EV charging station details.
  - name = “lookup.show” or “discover.show” or “browse.show”, value = “eMobilityServiceProviders” enables retreival of e-Mobility Service Providers details.
  - name = “lookup.show” or “discover.show” or “browse.show”, value = “tripadvisor” adds images, ratings, and editorials from Tripadvisor ™. **Note:** Only clients with a license with TripAdvisor for rich content will actually get it. If this licence is missing, TripAdvisor rich content will be missing, with no error reported. This content is only added to top 10 search results. If more results are returned, they will be missing rich TripAdvisor content.
  - name = “lookup.datasets” or “discover.datasets” or “browse.datasets” or “autosuggest.datasets”, value = <your_dataset_hrn> enables ingesting and searching of private POIs. **Note:** Only participants of the search customization can get access from HERE to use this feature, otherwise, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF">`SearchError.invalidCustomOptionFormat`</a> will be propagated in callbacks.</your_dataset_hrn>
  - name = “discover.ranking” or “browse.ranking”, value = “excursionDistance” enables balanced distribution of results for search in <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a>. Constraint: using this parameter when searching an area that is not a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a> generates an error <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO10badRequestyA2CmF">`SearchError.badRequest`</a>. **Note:** It is recommended to use <a href="sdk-for-ios-navigate-structs-searchoptions#/s:7heresdk13SearchOptionsV18distributedResultsSbvp">`SearchOptions.distributedResults`</a> instead. For a complete list of available endpoints, parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding & Search API v7</a>. **Note:** It’s easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomOption ( name : String , value : String ) -> SearchError ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Option name in the format <endpoint_name>.<option_name>, for example “discover.show”.</option_name></endpoint_name></p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Option value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Error in case when setting the option fails.

  </div>

  </div>

  </div>

- <div>

      setEVInterface(evcpInterface: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the EV interface through which search will interact with EVCP3. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setEVInterface ( evcpInterface : EVSearchInterface )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>evcpInterface</code></em><code> </code></td>
  <td><div>
  <p>The EV search interface implementation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


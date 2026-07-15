---
title: "SearchInterface Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-searchinterface"
---

# SearchInterface

<div class="declaration">

<div class="language">

``` highlight
public protocol SearchInterface : AnyObject
```

</div>

</div>

Provides the protocol for the online and offline search engines.

</div>

<div class="section section task-group-section">

<div class="task-group">

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
  @discardableResult func searchByText ( _ query : TextQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
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
  @discardableResult func searchByAddress ( _ query : AddressQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
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
  @discardableResult func searchByCategory ( _ query : CategoryQuery , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
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
  @discardableResult func searchByCoordinates ( _ coordinates : GeoCoordinates , options : SearchOptions , completion : @escaping SearchCompletionHandler ) -> TaskHandle
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
  @discardableResult func searchByPlaceId ( _ query : PlaceIdQuery , languageCode : LanguageCode ?, completion : @escaping PlaceIdSearchCompletionHandler ) -> TaskHandle
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

  Performs an asynchronous search for a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> based on the content found in <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a>. If <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> no longer contains the related POI. In that case, <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">`SearchError.noResultsFound`</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult func searchByPickedPlace ( _ pickedPlace : PickedPlace , languageCode : LanguageCode ?, completion : @escaping PlaceIdSearchCompletionHandler ) -> TaskHandle
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

  Note that while <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> includes as many details as are available, <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult func suggestByText ( _ query : TextQuery , options : SearchOptions , completion : @escaping SuggestCompletionHandler ) -> TaskHandle
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

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


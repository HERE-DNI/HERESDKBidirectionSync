---
title: "SearchInterface Protocol Reference"
slug: "sdk-for-ios-explore-protocols-searchinterface"
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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByText-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP12searchByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByText(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous text query search for <a href="sdk-for-ios-explore-classes-place">`Place`</a> instances within a given <a href="sdk-for-ios-explore-structs-textquery-area">`TextQuery.Area`</a>. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByAddress-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP15searchByAddress_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByAddress(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous address query search for <a href="sdk-for-ios-explore-classes-place">`Place`</a> instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="sdk-for-ios-explore-classes-place">`Place`</a> result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByAddress(_ query: AddressQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-addressquery">AddressQuery</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByCategory-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP16searchByCategory_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByCategory(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous category search for <a href="sdk-for-ios-explore-classes-place">`Place`</a> instances. A list containing at least one <a href="sdk-for-ios-explore-classes-placecategory">`PlaceCategory`</a> must be provided as part of the

      searchByCategory(...).query

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByCategory(_ query: CategoryQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-categoryquery">CategoryQuery</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByCoordinates-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoF0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByCoordinates(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for <a href="sdk-for-ios-explore-classes-place">`Place`</a> instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the <a href="sdk-for-ios-explore-structs-address">`Address`</a> related to the given coordinates. Note that more than one <a href="sdk-for-ios-explore-classes-place">`Place`</a> can be related to the given coordinates. The returned places are sorted by relevance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByCoordinates(_ coordinates: GeoCoordinates, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByPlaceId-_-languageCode-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0fG5QueryV_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0F0CSgtctF" class="token"><code>searchByPlaceId(_:</code><wbr></wbr><code>languageCode:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for a <a href="sdk-for-ios-explore-classes-place">`Place`</a> based on its ID and <a href="sdk-for-ios-explore-enums-languagecode">`LanguageCode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByPlaceId(_ query: PlaceIdQuery, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-placeidquery">PlaceIdQuery</a>
  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-searchByPickedPlace-_-languageCode-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0fG0V_AA08LanguageI0OSgyAA0B5ErrorOSg_AA0G0CSgtctF" class="token"><code>searchByPickedPlace(_:</code><wbr></wbr><code>languageCode:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for a <a href="sdk-for-ios-explore-classes-place">`Place`</a> based on the content found in <a href="sdk-for-ios-explore-structs-pickedplace">`PickedPlace`</a>. If <a href="sdk-for-ios-explore-structs-pickedplace">`PickedPlace`</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a> no longer contains the related POI. In that case, <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO14noResultsFoundyA2CmF">`SearchError.noResultsFound`</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func searchByPickedPlace(_ pickedPlace: PickedPlace, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-pickedplace">PickedPlace</a>
  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15SearchInterfaceP13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-suggestByText-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-searchinterface#sdk-for-ios-explore-s-7heresdk15SearchInterfaceP13suggestByText_7options10completionAA10TaskHandle_pAA0F5QueryV_AA0B7OptionsVyAA0B5ErrorOSg_SayAA10SuggestionCGSgtctF" class="token"><code>suggestByText(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

  Note that while <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> includes as many details as are available, <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a> includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with <a href="sdk-for-ios-explore-structs-placeidquery">`PlaceIdQuery`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func suggestByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SuggestCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


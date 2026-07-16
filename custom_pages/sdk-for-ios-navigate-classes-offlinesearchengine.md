---
title: "OfflineSearchEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-offlinesearchengine"
---

# OfflineSearchEngine

<div class="declaration">

<div class="language">

``` highlight
public class OfflineSearchEngine : SearchInterface
```

``` highlight
extension OfflineSearchEngine: NativeBase
```

``` highlight
extension OfflineSearchEngine: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-protocols-searchinterface">SearchInterface</a>

</div>

The OfflineSearchEngine works without internet and unlocks the search and geocoding capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.

It provides the same interfaces as the SearchEngine, but the results may slightly differ as the results are taken from already downloaded map data instead of initiating a new request to a HERE backend service. This way the data may be, for example, older compared to the data you may receive when using the SearchEngine. On the other hand, this class provides results faster as no online connection is necessary.

In comparison to the SearchEngine, there are a few limitations:

- The IDs of POIs are different and may differ among different map versions.
- The implementation is different and the resources are limited, so the results can differ.
- OfflineSearchEngine sometimes doesn’t return the requested number of results.

Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data. However, cached data may be incomplete, which can result in searches returning partial or incomplete information. Therefore, it is recommended to use persistent map data. Make sure that at least <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a> is enabled. For EV rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a>, for truck rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">`LayerConfiguration.Feature.truckServiceAttributes`</a>, for fuel station rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">`LayerConfiguration.Feature.fuelStationAttributes`</a> in <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineCACyKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineCACyKcfc" class="token"><code>init()</code></a> 

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

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineCyAcA09SDKNativeD0CKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineCyAcA09SDKNativeD0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByText-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC12searchByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByText(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  @discardableResult
  public func searchByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByAddress-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15searchByAddress_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByAddress(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  @discardableResult
  public func searchByAddress(_ query: AddressQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-addressquery">AddressQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByCategory-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC16searchByCategory_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByCategory(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  @discardableResult
  public func searchByCategory(_ query: CategoryQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-categoryquery">CategoryQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByCoordinates-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC19searchByCoordinates_7options10completionAA10TaskHandle_pAA03GeoG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>searchByCoordinates(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  @discardableResult
  public func searchByCoordinates(_ coordinates: GeoCoordinates, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0gH5QueryV_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0G0CSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByPlaceId-_-languageCode-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15searchByPlaceId_12languageCode10completionAA10TaskHandle_pAA0gH5QueryV_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0G0CSgtctF" class="token"><code>searchByPlaceId(_:</code><wbr></wbr><code>languageCode:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  @discardableResult
  public func searchByPlaceId(_ query: PlaceIdQuery, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-placeidquery">PlaceIdQuery</a>
  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0gH0V_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0H0CSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-searchByPickedPlace-_-languageCode-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC19searchByPickedPlace_12languageCode10completionAA10TaskHandle_pAA0gH0V_AA08LanguageJ0OSgyAA0C5ErrorOSg_AA0H0CSgtctF" class="token"><code>searchByPickedPlace(_:</code><wbr></wbr><code>languageCode:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous search for a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> based on the content found in <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a>. If <a href="sdk-for-ios-navigate-structs-pickedplace">`PickedPlace`</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> no longer contains the related POI. In that case, <a href="sdk-for-ios-navigate-enums-searcherror#sdk-for-ios-navigate-s-7heresdk11SearchErrorO14noResultsFoundyA2CmF">`SearchError.noResultsFound`</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling `OfflineSearchEngine.searchByPickedPlace`, only available for the Navigate license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func searchByPickedPlace(_ pickedPlace: PickedPlace, languageCode: LanguageCode?, completion: @escaping PlaceIdSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-pickedplace">PickedPlace</a>
  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-suggestByText-_-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC13suggestByText_7options10completionAA10TaskHandle_pAA0G5QueryV_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF" class="token"><code>suggestByText(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.

  Note that while `OfflineSearchEngine` includes as many details as are available, <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> includes only the information that is relevant for autosuggest use cases. Complete details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func suggestByText(_ query: TextQuery, options: SearchOptions, completion: @escaping SuggestCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC6attach10dataSource8callbackAA10TaskHandle_pAA8MyPlacesC_yAA0I7OutcomeOctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-attach-dataSource-callback" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC6attach10dataSource8callbackAA10TaskHandle_pAA8MyPlacesC_yAA0I7OutcomeOctF" class="token"><code>attach(dataSource:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Attach data source into SearchEngine instance. Places from MyPlaces ranked the same way as places from default source. New data source replaces old one. Note: Only OfflineSearchEngine supports search over MyPlaces.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func attach(dataSource: MyPlaces, callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-myplaces">MyPlaces</a>
  - <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>dataSource</code></em><code> </code></td>
  <td><div>
  <p>The data source.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC6search11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-search-structQuery-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC6search11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA5PlaceCGSgtctF" class="token"><code>search(structQuery:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for places. The user submits a <a href="sdk-for-ios-navigate-structs-structuredquery">`StructuredQuery`</a> that returns places adhering to the constraints provided in <a href="sdk-for-ios-navigate-structs-structuredquery">`StructuredQuery`</a>. For example, when user wants results of type street for a text query `Invalidenstraße` in `Berlin`, it can be searched by preparing <a href="sdk-for-ios-navigate-structs-structuredquery">`StructuredQuery`</a> providing <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5querySSvp">`StructuredQuery.query`</a> as `Invalidenstraße`, <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp">`StructuredQuery.areaCenter`</a>, <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp">`StructuredQuery.AddressElements.country`</a> as `Germany`, <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp">`StructuredQuery.AddressElements.city`</a> as `Berlin` and <a href="sdk-for-ios-navigate-structs-structuredquery-resulttype">`StructuredQuery.ResultType`</a> as `STREET`. The results will be presented only from the given geographical area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func search(structQuery query: StructuredQuery, options: SearchOptions, completion: @escaping SearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-structuredquery">StructuredQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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
  <p>Desired structured query to search.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC7suggest11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-suggest-structQuery-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC7suggest11structQuery7options10completionAA10TaskHandle_pAA010StructuredG0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA10SuggestionCGSgtctF" class="token"><code>suggest(structQuery:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to suggest places for a <a href="sdk-for-ios-navigate-structs-structuredquery">`StructuredQuery`</a> built with address elements and returns candidate suggestions sorted by relevance. For example, when user wants suggestions of type street for a text query `Invalidenstraße` in `Berlin`, it can be searched by preparing <a href="sdk-for-ios-navigate-structs-structuredquery">`StructuredQuery`</a> providing <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5querySSvp">`StructuredQuery.query`</a> as `Invalidenstraße`, <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp">`StructuredQuery.areaCenter`</a>, <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp">`StructuredQuery.AddressElements.country`</a> as `Germany`, <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp">`StructuredQuery.AddressElements.city`</a> as `Berlin` and <a href="sdk-for-ios-navigate-structs-structuredquery-resulttype">`StructuredQuery.ResultType`</a> as `STREET`. The suggestions will be presented only from the given geographical area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func suggest(structQuery query: StructuredQuery, options: SearchOptions, completion: @escaping SuggestCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-structuredquery">StructuredQuery</a>
  - <a href="sdk-for-ios-navigate-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-navigate-search#sdk-for-ios-navigate-s-7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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
  <p>Desired structured query to search.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15setIndexOptions03sdkD07options8listenerAA0bcF0C5ErrorOSgAA09SDKNativeD0C_AI0G0VAA0bcF8Listener_ptFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setIndexOptions-sdkEngine-options-listener" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-offlinesearchengine#sdk-for-ios-navigate-s-7heresdk19OfflineSearchEngineC15setIndexOptions03sdkD07options8listenerAA0bcF0C5ErrorOSgAA09SDKNativeD0C_AI0G0VAA0bcF8Listener_ptFZ" class="token"><code>setIndexOptions(sdkEngine:</code><wbr></wbr><code>options:</code><wbr></wbr><code>listener:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables or disables indexing. When indexing is enabled, HERE SDK will create a detailed index over persistent map data and update it as needed. A detailed index enables finding data faster and over entire persistent map. Creating an index takes time, but usually no more than a few seconds up to a couple of minutes, depending on persistent map size. As the feature is improved, the indexing time will improve. Also please note that this is a heavy processing task. The stored index increases the space taken by offline maps by around 2-5%. This may also improve in future versions.

  Indexing is disabled by default. If you want it enabled, make sure to call setIndexOptions with <a href="sdk-for-ios-navigate-classes-offlinesearchindex-options#sdk-for-ios-navigate-s-7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp">`OfflineSearchIndex.Options.enabled`</a> as `true` before any operations in <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a> or <a href="sdk-for-ios-navigate-classes-mapupdater">`MapUpdater`</a> that modify the persistent map. Calling setIndexOptions may also create or remove map index to match the previously installed map regions. If the matching index for installed map regions is found, then indexing is skipped. While a new index is being created, `OfflineSearchEngine` functionality can still be used. However, without a valid index in place yet, it operates as though indexing is disabled. If <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> is disposed during indexing (for example, by closing the app), the indexing is cancelled. Recreating <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> and enabling indexing will ensure that index is created.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setIndexOptions(sdkEngine: SDKNativeEngine, options: OfflineSearchIndex.Options, listener: OfflineSearchIndexListener) -> OfflineSearchIndex.Error?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-classes-offlinesearchindex">OfflineSearchIndex</a>
  - <a href="sdk-for-ios-navigate-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a>

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
  <p>Indexing is enabled and disabled per SDKNativeEngine instance. The index is created inside the related <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV24persistentMapStoragePathSSvp"><code>SDKOptions.persistentMapStoragePath</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Sets indexing options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>listener</code></em><code> </code></td>
  <td><div>
  <p>The listener that will receive updates about indexing process. When <a href="sdk-for-ios-navigate-classes-offlinesearchindex-options#sdk-for-ios-navigate-s-7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp"><code>OfflineSearchIndex.Options.enabled</code></a> is true, SDK would store listener and the listener will receive updates about indexing progress every time it is performed. When <a href="sdk-for-ios-navigate-classes-offlinesearchindex-options#sdk-for-ios-navigate-s-7heresdk18OfflineSearchIndexC7OptionsV7enabledSbvp"><code>OfflineSearchIndex.Options.enabled</code></a> is false, SDK would report indexing removal progress to the listener one last time and remove storage of listener.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An error in case there was one. It’s `nil` if the indexing listener could be configured successfully.

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


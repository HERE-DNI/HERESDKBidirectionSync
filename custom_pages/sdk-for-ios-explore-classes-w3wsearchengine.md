---
title: "W3WSearchEngine Class Reference"
slug: "sdk-for-ios-explore-classes-w3wsearchengine"
---

# W3WSearchEngine

<div class="declaration">

<div class="language">

``` highlight
public class W3WSearchEngine
```

``` highlight
extension W3WSearchEngine: NativeBase
```

``` highlight
extension W3WSearchEngine: Hashable
```

</div>

</div>

what3words is an alternative geocode system designed to identify any location on the planet. The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which has a three-word address. For example, the front door of HERE’s Berlin office is identified by “///wage.mere.heap”. `W3WSearchEngine` allows you to convert 3 word addresses to coordinates and also coordinates to 3 word addresses.

**Note:** Using W3WSearchEngine requires a licence to access HERE what3words APIs.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15W3WSearchEngineCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-w3wsearchengine#sdk-for-ios-explore-s-7heresdk15W3WSearchEngineCACyKcfc" class="token"><code>init()</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

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

   <span id="sdk-for-ios-explore-s-7heresdk15W3WSearchEngineCyAcA09SDKNativeD0CKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-w3wsearchengine#sdk-for-ios-explore-s-7heresdk15W3WSearchEngineCyAcA09SDKNativeD0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

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

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk15W3WSearchEngineC6search5words10completionAA10TaskHandle_pSS_yAA0bC5ErrorOSg_AA0B7WSquareVSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-search-words-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-w3wsearchengine#sdk-for-ios-explore-s-7heresdk15W3WSearchEngineC6search5words10completionAA10TaskHandle_pSS_yAA0bC5ErrorOSg_AA0B7WSquareVSgtctF" class="token"><code>search(words:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for a <a href="sdk-for-ios-explore-structs-w3wsquare">`W3WSquare`</a> that corresponds to the given 3 words.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func search(words: String, completion: @escaping W3WSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
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
  <td><code> </code><em><code>words</code></em><code> </code></td>
  <td><div>
  <p>A 3 word address as a string. It must be three words separated with dots or a japanese middle dot character (・). Words separated by spaces will be rejected. Optionally, the 3 word address can be prefixed with ///.</p>
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

  Handle that can be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15W3WSearchEngineC6search11coordinates8language10completionAA10TaskHandle_pAA14GeoCoordinatesV_SSSgyAA0bC5ErrorOSg_AA0B7WSquareVSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-search-coordinates-language-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-w3wsearchengine#sdk-for-ios-explore-s-7heresdk15W3WSearchEngineC6search11coordinates8language10completionAA10TaskHandle_pAA14GeoCoordinatesV_SSSgyAA0bC5ErrorOSg_AA0B7WSquareVSgtctF" class="token"><code>search(coordinates:</code><wbr></wbr><code>language:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to search for a <a href="sdk-for-ios-explore-structs-w3wsquare">`W3WSquare`</a>, which includes the 3 word address, that corresponds to the given coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func search(coordinates: GeoCoordinates, language: String?, completion: @escaping W3WSearchCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-search#sdk-for-ios-explore-s-7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
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
  <td><code> </code><em><code>language</code></em><code> </code></td>
  <td><div>
  <p>A supported 3 word address language as an ISO 639-1 2 letter code. For Bosnian-Croatian-Montenegrin-Serbian use “oo”. Defaults to “en” (English).</p>
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

  Handle that can be used to manipulate the execution of the task.

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


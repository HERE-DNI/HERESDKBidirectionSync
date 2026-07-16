---
title: "VenueEngine Class Reference"
slug: "sdk-for-ios-explore-classes-venueengine"
---

# VenueEngine

<div class="declaration">

<div class="language">

``` highlight
public class VenueEngine
```

``` highlight
extension VenueEngine: NativeBase
```

``` highlight
extension VenueEngine: Hashable
```

</div>

</div>

VenueEngine is an add-on to the base map functionality with its own content loading and cache. VenueEngine gives access to the venue functionality, which allows you to load and visualize venues on the map, search content inside venues etc.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC8callbackACyycSg_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC8callbackACyycSg_tKcfc" class="token"><code>init(callback:</code><wbr></wbr><code>)</code></a> 

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
  public init(callback: VenueEngineInitCompletionHandler?) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>

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
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The optional callback that will be triggered when a venue engine initialization will be completed. After the initialization, the <a href="sdk-for-ios-explore-classes-venueservice"><code>VenueService</code></a> should be started using one of its methods or using</p>
  <pre><code>VenueEngine.start(String)</code></pre>
  .
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC_8callbackAcA09SDKNativeC0C_yycSgtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC_8callbackAcA09SDKNativeC0C_yycSgtKcfc" class="token"><code>init(_:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

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
  public init(_ sdkEngine: SDKNativeEngine, callback: VenueEngineInitCompletionHandler?) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>

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
  <p>Instance of existing SDKEngine.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The optional callback that will be triggered when a venue engine initialization will be completed. After the initialization, the <a href="sdk-for-ios-explore-classes-venueservice"><code>VenueService</code></a> should be started using one of its methods or using</p>
  <pre><code>VenueEngine.start(String)</code></pre>
  .
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC12venueServiceAA0bE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-venueService" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC12venueServiceAA0bE0Cvp" class="token"><code>venueService</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The venue service. Gets the <a href="sdk-for-ios-explore-classes-venueservice">`VenueService`</a>. This service can be used to load the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> objects.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueService: VenueService { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venueservice">VenueService</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC8venueMapAA0bE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-venueMap" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC8venueMapAA0bE0Cvp" class="token"><code>venueMap</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The venue map. Gets a venue map to visualize venues and control the state of the venues on the map. You need to start the <a href="sdk-for-ios-explore-classes-venueservice">`VenueService`</a> to be able to load venues.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueMap: VenueMap { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuemap">VenueMap</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC5start8callbackyyAA19AuthenticationErrorOSg_AA0F4DataVSgtcSg_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC5start8callbackyyAA19AuthenticationErrorOSg_AA0F4DataVSgtcSg_tF" class="token"><code>start(callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticates asynchronously using HERE SDK credentials and uses a result token to start the <a href="sdk-for-ios-explore-classes-venueservice">`VenueService`</a>. An initialization status of the venue service is returned to objects registered as <a href="sdk-for-ios-explore-protocols-venueservicedelegate">`VenueServiceDelegate`</a>. If the authentication will fail, the venue service will not be started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(callback: AuthenticationCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>

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
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The optional callback that will be triggered when the authentication will be completed. If the authentication fails, the venue service will not be started.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC5start5tokenySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-token" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC5start5tokenySS_tF" class="token"><code>start(token:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticates asynchronously using HERE SDK credentials using a token to start the <a href="sdk-for-ios-explore-classes-venueservice">`VenueService`</a>. An initialization status of the venue service is returned to objects registered as <a href="sdk-for-ios-explore-protocols-venueservicedelegate">`VenueServiceDelegate`</a>. If the authentication will fail, the venue service will not be started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(token: String)
  ```

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
  <td><code> </code><em><code>token</code></em><code> </code></td>
  <td><div>
  <p>SDK project scope token to be used for authentication</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11VenueEngineC7destroyyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-destroy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venueengine#sdk-for-ios-explore-s-7heresdk11VenueEngineC7destroyyyF" class="token"><code>destroy()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Releases all internally used resources. The instance can’t be used anymore after calling this method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func destroy()
  ```

  </div>

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


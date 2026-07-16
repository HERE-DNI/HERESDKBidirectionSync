---
title: "SDKNativeEngine Class Reference"
slug: "sdk-for-ios-explore-classes-sdknativeengine"
---

# SDKNativeEngine

<div class="declaration">

<div class="language">

``` highlight
public class SDKNativeEngine
```

``` highlight
extension SDKNativeEngine: NativeBase
```

``` highlight
extension SDKNativeEngine: Hashable
```

</div>

</div>

Holds internal services and configurations needed by various HERE SDK modules.

You can initialize the HERE SDK in two ways:

- Create a shared instance of the `SDKNativeEngine` with

      SDKNativeEngine.makeSharedInstance()

  .

- Create individual instances of the `SDKNativeEngine` via

      SDKNativeEngine()

  . Note that this does not automatically set a shared instance.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC7optionsAcA10SDKOptionsV_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC7optionsAcA10SDKOptionsV_tKcfc" class="token"><code>init(options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes a new instance of SDKNativeEngine using supplied options.

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
  public init(options: SDKOptions) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>

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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options for the new engine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC7optionsAA10SDKOptionsVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC7optionsAA10SDKOptionsVvp" class="token"><code>options</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used by this instance of `SDKNativeEngine`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var options: SDKOptions { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Variable-sharedInstance" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ" class="token"><code>sharedInstance</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine. This is automatically set as a part of the SDK initialization process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static var sharedInstance: SDKNativeEngine? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13isOfflineModeSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isOfflineMode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13isOfflineModeSbvp" class="token"><code>isOfflineMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The offline mode. Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">`SDKNativeEngine.passThroughFeatures`</a>. Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV11offlineModeSbvp">`SDKOptions.offlineMode`</a>. Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isOfflineMode: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-passThroughFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp" class="token"><code>passThroughFeatures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The pass through features. Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a> will be enabled when at least one pass-through feature is set.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var passThroughFeatures: Set<PassThroughFeature>? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-passthroughfeature">PassThroughFeature</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Variable-parameterConfig" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ" class="token"><code>parameterConfig</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration for default values of parameters used in the HERE SDK. **Note:** This feature is in beta state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static var parameterConfig: ParameterConfiguration { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-parameterconfiguration">ParameterConfiguration</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13proxySettingsAA05ProxyE0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-proxySettings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13proxySettingsAA05ProxyE0VSgvp" class="token"><code>proxySettings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy settings of this SDK engine that will be used by HERE SDK network for all requests. Defaults to (`nil`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`nil`) to indicate that proxy should be disabled. If proxy is necessary from the start then it’s recommended to use <a href="sdk-for-ios-explore-structs-networksettings#sdk-for-ios-explore-s-7heresdk15NetworkSettingsV05proxyC0AA05ProxyC0VSgvp">`NetworkSettings.proxySettings`</a> in <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp">`SDKOptions.networkSettings`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var proxySettings: ProxySettings? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-proxysettings">ProxySettings</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13sdkUsageStatsSayAA0eF0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sdkUsageStats" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13sdkUsageStatsSayAA0eF0VGvp" class="token"><code>sdkUsageStats</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a list of usage statistics for all available HERE SDK features. <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a> has cache and persistent storage. Reads from the persistent storage happen on `SDKNativeEngine` creation step. Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sdkUsageStats: [UsageStats] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-usagestats">UsageStats</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19PurgeMemoryStrategyO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-PurgeMemoryStrategy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19PurgeMemoryStrategyO" class="token"><code>PurgeMemoryStrategy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enum representing a strategy to flush memory caches.

  <a href="sdk-for-ios-explore-classes-sdknativeengine-purgememorystrategy" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PurgeMemoryStrategy : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC18setAccessKeySecret06accessfG0ySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setAccessKeySecret-accessKeySecret" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC18setAccessKeySecret06accessfG0ySS_tF" class="token"><code>setAccessKeySecret(accessKeySecret:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Overrides HERE SDK access key secret with new value. The new credentials will be used for new requests.

  **Note:** This method can be called from any thread. Access key ID can be set with constructor of SDKNativeEngine. New instance of SDKNativeEngine should be used if a new access key ID is required.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setAccessKeySecret(accessKeySecret: String)
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
  <td><code> </code><em><code>accessKeySecret</code></em><code> </code></td>
  <td><div>
  <p>New access key secret.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC14setAccessScope5scopeySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setAccessScope-scope" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC14setAccessScope5scopeySS_tF" class="token"><code>setAccessScope(scope:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Overrides the token scope of the HERE SDK with new value. A new token will be fetched with the set scope and used for future requests. Setting an empty string will fetch a token for the global scope.

  This method can be called from any thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setAccessScope(scope: String)
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
  <td><code> </code><em><code>scope</code></em><code> </code></td>
  <td><div>
  <p>New scope for token</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC16enableUsageStats7enabledySb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-enableUsageStats-enabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC16enableUsageStats7enabledySb_tF" class="token"><code>enableUsageStats(enabled:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enable or disable <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a> for the HERE SDK. Defaults to disabled (false). When enabled,

      SDKNativeEngine.getSdkUsageStats()

  returns actual online data consumption. Note that the flag does not cancel pending requests. <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a> can be enabled or disabled at any time.
  </p>

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func enableUsageStats(enabled: Bool)
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
  <td><code> </code><em><code>enabled</code></em><code> </code></td>
  <td><div>
  <p>True, if UsageStats are enabled.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC18makeSharedInstance7optionsyAA10SDKOptionsV_tKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-makeSharedInstance-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC18makeSharedInstance7optionsyAA10SDKOptionsV_tKFZ" class="token"><code>makeSharedInstance(options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance see <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ">`SDKNativeEngine.sharedInstance`</a>. If there was previously shared instance then it’s destroyed before new instance is created.

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
  public static func makeSharedInstance(options: SDKOptions) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>

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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options for the new engine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC25clearPersistentUsageStatsyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-clearPersistentUsageStats" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC25clearPersistentUsageStatsyyF" class="token"><code>clearPersistentUsageStats()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Clear persistent storage for the HERE SDK <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a>. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearPersistentUsageStats()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC20clearUsageStatsCacheyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-clearUsageStatsCache" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC20clearUsageStatsCacheyyF" class="token"><code>clearUsageStatsCache()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Clear cache for the HERE SDK <a href="sdk-for-ios-explore-structs-usagestats">`UsageStats`</a>. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearUsageStatsCache()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC17purgeMemoryCaches8strategyyAC05PurgeE8StrategyO_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-purgeMemoryCaches-strategy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC17purgeMemoryCaches8strategyyAC05PurgeE8StrategyO_tF" class="token"><code>purgeMemoryCaches(strategy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Releases memory occupied by internal caches. Purging caches reduces memory footprint of application and may temporary reduce performance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func purgeMemoryCaches(strategy: SDKNativeEngine.PurgeMemoryStrategy)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine-purgememorystrategy">PurgeMemoryStrategy</a>

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
  <td><code> </code><em><code>strategy</code></em><code> </code></td>
  <td><div>
  <p>Option to control how much memory caches will be purged.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC11getDeviceId10completionyySSc_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getDeviceId-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC11getDeviceId10completionyySSc_tF" class="token"><code>getDeviceId(completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique identifier assigned to the device for this application. This device ID is primarily used for tracking Monthly Active Users (MAUs).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDeviceId(completion: @escaping DeviceIdHandle)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk14DeviceIdHandlea">DeviceIdHandle</a>

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
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


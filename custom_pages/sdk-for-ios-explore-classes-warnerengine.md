---
title: "WarnerEngine Class Reference"
slug: "sdk-for-ios-explore-classes-warnerengine"
---

# WarnerEngine

<div class="declaration">

<div class="language">

``` highlight
public class WarnerEngine : ElectronicHorizonDelegate
```

``` highlight
extension WarnerEngine: NativeBase
```

``` highlight
extension WarnerEngine: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a>

</div>

Provides the core functionality for generating and managing navigation warnings.

`WarnerEngine` processes Electronic Horizon data and determines when various types of warnings should be issued. It is used with <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a>, which supply the road topology and positional updates required for warning evaluation.

The engine monitors enabled warning types and notifies registered listeners when new warnings become available.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC15enabledWarningsACSayAA11WarningTypeOG_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-enabledWarnings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC15enabledWarningsACSayAA11WarningTypeOG_tKcfc" class="token"><code>init(enabledWarnings:</code><wbr></wbr><code>)</code></a> 

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
  public init(enabledWarnings: [WarningType]) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <td><code> </code><em><code>enabledWarnings</code></em><code> </code></td>
  <td><div>
  <p>The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC03sdkC015enabledWarningsAcA09SDKNativeC0C_SayAA11WarningTypeOGtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine-enabledWarnings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC03sdkC015enabledWarningsAcA09SDKNativeC0C_SayAA11WarningTypeOGtKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>enabledWarnings:</code><wbr></wbr><code>)</code></a> 

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
  public init(sdkEngine: SDKNativeEngine, enabledWarnings: [WarningType]) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <p>A <code>SDKEngine</code> instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>enabledWarnings</code></em><code> </code></td>
  <td><div>
  <p>The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC03sdkC09wallClock15enabledWarningsAcA09SDKNativeC0C_AA04WallF0_pSayAA11WarningTypeOGtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine-wallClock-enabledWarnings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC03sdkC09wallClock15enabledWarningsAcA09SDKNativeC0C_AA04WallF0_pSayAA11WarningTypeOGtKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>wallClock:</code><wbr></wbr><code>enabledWarnings:</code><wbr></wbr><code>)</code></a> 

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
  public init(sdkEngine: SDKNativeEngine, wallClock: WallClock, enabledWarnings: [WarningType]) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-protocols-wallclock">WallClock</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <p>A <code>SDKEngine</code> instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>wallClock</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-explore-protocols-wallclock"><code>WallClock</code></a> instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>enabledWarnings</code></em><code> </code></td>
  <td><div>
  <p>The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-warningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp" class="token"><code>warningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options that define warning behavior for all the warners. Provides configuration parameters for all the warners.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var warningOptions: WarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-warningoptions">WarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC13timingProfileAA06TimingE0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timingProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC13timingProfileAA06TimingE0Ovp" class="token"><code>timingProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The timing profile that defines when navigation warnings should be triggered. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected <a href="sdk-for-ios-explore-enums-timingprofile">`TimingProfile`</a> and may adjust automatically according to the current speed limit:

  - For <a href="sdk-for-ios-explore-enums-timingprofile#sdk-for-ios-explore-s-7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a>, thresholds apply when the current speed limit is above 100 km/h (62 mph).
  - For <a href="sdk-for-ios-explore-enums-timingprofile#sdk-for-ios-explore-s-7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a>, thresholds apply when the current speed limit is above 60 km/h (37 mph).
  - For <a href="sdk-for-ios-explore-enums-timingprofile#sdk-for-ios-explore-s-7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a>, thresholds apply when the current speed limit is 60 km/h (37 mph) or below.

  **Note:** Custom threshold values can be set, but these timing-profile rules will still apply.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timingProfile: TimingProfile { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC26onElectronicHorizonUpdated9errorCode6updateyAA0ef5ErrorI0OSg_AA0eF6UpdateVSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onElectronicHorizonUpdated-errorCode-update" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC26onElectronicHorizonUpdated9errorCode6updateyAA0ef5ErrorI0OSg_AA0eF6UpdateVSgtF" class="token"><code>onElectronicHorizonUpdated(errorCode:</code><wbr></wbr><code>update:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called whenever the electronic horizon subsystem produces:

  - a new update,
  - an error,

  The client must inspect `error_code` to determine whether the call represents an error or a valid update.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onElectronicHorizonUpdated(errorCode: ElectronicHorizonErrorCode?, update: ElectronicHorizonUpdate?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonupdate">ElectronicHorizonUpdate</a>

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
  <td><code> </code><em><code>errorCode</code></em><code> </code></td>
  <td><div>
  <p>The error associated with the horizon computation. <code>nil</code> means no error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>update</code></em><code> </code></td>
  <td><div>
  <p>The update describing the current electronic horizon state. May be <code>nil</code> if an update could not be produced.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC18addEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addEnabledWarnings-warningTypes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC18addEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF" class="token"><code>addEnabledWarnings(warningTypes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds the given warning types to the set of warnings monitored by the engine.

  After this call, the engine will begin generating warnings for all types included in

      WarnerEngine.addEnabledWarnings(...).warningTypes

  , in addition to those that are already enabled.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addEnabledWarnings(warningTypes: [WarningType])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <td><code> </code><em><code>warningTypes</code></em><code> </code></td>
  <td><div>
  <p>Warning types to be added to the engine’s active monitoring set.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC21removeEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeEnabledWarnings-warningTypes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC21removeEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF" class="token"><code>removeEnabledWarnings(warningTypes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes the given warning types from the set of warnings monitored by the engine.

  After this call, the engine will stop generating warnings for all types included in

      WarnerEngine.removeEnabledWarnings(...).warningTypes

  , while other enabled types remain unaffected.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeEnabledWarnings(warningTypes: [WarningType])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <td><code> </code><em><code>warningTypes</code></em><code> </code></td>
  <td><div>
  <p>Warning types to be removed from the engine’s active monitoring set.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC18setEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setEnabledWarnings-warningTypes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC18setEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF" class="token"><code>setEnabledWarnings(warningTypes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces the current set of enabled warning types with the provided list.

  After this call, the engine will monitor and generate warnings only for types included in

      WarnerEngine.setEnabledWarnings(...).warningTypes

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setEnabledWarnings(warningTypes: [WarningType])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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
  <td><code> </code><em><code>warningTypes</code></em><code> </code></td>
  <td><div>
  <p>The complete new set of warning types the engine should track.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC18getEnabledWarningsSayAA11WarningTypeOGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getEnabledWarnings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC18getEnabledWarningsSayAA11WarningTypeOGyF" class="token"><code>getEnabledWarnings()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the current list of enabled warning types. If the WarnerEngine was retrieved from the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a>, it will also contain all the warnings enabled for which listeners are set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getEnabledWarnings() -> [WarningType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

  </div>

  <div>

  #### Return Value

  The currect list instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC18addWarningDelegateyyAA0eF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addWarningDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC18addWarningDelegateyyAA0eF0_pF" class="token"><code>addWarningDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Registers a listener that will receive warning notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addWarningDelegate(_ warningListener: WarningDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-warningdelegate">WarningDelegate</a>

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
  <td><code> </code><em><code>warningListener</code></em><code> </code></td>
  <td><div>
  <p>The listener instance that should be notified when new warnings are generated.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC21removeWarningDelegateyyAA0eF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeWarningDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC21removeWarningDelegateyyAA0eF0_pF" class="token"><code>removeWarningDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unregisters a previously added warning listener.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeWarningDelegate(_ warningListener: WarningDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-warningdelegate">WarningDelegate</a>

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
  <td><code> </code><em><code>warningListener</code></em><code> </code></td>
  <td><div>
  <p>The listener instance that should no longer receive warning notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC19getWarningsRegistryAA0eF0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getWarningsRegistry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC19getWarningsRegistryAA0eF0CyF" class="token"><code>getWarningsRegistry()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.). <a href="sdk-for-ios-explore-classes-warningsregistry">`WarningsRegistry`</a> class exposes getter methods, each returning the detailed warning object for the given identifier. Use this getter to look up complete warning information by its id, as provided through `WarningListener.onWarning`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getWarningsRegistry() -> WarningsRegistry
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-warningsregistry">WarningsRegistry</a>

  </div>

  <div>

  #### Return Value

  The centralized <a href="sdk-for-ios-explore-classes-warningsregistry">`WarningsRegistry`</a> instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getWarningNotificationDistances-warningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF" class="token"><code>getWarningNotificationDistances(warningType:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the warning notification distances for the requested warning type.

  **Note**: <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF">`WarningType.custom`</a> is not a valid value for this method. Use <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF">`WarnerEngine.getCustomWarningNotificationDistances(...)`</a> to retrieve distances for a specific custom warning type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getWarningNotificationDistances(warningType: WarningType) -> WarningNotificationDistances
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>warningType</code></em><code> </code></td>
  <td><div>
  <p>The warning type for which the notification distances will be returned. Must not be <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF"><code>WarningType.custom</code></a>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The warning notification distances for the given

      WarnerEngine.getWarningNotificationDistances(...).warningType

  . If
      WarnerEngine.getWarningNotificationDistances(...).warningType

  is <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF">`WarningType.custom`</a>, a default <a href="sdk-for-ios-explore-structs-warningnotificationdistances">`WarningNotificationDistances`</a> value is returned.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setWarningNotificationDistances-warningType-warningNotificationDistances" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF" class="token"><code>setWarningNotificationDistances(warningType:</code><wbr></wbr><code>warningNotificationDistances:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the warning notification distances for the specified warning type.

  **Note**: <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF">`WarningType.custom`</a> is not a valid value for this method. Use <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF">`WarnerEngine.setCustomWarningNotificationDistances(...)`</a> to configure distances for a specific custom warning type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setWarningNotificationDistances(warningType: WarningType, warningNotificationDistances: WarningNotificationDistances) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>warningType</code></em><code> </code></td>
  <td><div>
  <p>The warning type for which the warning notification distances will be set. Must not be <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF"><code>WarningType.custom</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>warningNotificationDistances</code></em><code> </code></td>
  <td><div>
  <p>The warning notification distances to be set for the specified warning type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  True if the distances were successfully set; false if

      WarnerEngine.setWarningNotificationDistances(...).warningType

  is <a href="sdk-for-ios-explore-enums-warningtype#sdk-for-ios-explore-s-7heresdk11WarningTypeO6customyA2CmF">`WarningType.custom`</a> or the options could not be applied.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getCustomWarningNotificationDistances-customWarningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF" class="token"><code>getCustomWarningNotificationDistances(customWarningType:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the warning notification distances for the specified custom warning type.

  Unlike <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF">`WarnerEngine.getWarningNotificationDistances(...)`</a>, which operates on a <a href="sdk-for-ios-explore-enums-warningtype">`WarningType`</a>, this method targets a specific custom warning category identified by

      WarnerEngine.getCustomWarningNotificationDistances(...).customWarningType

  , as defined in <a href="sdk-for-ios-explore-structs-customwarning#sdk-for-ios-explore-s-7heresdk13CustomWarningV06customC4Types5Int32Vvp">`CustomWarning.customWarningType`</a> and <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV06customB4Types5Int32VSgvp">`Warning.customWarningType`</a>.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCustomWarningNotificationDistances(customWarningType: Int32) -> WarningNotificationDistances
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>customWarningType</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the custom warning type for which the notification distances are requested.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The warning notification distances configured for the given

      WarnerEngine.getCustomWarningNotificationDistances(...).customWarningType

  . If no distances have been explicitly set for this type, a default <a href="sdk-for-ios-explore-structs-warningnotificationdistances">`WarningNotificationDistances`</a> value is returned.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomWarningNotificationDistances-customWarningType-warningNotificationDistances" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF" class="token"><code>setCustomWarningNotificationDistances(customWarningType:</code><wbr></wbr><code>warningNotificationDistances:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the warning notification distances for the specified custom warning type.

  Unlike <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF">`WarnerEngine.setWarningNotificationDistances(...)`</a>, which applies settings to a <a href="sdk-for-ios-explore-enums-warningtype">`WarningType`</a>, this method allows configuring notification distances independently for each custom warning category identified by

      WarnerEngine.setCustomWarningNotificationDistances(...).customWarningType

  , as defined in <a href="sdk-for-ios-explore-structs-customwarning#sdk-for-ios-explore-s-7heresdk13CustomWarningV06customC4Types5Int32Vvp">`CustomWarning.customWarningType`</a> and <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV06customB4Types5Int32VSgvp">`Warning.customWarningType`</a>.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomWarningNotificationDistances(customWarningType: Int32, warningNotificationDistances: WarningNotificationDistances) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>customWarningType</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the custom warning type for which the notification distances should be set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>warningNotificationDistances</code></em><code> </code></td>
  <td><div>
  <p>The warning notification distances to be applied for the specified</p>
  <pre><code>WarnerEngine.setCustomWarningNotificationDistances(...).customWarningType</code></pre>
  .
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  True if the distances were successfully set; false otherwise.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC21finalizeGivenWarningsyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-finalizeGivenWarnings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC21finalizeGivenWarningsyyF" class="token"><code>finalizeGivenWarnings()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Marks all currently active warnings as passed (`DistanceType.PASSED`), notifies all registered <a href="sdk-for-ios-explore-protocols-warningdelegate">`WarningDelegate`</a> instances on the main thread, and then clears these warnings from their corresponding registries by invoking the appropriate`WarningsRegistry.clear<Type>` methods.

  This method triggers notifications only for enabled warners. Warning processing may occur asynchronously unless synchronous mode is enabled.

  **Note**: Although each warning type can also be cleared manually via the respective

      WarningsRegistry.clear<Type>()

  methods,
      finalizeGivenWarnings()

  provides a unified way to flush all active warnings after they have been reported as passed. If this method is not invoked, warnings will continue to accumulate in the registry according to the configured warning-generation options.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func finalizeGivenWarnings()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC24addCustomWarningProvider06customfG024segmentDataLoaderOptionsyAA0efG0_p_AA07SegmentjkL0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addCustomWarningProvider-customWarningProvider-segmentDataLoaderOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC24addCustomWarningProvider06customfG024segmentDataLoaderOptionsyAA0efG0_p_AA07SegmentjkL0VtF" class="token"><code>addCustomWarningProvider(customWarningProvider:</code><wbr></wbr><code>segmentDataLoaderOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Registers a custom warning provider.

  The registered provider participates in warning evaluation and is invoked to generate custom warnings based on the current vehicle position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addCustomWarningProvider(customWarningProvider: CustomWarningProvider, segmentDataLoaderOptions: SegmentDataLoaderOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-customwarningprovider">CustomWarningProvider</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>

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
  <td><code> </code><em><code>customWarningProvider</code></em><code> </code></td>
  <td><div>
  <p>A provider responsible for generating custom warnings.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>segmentDataLoaderOptions</code></em><code> </code></td>
  <td><div>
  <p>Specifies which data should be loaded by the <a href="sdk-for-ios-explore-classes-segmentdataloader"><code>SegmentDataLoader</code></a>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC27removeCustomWarningProvider06customfG0yAA0efG0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeCustomWarningProvider-customWarningProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC27removeCustomWarningProvider06customfG0yAA0efG0_p_tF" class="token"><code>removeCustomWarningProvider(customWarningProvider:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unregisters a custom warning provider.

  After removal, the provider will no longer participate in warning evaluation and will not generate custom warnings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeCustomWarningProvider(customWarningProvider: CustomWarningProvider)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-customwarningprovider">CustomWarningProvider</a>

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
  <td><code> </code><em><code>customWarningProvider</code></em><code> </code></td>
  <td><div>
  <p>The provider to be removed.</p>
  <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12WarnerEngineC27clearCustomWarningProvidersyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-clearCustomWarningProviders" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-warnerengine#sdk-for-ios-explore-s-7heresdk12WarnerEngineC27clearCustomWarningProvidersyyF" class="token"><code>clearCustomWarningProviders()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unregisters all custom warning providers.

  After this call, no custom warning providers will participate in warning evaluation until new providers are registered.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearCustomWarningProviders()
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


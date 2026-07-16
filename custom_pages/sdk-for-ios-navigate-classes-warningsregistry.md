---
title: "WarningsRegistry Class Reference"
slug: "sdk-for-ios-navigate-classes-warningsregistry"
---

# WarningsRegistry

<div class="declaration">

<div class="language">

``` highlight
public class WarningsRegistry
```

``` highlight
extension WarningsRegistry: NativeBase
```

``` highlight
extension WarningsRegistry: Hashable
```

</div>

</div>

A class that store warning metadata for different warning types. Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.). Provided by <a href="sdk-for-ios-navigate-classes-warnerengine">`WarnerEngine`</a> so callers can lookup detailed information about specific warnings.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getSafetyCameraWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getSafetyCameraWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getSafetyCameraWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getSafetyCameraWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a safety-camera warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSafetyCameraWarning(warning: Warning) -> SafetyCameraWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-safetycamerawarning">SafetyCameraWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single safety-camera warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-safetycamerawarning">`SafetyCameraWarning`</a> object associated with the provided

      WarningsRegistry.getSafetyCameraWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getSafetyCameraWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC26getTruckRestrictionWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getTruckRestrictionWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC26getTruckRestrictionWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getTruckRestrictionWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a truck restrictions warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getTruckRestrictionWarning(warning: Warning) -> TruckRestrictionWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-truckrestrictionwarning">TruckRestrictionWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single truck restrictions warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-truckrestrictionwarning">`TruckRestrictionWarning`</a> object associated with the provided

      WarningsRegistry.getTruckRestrictionWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getTruckRestrictionWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC18getRoadSignWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getRoadSignWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC18getRoadSignWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getRoadSignWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a road-sign warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getRoadSignWarning(warning: Warning) -> RoadSignWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-roadsignwarning">RoadSignWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single road sign warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `sdk.navigation.RoadSignWarning` object associated with the provided

      WarningsRegistry.getRoadSignWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getRoadSignWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC23getRealisticViewWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getRealisticViewWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC23getRealisticViewWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getRealisticViewWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a realistic-view warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getRealisticViewWarning(warning: Warning) -> RealisticViewWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-realisticviewwarning">RealisticViewWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single realistic-view warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-realisticviewwarning">`RealisticViewWarning`</a> object associated with the provided

      WarningsRegistry.getRealisticViewWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getRealisticViewWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC27getEnvironmentalZoneWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getEnvironmentalZoneWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC27getEnvironmentalZoneWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getEnvironmentalZoneWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns environmental zone warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getEnvironmentalZoneWarning(warning: Warning) -> EnvironmentalZoneWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-environmentalzonewarning">EnvironmentalZoneWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single environmental zone warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-environmentalzonewarning">`EnvironmentalZoneWarning`</a> object associated with the provided

      WarningsRegistry.getEnvironmentalZoneWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getEnvironmentalZoneWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC20getSchoolZoneWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getSchoolZoneWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC20getSchoolZoneWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getSchoolZoneWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a school zone warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSchoolZoneWarning(warning: Warning) -> SchoolZoneWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-schoolzonewarning">SchoolZoneWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single school zone warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-schoolzonewarning">`SchoolZoneWarning`</a> object associated with the provided

      WarningsRegistry.getSchoolZoneWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getSchoolZoneWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC18getTollStopWarning7warningAA0eF0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getTollStopWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC18getTollStopWarning7warningAA0eF0VSgAA0G0V_tF" class="token"><code>getTollStopWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a toll stop warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getTollStopWarning(warning: Warning) -> TollStop?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-tollstop">TollStop</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single toll stop warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-tollstop">`TollStop`</a> object associated with the provided

      WarningsRegistry.getTollStopWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getTollStopWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC20getDangerZoneWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getDangerZoneWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC20getDangerZoneWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getDangerZoneWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a danger zone warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDangerZoneWarning(warning: Warning) -> DangerZoneWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-dangerzonewarning">DangerZoneWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single danger zone warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-dangerzonewarning">`DangerZoneWarning`</a> object associated with the provided

      WarningsRegistry.getDangerZoneWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getDangerZoneWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC24getBorderCrossingWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getBorderCrossingWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC24getBorderCrossingWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getBorderCrossingWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a border crossing warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBorderCrossingWarning(warning: Warning) -> BorderCrossingWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">BorderCrossingWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single border crossing warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">`BorderCrossingWarning`</a> object associated with the provided

      WarningsRegistry.getBorderCrossingWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getBorderCrossingWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC25getRailwayCrossingWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getRailwayCrossingWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC25getRailwayCrossingWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getRailwayCrossingWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a railway crossing warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getRailwayCrossingWarning(warning: Warning) -> RailwayCrossingWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-railwaycrossingwarning">RailwayCrossingWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single railway crossing warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-railwaycrossingwarning">`RailwayCrossingWarning`</a> object associated with the provided

      WarningsRegistry.getRailwayCrossingWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getRailwayCrossingWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getLowSpeedZoneWarning7warningAA0efgH0VSgAA0H0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getLowSpeedZoneWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getLowSpeedZoneWarning7warningAA0efgH0VSgAA0H0V_tF" class="token"><code>getLowSpeedZoneWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a low speed zone warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getLowSpeedZoneWarning(warning: Warning) -> LowSpeedZoneWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-lowspeedzonewarning">LowSpeedZoneWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single low speed zone warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-lowspeedzonewarning">`LowSpeedZoneWarning`</a> object associated with the provided

      WarningsRegistry.getLowSpeedZoneWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getLowSpeedZoneWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getTrafficMergeWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getTrafficMergeWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getTrafficMergeWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getTrafficMergeWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a traffic merge warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getTrafficMergeWarning(warning: Warning) -> TrafficMergeWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-trafficmergewarning">TrafficMergeWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single traffic merge warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `sdk.navigation.TrafficMergeWarning` object associated with the provided

      WarningsRegistry.getTrafficMergeWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getTrafficMergeWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getLaneDecreaseWarning7warningAA0efG0VSgAA0G0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getLaneDecreaseWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC22getLaneDecreaseWarning7warningAA0efG0VSgAA0G0V_tF" class="token"><code>getLaneDecreaseWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a lane decrease warning corresponding to the given identifier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getLaneDecreaseWarning(warning: Warning) -> LaneDecreaseWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-lanedecreasewarning">LaneDecreaseWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>. The <code>warning</code> uniquely identifies a single lane decrease warning within this registry and is used to retrieve its full metadata.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-lanedecreasewarning">`LaneDecreaseWarning`</a> object associated with the provided

      WarningsRegistry.getLaneDecreaseWarning(...).warning

  , or `nil` if no warning exists for the given
      WarningsRegistry.getLaneDecreaseWarning(...).warning

  . This object contains the full details and attributes of the corresponding warning.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC16getCustomWarning7warningAA0eF0VSgAA0F0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getCustomWarning-warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-warningsregistry#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC16getCustomWarning7warningAA0eF0VSgAA0F0V_tF" class="token"><code>getCustomWarning(warning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns additional data associated with the given custom warning.

  The provided

      WarningsRegistry.getCustomWarning(...).warning

  identifies a specific custom warning instance by its base warning information and custom warning type. This information is used to resolve the corresponding entry in the warning registry and retrieve any additional, type-specific data associated with the warning.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCustomWarning(warning: Warning) -> CustomWarning?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-warning">Warning</a>
  - <a href="sdk-for-ios-navigate-structs-customwarning">CustomWarning</a>

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
  <td><code> </code><em><code>warning</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-structs-warning"><code>Warning</code></a> instance identifying the custom warning for which additional data should be retrieved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-customwarning">`CustomWarning`</a> associated with the given

      WarningsRegistry.getCustomWarning(...).warning

  , or `nil` if no additional data exists for this warning. The returned object contains the payload with type-specific details and attributes of the corresponding warning.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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


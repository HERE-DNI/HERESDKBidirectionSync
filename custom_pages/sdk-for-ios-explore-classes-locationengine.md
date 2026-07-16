---
title: "LocationEngine Class Reference"
slug: "sdk-for-ios-explore-classes-locationengine"
---

# LocationEngine

<div class="declaration">

<div class="language">

``` highlight
public class LocationEngine : LocationEngineBase
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-locationenginebase">LocationEngineBase</a>

</div>

This class handles location updates received according to the desired LocationAccuracy. Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one LocationEngine can be started at a time. Multiple delegates can be attached, either to receive location updates, see LocationUpdateDelegate, or status updates, see LocationStatusDelegate. When a different LocationAccuracy is desired, the LocationEngine needs to be stopped and started again.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP9isStartedSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isStarted" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP9isStartedSbvp" class="token"><code>isStarted</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) var isStarted: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public convenience init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC03sdkC0AcA09SDKNativeC0C_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC03sdkC0AcA09SDKNativeC0C_tKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC5start16locationAccuracyAA0bC6StatusOAA0bF0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-locationAccuracy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC5start16locationAccuracyAA0bC6StatusOAA0bF0O_tF" class="token"><code>start(locationAccuracy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts the location engine with desired LocationAccuracy.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(locationAccuracy: LocationAccuracy) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationaccuracy">LocationAccuracy</a>
  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>locationAccuracy</code></em><code> </code></td>
  <td><div>
  <p>Determines desired location accuracy.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Location engine status.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC5start15locationOptionsAA0bC6StatusOAA0bF0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-locationOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC5start15locationOptionsAA0bC6StatusOAA0bF0V_tF" class="token"><code>start(locationOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts the location engine with desired LocationOptions. This method variant is not currently supported on iOS platforms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(locationOptions: LocationOptions) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>locationOptions</code></em><code> </code></td>
  <td><div>
  <p>Determines desired location options.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  LocationEngineStatus.notSupported.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC06updateB8Accuracy08locationE0AA0bC6StatusOAA0bE0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-updateLocationAccuracy-locationAccuracy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC06updateB8Accuracy08locationE0AA0bC6StatusOAA0bE0O_tF" class="token"><code>updateLocationAccuracy(locationAccuracy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired LocationAccuracy. This method is a faster way to change location accuracy for already started location engine, than calling <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC4stopyyF">`stop(...)`</a> and

      start(LocationOptions)

  in sequence. Returns <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO8notReadyyA2CmF">`LocationEngineStatus.notReady`</a>, if called for unstarted location engine.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocationAccuracy(locationAccuracy: LocationAccuracy) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationaccuracy">LocationAccuracy</a>
  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>locationAccuracy</code></em><code> </code></td>
  <td><div>
  <p>Desired location accuracy. Requested accuracy is not guaranteed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Engine status. Valid values are defined in <a href="sdk-for-ios-explore-enums-locationenginestatus">`LocationEngineStatus`</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC06updateB7Options08locationE0AA0bC6StatusOAA0bE0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-updateLocationOptions-locationOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC06updateB7Options08locationE0AA0bC6StatusOAA0bE0V_tF" class="token"><code>updateLocationOptions(locationOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired LocationOptions. This method is a faster way to change location options for already started location engine, than calling <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC4stopyyF">`stop(...)`</a> and

      start(LocationOptions)

  in sequence. Returns <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO8notReadyyA2CmF">`LocationEngineStatus.notReady`</a>, if called for unstarted location engine. This method variant is not currently supported on iOS platforms. Returns <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which this method variant is not supported.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocationOptions(locationOptions: LocationOptions) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>locationOptions</code></em><code> </code></td>
  <td><div>
  <p>Desired location options.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Engine status. Valid values are defined in <a href="sdk-for-ios-explore-enums-locationenginestatus">`LocationEngineStatus`</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastKnownLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp" class="token"><code>lastKnownLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the last known location obtained by the engine. Location is returned synchronously. Location object has timestamp attribute, which reflects when data was obtained. If location was never obtained - nil is returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastKnownLocation: Location? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC4stopyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-stop" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC4stopyyF" class="token"><code>stop()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops the location engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stop()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC33confirmHEREPrivacyNoticeInclusionAA18ConfirmationStatusOyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-confirmHEREPrivacyNoticeInclusion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC33confirmHEREPrivacyNoticeInclusionAA18ConfirmationStatusOyF" class="token"><code>confirmHEREPrivacyNoticeInclusion()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method does nothing on iOS platforms. Returns <a href="sdk-for-ios-explore-enums-confirmationstatus#sdk-for-ios-explore-s-7heresdk18ConfirmationStatusO2okyA2CmF">`ConfirmationStatus.ok`</a> on this platform.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func confirmHEREPrivacyNoticeInclusion() -> ConfirmationStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-confirmationstatus">ConfirmationStatus</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC33confirmHEREPrivacyNoticeExceptionAA18ConfirmationStatusOyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-confirmHEREPrivacyNoticeException" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC33confirmHEREPrivacyNoticeExceptionAA18ConfirmationStatusOyF" class="token"><code>confirmHEREPrivacyNoticeException()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method does nothing on iOS platforms. Returns <a href="sdk-for-ios-explore-enums-confirmationstatus#sdk-for-ios-explore-s-7heresdk18ConfirmationStatusO2okyA2CmF">`ConfirmationStatus.ok`</a> on this platform.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func confirmHEREPrivacyNoticeException() -> ConfirmationStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-confirmationstatus">ConfirmationStatus</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC03addB8Delegate08locationE0yAA0bE0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addLocationDelegate-locationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC03addB8Delegate08locationE0yAA0bE0_p_tF" class="token"><code>addLocationDelegate(locationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a LocationDelegate to the engine to get notified when there is a new location update available. Supports more than one delegate, instance is added only once.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addLocationDelegate(locationDelegate: LocationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC06removeB8Delegate08locationE0yAA0bE0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeLocationDelegate-locationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC06removeB8Delegate08locationE0yAA0bE0_p_tF" class="token"><code>removeLocationDelegate(locationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a LocationDelegate from the engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeLocationDelegate(locationDelegate: LocationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addLocationStatusDelegate-locationStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF" class="token"><code>addLocationStatusDelegate(locationStatusDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addLocationStatusDelegate(locationStatusDelegate: LocationStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeLocationStatusDelegate-locationStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF" class="token"><code>removeLocationStatusDelegate(locationStatusDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeLocationStatusDelegate(locationStatusDelegate: LocationStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setBackgroundLocationAllowed-allowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF" class="token"><code>setBackgroundLocationAllowed(allowed:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables or disables application’s background location updates. By default background location updates are enabled if application has background location capabilities.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setBackgroundLocationAllowed(allowed: Bool) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>allowed</code></em><code> </code></td>
  <td><div>
  <p>Set to true to allow background location updates, or false to disable them.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO10notAllowedyA2CmF">`LocationEngineStatus.notAllowed`</a> if the application does not have background location capabilities enabled. <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support controlling of background location modes.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC013getBackgroundB7AllowedSbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getBackgroundLocationAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC013getBackgroundB7AllowedSbyF" class="token"><code>getBackgroundLocationAllowed()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location updates are enabled. Returns false on platforms which do not support controlling of background location modes using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">`LocationEngineBase.setBackgroundLocationAllowed(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBackgroundLocationAllowed() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  True if background location updates are allowed, false otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setBackgroundLocationIndicatorVisible-visible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF" class="token"><code>setBackgroundLocationIndicatorVisible(visible:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls visibility of application’s background location indicator. By default background location indicator is visible, if application has background location capabilities.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setBackgroundLocationIndicatorVisible(visible: Bool) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>visible</code></em><code> </code></td>
  <td><div>
  <p>Set to true to show background location indicator, or false to hide it.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO10notAllowedyA2CmF">`LocationEngineStatus.notAllowed`</a> if the application does not have background location capabilities enabled. <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support controlling of background location indicator visibility.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC013getBackgroundB16IndicatorVisibleSbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getBackgroundLocationIndicatorVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC013getBackgroundB16IndicatorVisibleSbyF" class="token"><code>getBackgroundLocationIndicatorVisible()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location indicator is visible. Returns false on platforms which do not support controlling of background location indicator using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">`LocationEngineBase.setBackgroundLocationIndicatorVisible(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBackgroundLocationIndicatorVisible() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  True if background location indicator is visible, false otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setPauseLocationUpdatesAutomatically-allowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF" class="token"><code>setPauseLocationUpdatesAutomatically(allowed:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls automatic pausing of location updates e.g. for improving device’s battery life at times when location data is unlikely to change. By default automatic pausing of location updates is allowed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setPauseLocationUpdatesAutomatically(allowed: Bool) -> LocationEngineStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

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
  <td><code> </code><em><code>allowed</code></em><code> </code></td>
  <td><div>
  <p>Set to true to allow automatic pausing of location updates, or false to disable them.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support automatic pausing of location updates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC08getPauseB20UpdatesAutomaticallySbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getPauseLocationUpdatesAutomatically" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC08getPauseB20UpdatesAutomaticallySbyF" class="token"><code>getPauseLocationUpdatesAutomatically()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if automatic pausing of location updates are enabled. Returns false on platforms which do not support controlling of automatic pausing of location updates using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">`LocationEngineBase.setPauseLocationUpdatesAutomatically(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getPauseLocationUpdatesAutomatically() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  True if automatic pausing of location updates is enabled, false otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14LocationEngineC36setCallListenerFromMainThreadEnabled7enabledySb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCallListenerFromMainThreadEnabled-enabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk14LocationEngineC36setCallListenerFromMainThreadEnabled7enabledySb_tF" class="token"><code>setCallListenerFromMainThreadEnabled(enabled:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables or disables forcing listener calls to originate from main thread. When disabled listener calls can originate from any thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCallListenerFromMainThreadEnabled(enabled: Bool)
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
  <p>Set to true to force listener calls to be called from main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16LocationDelegateP02onB7UpdatedyyAA0B0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onLocationUpdated-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk16LocationDelegateP02onB7UpdatedyyAA0B0VF" class="token"><code>onLocationUpdated(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated(_ position: Location)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22LocationStatusDelegateP02onC7Changed014locationEngineC0yAA0bhC0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onStatusChanged-locationEngineStatus" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk22LocationStatusDelegateP02onC7Changed014locationEngineC0yAA0bhC0O_tF" class="token"><code>onStatusChanged(locationEngineStatus:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onStatusChanged(locationEngineStatus: LocationEngineStatus)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22LocationStatusDelegateP22onFeaturesNotAvailable8featuresySayAA0B7FeatureOG_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onFeaturesNotAvailable-features" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-locationengine#sdk-for-ios-explore-s-7heresdk22LocationStatusDelegateP22onFeaturesNotAvailable8featuresySayAA0B7FeatureOG_tF" class="token"><code>onFeaturesNotAvailable(features:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onFeaturesNotAvailable(features: [LocationFeature])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-locationfeature">LocationFeature</a>

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


---
title: "LocationEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-locationengine"
---

# LocationEngine

<div class="declaration">

<div class="language">

``` highlight
public class LocationEngine : LocationEngineBase
```

</div>

</div>

This class handles location updates received according to the desired LocationAccuracy. Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one LocationEngine can be started at a time. Multiple delegates can be attached, either to receive location updates, see LocationUpdateDelegate, or status updates, see LocationStatusDelegate. When a different LocationAccuracy is desired, the LocationEngine needs to be stopped and started again.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18LocationEngineBaseP9isStartedSbvp"></span>` `<span id="//apple_ref/swift/Property/isStarted" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationengine#/s:7heresdk18LocationEngineBaseP9isStartedSbvp" class="token"><code>isStarted</code></a>` `

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
  public private(set) var isStarted : Bool { get }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

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

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public convenience init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(sdkEngine: )

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
  public init ( sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      start(locationAccuracy: )

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
  public func start ( locationAccuracy : LocationAccuracy ) -> LocationEngineStatus
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

      start(locationOptions: )

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
  public func start ( locationOptions : LocationOptions ) -> LocationEngineStatus
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

      updateLocationAccuracy(locationAccuracy: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired LocationAccuracy. This method is a faster way to change location accuracy for already started location engine, than calling

      stop(...)

  and
      start(LocationOptions)

  in sequence. Returns <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">`LocationEngineStatus.notReady`</a>, if called for unstarted location engine.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocationAccuracy ( locationAccuracy : LocationAccuracy ) -> LocationEngineStatus
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

  Engine status. Valid values are defined in <a href="sdk-for-ios-navigate-enums-locationenginestatus">`LocationEngineStatus`</a>

  </div>

  </div>

  </div>

- <div>

      updateLocationOptions(locationOptions: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired LocationOptions. This method is a faster way to change location options for already started location engine, than calling

      stop(...)

  and
      start(LocationOptions)

  in sequence. Returns <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">`LocationEngineStatus.notReady`</a>, if called for unstarted location engine. This method variant is not currently supported on iOS platforms. Returns <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which this method variant is not supported.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocationOptions ( locationOptions : LocationOptions ) -> LocationEngineStatus
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

  Engine status. Valid values are defined in <a href="sdk-for-ios-navigate-enums-locationenginestatus">`LocationEngineStatus`</a>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp"></span>` `<span id="//apple_ref/swift/Property/lastKnownLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationengine#/s:7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp" class="token"><code>lastKnownLocation</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

      stop()

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
  public func stop ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      confirmHEREPrivacyNoticeInclusion()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method does nothing on iOS platforms. Returns <a href="sdk-for-ios-navigate-enums-confirmationstatus#/s:7heresdk18ConfirmationStatusO2okyA2CmF">`ConfirmationStatus.ok`</a> on this platform.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func confirmHEREPrivacyNoticeInclusion () -> ConfirmationStatus
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      confirmHEREPrivacyNoticeException()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method does nothing on iOS platforms. Returns <a href="sdk-for-ios-navigate-enums-confirmationstatus#/s:7heresdk18ConfirmationStatusO2okyA2CmF">`ConfirmationStatus.ok`</a> on this platform.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func confirmHEREPrivacyNoticeException () -> ConfirmationStatus
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addLocationDelegate(locationDelegate: )

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
  public func addLocationDelegate ( locationDelegate : LocationDelegate )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      removeLocationDelegate(locationDelegate: )

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
  public func removeLocationDelegate ( locationDelegate : LocationDelegate )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addLocationStatusDelegate(locationStatusDelegate: )

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
  public func addLocationStatusDelegate ( locationStatusDelegate : LocationStatusDelegate )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      removeLocationStatusDelegate(locationStatusDelegate: )

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
  public func removeLocationStatusDelegate ( locationStatusDelegate : LocationStatusDelegate )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      setBackgroundLocationAllowed(allowed: )

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
  public func setBackgroundLocationAllowed ( allowed : Bool ) -> LocationEngineStatus
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

  <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF">`LocationEngineStatus.notAllowed`</a> if the application does not have background location capabilities enabled. <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support controlling of background location modes.

  </div>

  </div>

  </div>

- <div>

      getBackgroundLocationAllowed()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location updates are enabled. Returns false on platforms which do not support controlling of background location modes using

      LocationEngineBase.setBackgroundLocationAllowed(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBackgroundLocationAllowed () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  True if background location updates are allowed, false otherwise.

  </div>

  </div>

  </div>

- <div>

      setBackgroundLocationIndicatorVisible(visible: )

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
  public func setBackgroundLocationIndicatorVisible ( visible : Bool ) -> LocationEngineStatus
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

  <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF">`LocationEngineStatus.notAllowed`</a> if the application does not have background location capabilities enabled. <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support controlling of background location indicator visibility.

  </div>

  </div>

  </div>

- <div>

      getBackgroundLocationIndicatorVisible()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location indicator is visible. Returns false on platforms which do not support controlling of background location indicator using

      LocationEngineBase.setBackgroundLocationIndicatorVisible(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBackgroundLocationIndicatorVisible () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  True if background location indicator is visible, false otherwise.

  </div>

  </div>

  </div>

- <div>

      setPauseLocationUpdatesAutomatically(allowed: )

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
  public func setPauseLocationUpdatesAutomatically ( allowed : Bool ) -> LocationEngineStatus
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

  <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO2okyA2CmF">`LocationEngineStatus.ok`</a> if call succeeds. <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">`LocationEngineStatus.notSupported`</a> on platforms which do not support automatic pausing of location updates.

  </div>

  </div>

  </div>

- <div>

      getPauseLocationUpdatesAutomatically()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if automatic pausing of location updates are enabled. Returns false on platforms which do not support controlling of automatic pausing of location updates using

      LocationEngineBase.setPauseLocationUpdatesAutomatically(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getPauseLocationUpdatesAutomatically () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  True if automatic pausing of location updates is enabled, false otherwise.

  </div>

  </div>

  </div>

- <div>

      setCallListenerFromMainThreadEnabled(enabled: )

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
  public func setCallListenerFromMainThreadEnabled ( enabled : Bool )
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

      onLocationUpdated(_: )

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
  public func onLocationUpdated ( _ position : Location )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      onStatusChanged(locationEngineStatus: )

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
  public func onStatusChanged ( locationEngineStatus : LocationEngineStatus )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      onFeaturesNotAvailable(features: )

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
  public func onFeaturesNotAvailable ( features : [ LocationFeature ])
  ```

  </pre>

  </div>

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


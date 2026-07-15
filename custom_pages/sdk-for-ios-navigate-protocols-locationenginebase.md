---
title: "LocationEngineBase Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-locationenginebase"
---

# LocationEngineBase

<div class="declaration">

<div class="language">

``` highlight
public protocol LocationEngineBase : AnyObject
```

</div>

</div>

Public protocol that describes the behaviour of <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>. Implementation is platform-specific.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp"></span>` `<span id="//apple_ref/swift/Property/lastKnownLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-protocols-locationenginebase#/s:7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp" class="token"><code>lastKnownLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The last known location obtained by the <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>. It is persisted throughout the app’s lifecycle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var lastKnownLocation: Location? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LocationEngineBaseP9isStartedSbvp"></span>` `<span id="//apple_ref/swift/Property/isStarted" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-protocols-locationenginebase#/s:7heresdk18LocationEngineBaseP9isStartedSbvp" class="token"><code>isStarted</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Checks if the engine is in started state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var isStarted: Bool { get }
  ```

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

  Starts the location engine with desired <a href="sdk-for-ios-navigate-enums-locationaccuracy">`LocationAccuracy`</a>. Returns <a href="sdk-for-ios-navigate-enums-locationenginestatus#/s:7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF">`LocationEngineStatus.alreadyStarted`</a>, if

      start(LocationOptions)

  is called again without
      stop(...)

  in between.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func start ( locationAccuracy : LocationAccuracy ) -> LocationEngineStatus
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

      updateLocationAccuracy(locationAccuracy: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired <a href="sdk-for-ios-navigate-enums-locationaccuracy">`LocationAccuracy`</a>. This method is a faster way to change location accuracy for already started location engine, than calling

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
  func updateLocationAccuracy ( locationAccuracy : LocationAccuracy ) -> LocationEngineStatus
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
  func stop ()
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

  Adds a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a> to the engine to get notified when there is a new location update available. Supports more than one delegate, instance is added only once.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addLocationDelegate ( locationDelegate : LocationDelegate )
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
  <td><code> </code><em><code>locationDelegate</code></em><code> </code></td>
  <td><div>
  <p>The listener.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Removes a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a> from the engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeLocationDelegate ( locationDelegate : LocationDelegate )
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
  <td><code> </code><em><code>locationDelegate</code></em><code> </code></td>
  <td><div>
  <p>The listener.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Adds a <a href="sdk-for-ios-navigate-protocols-locationstatusdelegate">`LocationStatusDelegate`</a> to the engine to get notified when there is an important status change. Supports more than one delegate, instance is added only once.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addLocationStatusDelegate ( locationStatusDelegate : LocationStatusDelegate )
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
  <td><code> </code><em><code>locationStatusDelegate</code></em><code> </code></td>
  <td><div>
  <p>The listener.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Removes a <a href="sdk-for-ios-navigate-protocols-locationstatusdelegate">`LocationStatusDelegate`</a> from the engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeLocationStatusDelegate ( locationStatusDelegate : LocationStatusDelegate )
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
  <td><code> </code><em><code>locationStatusDelegate</code></em><code> </code></td>
  <td><div>
  <p>The listener.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Enables or disables background location updates for an application. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func setBackgroundLocationAllowed ( allowed : Bool ) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to allow background location updates, or <code>false</code> to disable them.</p>
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

  Check if application’s background location updates are enabled. Returns `false` on platforms which do not support controlling of background location modes using

      setBackgroundLocationAllowed(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getBackgroundLocationAllowed () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `True` if background location updates are allowed, `false` otherwise.

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
  func setBackgroundLocationIndicatorVisible ( visible : Bool ) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to show background location indicator, or <code>false</code> to hide it.</p>
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

  Check if application’s background location indicator is visible. Returns `false` on platforms which do not support controlling of background location indicator using

      setBackgroundLocationIndicatorVisible(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getBackgroundLocationIndicatorVisible () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `True` if background location indicator is visible, `false` otherwise.

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
  func setPauseLocationUpdatesAutomatically ( allowed : Bool ) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to allow automatic pausing of location updates, or <code>false</code> to disable them.</p>
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

  Check if automatic pausing of location updates are enabled. Returns `false` on platforms which do not support controlling of automatic pausing of location updates using

      setPauseLocationUpdatesAutomatically(...)

  method.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getPauseLocationUpdatesAutomatically () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `True` if automatic pausing of location updates is enabled, `false` otherwise.

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


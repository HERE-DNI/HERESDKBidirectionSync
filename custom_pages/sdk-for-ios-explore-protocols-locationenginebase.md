---
title: "LocationEngineBase Protocol Reference"
slug: "sdk-for-ios-explore-protocols-locationenginebase"
---

# LocationEngineBase

<div class="declaration">

<div class="language">

``` highlight
public protocol LocationEngineBase : AnyObject
```

</div>

</div>

Public protocol that describes the behaviour of <a href="sdk-for-ios-explore-classes-locationengine">`LocationEngine`</a>. Implementation is platform-specific.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastKnownLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp" class="token"><code>lastKnownLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The last known location obtained by the <a href="sdk-for-ios-explore-classes-locationengine">`LocationEngine`</a>. It is persisted throughout the app’s lifecycle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var lastKnownLocation: Location? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP9isStartedSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isStarted" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP9isStartedSbvp" class="token"><code>isStarted</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP5start16locationAccuracyAA0bC6StatusOAA0bG0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-locationAccuracy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP5start16locationAccuracyAA0bC6StatusOAA0bG0O_tF" class="token"><code>start(locationAccuracy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts the location engine with desired <a href="sdk-for-ios-explore-enums-locationaccuracy">`LocationAccuracy`</a>. Returns <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF">`LocationEngineStatus.alreadyStarted`</a>, if

      start(LocationOptions)

  is called again without <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP4stopyyF">`stop(...)`</a> in between.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func start(locationAccuracy: LocationAccuracy) -> LocationEngineStatus
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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06updateB8Accuracy08locationF0AA0bC6StatusOAA0bF0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-updateLocationAccuracy-locationAccuracy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06updateB8Accuracy08locationF0AA0bC6StatusOAA0bF0O_tF" class="token"><code>updateLocationAccuracy(locationAccuracy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reconfigures the location engine with desired <a href="sdk-for-ios-explore-enums-locationaccuracy">`LocationAccuracy`</a>. This method is a faster way to change location accuracy for already started location engine, than calling <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP4stopyyF">`stop(...)`</a> and

      start(LocationOptions)

  in sequence. Returns <a href="sdk-for-ios-explore-enums-locationenginestatus#sdk-for-ios-explore-s-7heresdk20LocationEngineStatusO8notReadyyA2CmF">`LocationEngineStatus.notReady`</a>, if called for unstarted location engine.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func updateLocationAccuracy(locationAccuracy: LocationAccuracy) -> LocationEngineStatus
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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP4stopyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-stop" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP4stopyyF" class="token"><code>stop()</code></a> 

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
  func stop()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB8Delegate08locationF0yAA0bF0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addLocationDelegate-locationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB8Delegate08locationF0yAA0bF0_p_tF" class="token"><code>addLocationDelegate(locationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a <a href="sdk-for-ios-explore-protocols-locationdelegate">`LocationDelegate`</a> to the engine to get notified when there is a new location update available. Supports more than one delegate, instance is added only once.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addLocationDelegate(locationDelegate: LocationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB8Delegate08locationF0yAA0bF0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeLocationDelegate-locationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB8Delegate08locationF0yAA0bF0_p_tF" class="token"><code>removeLocationDelegate(locationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a <a href="sdk-for-ios-explore-protocols-locationdelegate">`LocationDelegate`</a> from the engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeLocationDelegate(locationDelegate: LocationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addLocationStatusDelegate-locationStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF" class="token"><code>addLocationStatusDelegate(locationStatusDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">`LocationStatusDelegate`</a> to the engine to get notified when there is an important status change. Supports more than one delegate, instance is added only once.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addLocationStatusDelegate(locationStatusDelegate: LocationStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeLocationStatusDelegate-locationStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF" class="token"><code>removeLocationStatusDelegate(locationStatusDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">`LocationStatusDelegate`</a> from the engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeLocationStatusDelegate(locationStatusDelegate: LocationStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setBackgroundLocationAllowed-allowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF" class="token"><code>setBackgroundLocationAllowed(allowed:</code><wbr></wbr><code>)</code></a> 

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
  func setBackgroundLocationAllowed(allowed: Bool) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to allow background location updates, or <code>false</code> to disable them.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013getBackgroundB7AllowedSbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getBackgroundLocationAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013getBackgroundB7AllowedSbyF" class="token"><code>getBackgroundLocationAllowed()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location updates are enabled. Returns `false` on platforms which do not support controlling of background location modes using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">`setBackgroundLocationAllowed(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getBackgroundLocationAllowed() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  `True` if background location updates are allowed, `false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setBackgroundLocationIndicatorVisible-visible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF" class="token"><code>setBackgroundLocationIndicatorVisible(visible:</code><wbr></wbr><code>)</code></a> 

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
  func setBackgroundLocationIndicatorVisible(visible: Bool) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to show background location indicator, or <code>false</code> to hide it.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013getBackgroundB16IndicatorVisibleSbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getBackgroundLocationIndicatorVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013getBackgroundB16IndicatorVisibleSbyF" class="token"><code>getBackgroundLocationIndicatorVisible()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if application’s background location indicator is visible. Returns `false` on platforms which do not support controlling of background location indicator using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">`setBackgroundLocationIndicatorVisible(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getBackgroundLocationIndicatorVisible() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  `True` if background location indicator is visible, `false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setPauseLocationUpdatesAutomatically-allowed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF" class="token"><code>setPauseLocationUpdatesAutomatically(allowed:</code><wbr></wbr><code>)</code></a> 

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
  func setPauseLocationUpdatesAutomatically(allowed: Bool) -> LocationEngineStatus
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
  <p>Set to <code>true</code> to allow automatic pausing of location updates, or <code>false</code> to disable them.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08getPauseB20UpdatesAutomaticallySbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getPauseLocationUpdatesAutomatically" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08getPauseB20UpdatesAutomaticallySbyF" class="token"><code>getPauseLocationUpdatesAutomatically()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if automatic pausing of location updates are enabled. Returns `false` on platforms which do not support controlling of automatic pausing of location updates using <a href="sdk-for-ios-explore-protocols-locationenginebase#sdk-for-ios-explore-s-7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">`setPauseLocationUpdatesAutomatically(...)`</a> method.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getPauseLocationUpdatesAutomatically() -> Bool
  ```

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


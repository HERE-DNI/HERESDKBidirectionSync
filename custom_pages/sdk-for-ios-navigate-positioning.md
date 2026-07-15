---
title: "Positioning  Reference"
slug: "sdk-for-ios-navigate-positioning"
---

# Positioning

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18AuthenticationDataV"></span>` `<span id="//apple_ref/swift/Struct/AuthenticationData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk18AuthenticationDataV" class="token"><code>AuthenticationData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication data

  <a href="sdk-for-ios-navigate-structs-authenticationdata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AuthenticationData : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19AuthenticationErrorO"></span>` `<span id="//apple_ref/swift/Enum/AuthenticationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk19AuthenticationErrorO" class="token"><code>AuthenticationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication error

  <a href="sdk-for-ios-navigate-enums-authenticationerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AuthenticationError : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension AuthenticationError : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18ConfirmationStatusO"></span>` `<span id="//apple_ref/swift/Enum/ConfirmationStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk18ConfirmationStatusO" class="token"><code>ConfirmationStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Confirmation action specific status codes.

  <a href="sdk-for-ios-navigate-enums-confirmationstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ConfirmationStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16LocationAccuracyO"></span>` `<span id="//apple_ref/swift/Enum/LocationAccuracy" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk16LocationAccuracyO" class="token"><code>LocationAccuracy</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the desired location accuracy, however the actual accuracy is not guaranteed. When requesting high-accuracy locations, the initial update delivered by the LocationEngine may not have the requested accuracy. Requesting higher accuracy location updates usually means higher power consumption, therefore you should use the lowest accuracy suitable for your use case to preserve the device battery.

  <a href="sdk-for-ios-navigate-enums-locationaccuracy" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationAccuracy : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LocationEngineBaseP"></span>` `<span id="//apple_ref/swift/Protocol/LocationEngineBase" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk18LocationEngineBaseP" class="token"><code>LocationEngineBase</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Public protocol that describes the behaviour of <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>. Implementation is platform-specific.

  <a href="sdk-for-ios-navigate-protocols-locationenginebase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LocationEngineBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20LocationEngineStatusO"></span>` `<span id="//apple_ref/swift/Enum/LocationEngineStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk20LocationEngineStatusO" class="token"><code>LocationEngineStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the status of the LocationEngine.

  <a href="sdk-for-ios-navigate-enums-locationenginestatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationEngineStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15LocationFeatureO"></span>` `<span id="//apple_ref/swift/Enum/LocationFeature" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk15LocationFeatureO" class="token"><code>LocationFeature</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Location features supported by HERE positioning.

  <a href="sdk-for-ios-navigate-enums-locationfeature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationFeature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocationEngineC"></span>` `<span id="//apple_ref/swift/Class/LocationEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk14LocationEngineC" class="token"><code>LocationEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class handles location updates received according to the desired LocationAccuracy. Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one LocationEngine can be started at a time. Multiple delegates can be attached, either to receive location updates, see LocationUpdateDelegate, or status updates, see LocationStatusDelegate. When a different LocationAccuracy is desired, the LocationEngine needs to be stopped and started again.

  <a href="sdk-for-ios-navigate-classes-locationengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LocationEngine : LocationEngineBase
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationSimulatorC"></span>` `<span id="//apple_ref/swift/Class/LocationSimulator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk17LocationSimulatorC" class="token"><code>LocationSimulator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the `LocationSimulator` to generate locations along a route or a GPX document. It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions">`LocationSimulatorOptions`</a>. The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the `LocationSimulator` uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom `speedFactor` for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> and inserted into the provided <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object: `latitude, longitude, altitude, time, bearingInDegrees, speedInMetersPerSecond, horizontalAccuracyInMeters, verticalAccuracyInMeters` and `locationTechnology`.

  Note that simulation works offline and independent from any map data

  - only the information found in the provided route or GPX document is considered.
  - When initializing the `LocationSimulator` with a route, then interpolations take place between the vertices of the route’s polyline. The distance between interpolated locations is a function of the current span’s speed and the set notification interval.
  - When initializing the `LocationSimulator` with a GPX file, the `LocationSimulator` does not apply any interpolation on the provided location data as this would shadow the recorded GPX data.

  Notifications will stop after the entire route has been traveled.

  **Note:** Map-matched locations are only accessible from <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a>.

  <a href="sdk-for-ios-navigate-classes-locationsimulator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LocationSimulator
  ```

  ``` highlight
  extension LocationSimulator: NativeBase
  ```

  ``` highlight
  extension LocationSimulator: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24LocationSimulatorOptionsV"></span>` `<span id="//apple_ref/swift/Struct/LocationSimulatorOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk24LocationSimulatorOptionsV" class="token"><code>LocationSimulatorOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify how the location simulator will behave.

  <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocationSimulatorOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22LocationStatusDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/LocationStatusDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-positioning#/s:7heresdk22LocationStatusDelegateP" class="token"><code>LocationStatusDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for listening the LocationEngine status updates.

  <a href="sdk-for-ios-navigate-protocols-locationstatusdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LocationStatusDelegate : AnyObject
  ```

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


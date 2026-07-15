---
title: "LocationSimulator Class Reference"
slug: "sdk-for-ios-navigate-classes-locationsimulator"
---

# LocationSimulator

<div class="declaration">

<div class="language">

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

Use the `LocationSimulator` to generate locations along a route or a GPX document. It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions">`LocationSimulatorOptions`</a>. The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the `LocationSimulator` uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom `speedFactor` for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> and inserted into the provided <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object: `latitude, longitude, altitude, time, bearingInDegrees, speedInMetersPerSecond, horizontalAccuracyInMeters, verticalAccuracyInMeters` and `locationTechnology`.

Note that simulation works offline and independent from any map data

- only the information found in the provided route or GPX document is considered.
- When initializing the `LocationSimulator` with a route, then interpolations take place between the vertices of the route’s polyline. The distance between interpolated locations is a function of the current span’s speed and the set notification interval.
- When initializing the `LocationSimulator` with a GPX file, the `LocationSimulator` does not apply any interpolation on the provided location data as this would shadow the recorded GPX data.

Notifications will stop after the entire route has been traveled.

**Note:** Map-matched locations are only accessible from <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(route: options: )

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

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( route : Route , options : LocationSimulatorOptions ) throws
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
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>The route to travel.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options to specify how the location simulator will behave.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(gpxTrack: options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a location simulator

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( gpxTrack : GPXTrack , options : LocationSimulatorOptions ) throws
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
  <td><code> </code><em><code>gpxTrack</code></em><code> </code></td>
  <td><div>
  <p>The GPX track to travel.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options to specify how the location simulator will behave.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationSimulatorC8delegateAA0B8Delegate_pSgvp"></span>` `<span id="//apple_ref/swift/Property/delegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationsimulator#/s:7heresdk17LocationSimulatorC8delegateAA0B8Delegate_pSgvp" class="token"><code>delegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The object that notifies on location updates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var delegate: LocationDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      start()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts the location provider to send notifications to the subscribers. Calling this method will always start the location simulator from the route’s first <a href="sdk-for-ios-navigate-structs-waypoint">`Waypoint`</a>, even if a simulation has already been started or stopped.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start ()
  ```

  </pre>

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

  Stops the location provider from sending notifications to the subscribers.

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

      pause()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Pauses sending notifications to the subscribers. Calling this function has no effect when location provider is not started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func pause ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      resume()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Resumes sending notifications to the subscribers. Calling this function has no effect when location provider is not started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func resume ()
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


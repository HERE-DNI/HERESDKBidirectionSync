---
title: "ElectronicHorizonEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-electronichorizonengine"
---

# ElectronicHorizonEngine

<div class="declaration">

<div class="language">

``` highlight
public class ElectronicHorizonEngine
```

``` highlight
extension ElectronicHorizonEngine: NativeBase
```

``` highlight
extension ElectronicHorizonEngine: Hashable
```

</div>

</div>

Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight. You can subscribe to electronic horizon updates based on position updates by using <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a>. For more information about sub path levels, see <a href="sdk-for-ios-navigate-structs-electronichorizonoptions#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp">`ElectronicHorizonOptions.lookAheadDistancesInMeters`</a>.

The electronic horizon engine uses map-matched locations and can optionally use a <a href="sdk-for-ios-navigate-classes-route">`Route`</a> to improve the most-preferred path (MPP).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(sdkEngine: options: transportMode: route: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of `ElectronicHorizonEngine`.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> If the electronic horizon engine cannot be created.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( sdkEngine : SDKNativeEngine , options : ElectronicHorizonOptions , transportMode : TransportMode , route : Route ?) throws
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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-classes-sdknativeengine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-structs-electronichorizonoptions"><code>ElectronicHorizonOptions</code></a> instance that configures how the electronic horizon is calculated, including look-ahead distances.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>transportMode</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-enums-transportmode"><code>TransportMode</code></a> that is used when building the electronic horizon paths.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-classes-route"><code>Route</code></a> that improves the calculation of the most-preferred path (MPP). If <code>nil</code> is passed, the most-preferred path can deviate from the route.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23ElectronicHorizonEngineC5routeAA5RouteCSgvp"></span>` `<span id="//apple_ref/swift/Property/route" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-electronichorizonengine#/s:7heresdk23ElectronicHorizonEngineC5routeAA5RouteCSgvp" class="token"><code>route</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The instance of <a href="sdk-for-ios-navigate-classes-route">`Route`</a> that is being used by `ElectronicHorizonEngine`. You can override this property to rebuild the electronic horizon based on a different route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var route: Route? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      update(mapMatchedLocation: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates the electronic horizon paths based on the provided map-matched location. This method returns immediately and does not block. When internal calculation is complete, callbacks are called on the main thread. When multiple updates are triggered while processing is still running, intermediate locations are skipped and only the last location is processed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func update ( mapMatchedLocation : MapMatchedLocation )
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
  <td><code> </code><em><code>mapMatchedLocation</code></em><code> </code></td>
  <td><div>
  <p>The map-matched location that defines the current vehicle position on the road network.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addElectronicHorizonDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds an <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a> to the subscription list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addElectronicHorizonDelegate ( _ electronicHorizonListener : ElectronicHorizonDelegate )
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
  <td><code> </code><em><code>electronicHorizonListener</code></em><code> </code></td>
  <td><div>
  <p>The listener that receives electronic horizon path updates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeElectronicHorizonDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes an <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a> from the subscription list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeElectronicHorizonDelegate ( _ electronicHorizonListener : ElectronicHorizonDelegate )
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
  <td><code> </code><em><code>electronicHorizonListener</code></em><code> </code></td>
  <td><div>
  <p>The listener that should no longer receive electronic horizon path updates.</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


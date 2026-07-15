---
title: "RoutePrefetcher Class Reference"
slug: "sdk-for-ios-explore-classes-routeprefetcher"
---

# RoutePrefetcher

<div class="declaration">

<div class="language">

``` highlight
public class RoutePrefetcher
```

``` highlight
extension RoutePrefetcher: NativeBase
```

``` highlight
extension RoutePrefetcher: Hashable
```

</div>

</div>

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data. This allows scenarios such as navigation to work in a specific area reliably even though the network might be offline at that time. Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a RoutePrefetcher instance for a given <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ sdkEngine : SDKNativeEngine )
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
  <p>Instance of an existing SDKEngine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoutePrefetcherC28prefetchCorridorLengthMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/prefetchCorridorLengthMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-routeprefetcher#/s:7heresdk15RoutePrefetcherC28prefetchCorridorLengthMeterss5Int32Vvp" class="token"><code>prefetchCorridorLengthMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var prefetchCorridorLengthMeters: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      prefetchAroundLocationWithRadius(currentLocation: radiusInMeters: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Prefetches map data within a user-defined circular area around a given location. The radius, specified in meters, must be between 1 km and 50 km. If `nil` is passed as the radius, a default value of 2 km is used. It is recommended to call this method once before starting navigation to ensure a smooth experience.

  To control list of map content features for area prefetch, use <a href="sdk-for-ios-explore-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Please use `PolygonPrefetcher.prefetch(...﹚` instead.") public func prefetchAroundLocationWithRadius ( currentLocation : GeoCoordinates , radiusInMeters : Double ?)
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
  <td><code> </code><em><code>currentLocation</code></em><code> </code></td>
  <td><div>
  <p>The center of the circle to prefetch data within.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>radiusInMeters</code></em><code> </code></td>
  <td><div>
  <p>The radius of the circle to prefetch data within.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      prefetchAroundRouteOnIntervals(navigator: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Prefetches map data within a corridor along the route, that is currently set for the provided <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> instance. If no route is set, no data will be prefetched. The route corridor defaults to a length of 10 km and a width of 5 km. To prefetch the whole route before navigation has been started see

      RoutePrefetcher.prefetchGeoCorridor(...)

  . Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the end of the current corridor. Prefetching happens based on the current map-matched location - as indicated by the <a href="sdk-for-ios-explore-structs-routeprogress">`RouteProgress`</a> event. This method should be called right after navigation has started. In case of default prefetch length first prefetching will start after traveling a distance of 9 km along the route.
  </p>

  To control list of map content features for prefetch, use <a href="sdk-for-ios-explore-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func prefetchAroundRouteOnIntervals ( navigator : NavigatorProtocol )
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
  <td><code> </code><em><code>navigator</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-explore-protocols-navigatorprotocol"><code>NavigatorProtocol</code></a> to listen for Route Progress to prefetch data ahead.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      stopPrefetchAroundRoute()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops listening <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> passed to

      RoutePrefetcher.prefetchAroundRouteOnIntervals(...)

  for route progress events and stops prefetching data along the current route.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stopPrefetchAroundRoute ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      prefetchGeoCorridor(corridor: callback: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Prefetch tiles for a given geo-corridor. A geo-corridor can easily be created from a route with <a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp">`Route.geometry`</a> so navigation on this route is possible in offline cases. Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new prefetched tiles <a href="sdk-for-ios-explore-enums-maploadererror#/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF">`MapLoaderError.notEnoughSpace`</a> is returned. When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again. Please also note, any route calculation may not possible on prefetched tiles.

  To control list of map content features for corridor prefetch, use <a href="sdk-for-ios-explore-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func prefetchGeoCorridor ( corridor : GeoCorridor , callback : PrefetchStatusListener ) -> TaskHandle
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
  <td><code> </code><em><code>corridor</code></em><code> </code></td>
  <td><div>
  <p>indicates <a href="sdk-for-ios-explore-structs-geocorridor"><code>GeoCorridor</code></a> that can be constructed from the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>is invoked to report progress and the result of prefetch. After operation is finished,</p>
  <pre><code>onComplete(...)</code></pre>
  is invoked on the main thread. Progress is reported by invocation of
  <pre><code>onProgress(...)</code></pre>
  on the main thread.
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

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


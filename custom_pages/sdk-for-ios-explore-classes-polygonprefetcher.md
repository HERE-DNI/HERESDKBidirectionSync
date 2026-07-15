---
title: "PolygonPrefetcher Class Reference"
slug: "sdk-for-ios-explore-classes-polygonprefetcher"
---

# PolygonPrefetcher

<div class="declaration">

<div class="language">

``` highlight
public class PolygonPrefetcher
```

``` highlight
extension PolygonPrefetcher: NativeBase
```

``` highlight
extension PolygonPrefetcher: Hashable
```

</div>

</div>

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data. Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  Creates a PolygonPrefetcher instance for a given <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

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

      prefetch(geoPolygon: callback: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Prefetches map data for an area bounded by geo polygon. After the operation is finished

      onComplete(...)

  is invoked on the main thread. Progress is reported by invocation of
      onProgress(...)

  on the main thread. If there is not enough space left in the cache to store needed tiles, operation will fail with <a href="sdk-for-ios-explore-enums-maploadererror#/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF">`MapLoaderError.notEnoughSpace`</a>. To increase cache size, use <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">`SDKOptions.cacheSizeInBytes`</a> API.
  </p>

  To control list of map content features for area prefetch, use <a href="sdk-for-ios-explore-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  To prefetch map data within user-defined circular area around a given location:

  1.  Create a GeoCircle using the given location and radius.
  2.  Create a GeoPolygon using the GeoCircle.
  3.  Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API. Usage: GeoCircle geoCircle = GeoCircle(location, radius); GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func prefetch ( geoPolygon : GeoPolygon , callback : PrefetchStatusListener ) -> TaskHandle
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
  <td><code> </code><em><code>geoPolygon</code></em><code> </code></td>
  <td><div>
  <p>Area to prefetch map data for.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Callback that is triggered to report progress and the result of prefetch.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

      estimateMapDataSize(geoPolygon: callback: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimates map data size for the area bounded by geo polygon. Size for tiles that are already in the cache will not be included in the final result.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func estimateMapDataSize ( geoPolygon : GeoPolygon , callback : MapDataSizeListener ) -> TaskHandle
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
  <td><code> </code><em><code>geoPolygon</code></em><code> </code></td>
  <td><div>
  <p>Area to estimate map data size for.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Callback that is triggered to report the result of map data size estimation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

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

